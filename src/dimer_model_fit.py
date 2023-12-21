import numpy as np
from scipy.optimize import curve_fit

"""
Model

"""


def model_m_from_c(ka, km, c):
    # See notebook 'Dimer model solving'
    return (
        c
        * km
        * (
            2 * c * ka * km * (4 * c * ka + np.sqrt(8 * c * ka + 1) + 1)
            + np.sqrt(
                32 * c**3 * ka**3
                + 24 * c**2 * ka**2 * np.sqrt(8 * c * ka + 1)
                + 72 * c**2 * ka**2
                + 16 * c * ka * np.sqrt(8 * c * ka + 1)
                + 24 * c * ka
                + 2 * np.sqrt(8 * c * ka + 1)
                + 2
            )
        )
        / (
            8 * c**2 * ka**2
            + 4 * c * ka * np.sqrt(8 * c * ka + 1)
            + 8 * c * ka
            + np.sqrt(8 * c * ka + 1)
            + 1
        )
    )


# Note: from here on ka and km are expressed in log10 format


def model_unpaired(cyt, ka, km):
    c1 = cyt
    m1 = model_m_from_c(10**ka, 10**km, c1)
    return m1


def model_unpaired_log(logcyt, ka, km):
    c1 = 10**logcyt
    m1 = model_m_from_c(10**ka, 10**km, c1)
    return np.log10(m1)


def model_paired(cyt_l109r, ka1, ka2, km):
    cyt, l109r = cyt_l109r
    ka = (ka1 * np.array([l109r == 0])).flatten() + (
        ka2 * np.array([l109r == 1])
    ).flatten()
    c1 = cyt
    m1 = model_m_from_c(10**ka, 10**km, c1)
    return m1


def model_log_paired(logcyt_l109r, ka1, ka2, km):
    logcyt, l109r = logcyt_l109r
    cyt = 10**logcyt
    c1 = cyt
    ka = (ka1 * np.array([l109r == 0])).flatten() + (
        ka2 * np.array([l109r == 1])
    ).flatten()
    m1 = model_m_from_c(10**ka, 10**km, c1)
    return np.log10(m1)


def model_log_paired_D(logcyt_l109r, ka1, ka2, km, D):
    logcyt, l109r = logcyt_l109r
    cyt = 10**logcyt
    c1 = cyt
    ka = (ka1 * np.array([l109r == 0])).flatten() + (
        ka2 * np.array([l109r == 1])
    ).flatten()
    m1 = model_m_from_c(10**ka, 10**km, c1)
    return np.log10(m1) * (10**D)


def monomer_fraction(conc, ka):
    return ((np.sqrt(4 * conc * (10**ka) + 1) - 1) / (2 * (10**ka))) / conc


def dimer_fraction(conc, ka):
    return 1 - (((np.sqrt(4 * conc * (10**ka) + 1) - 1) / (2 * (10**ka))) / conc)


"""
Fitting

"""


class EnergiesConfidenceIntervalPaired:
    """A class used to calculate the confidence interval of energy levels in a paired system."""

    def __init__(
        self,
        df,
        region="post",
        log=False,
        p0=(15, 15, 5),
        fix_wt=False,
        fix_mut=False,
        fit_D=False,
    ):
        """
        Initializes the class with the given parameters and data.

        Args:
            df (pd.DataFrame): The data frame containing the data.
            region (str, optional): The region of interest. "post" or "whole". Defaults to "post".
            log (bool, optional): A flag to determine if logarithmic calculations should be used. Defaults to False.
            p0 (tuple, optional): The initial guess for the parameters. Defaults to (15, 15, 5).
            fix_wt (bool, optional): A flag to determine if the wild type dimer enenrgy should be fixed. Defaults to False.
            fix_mut (bool, optional): A flag to determine if the mutant dimer energy should be fixed. Defaults to False.
            fit_D (bool, optional): A flag to determine if the D parameter should be fit. Defaults to False.
        """

        # Import data
        self.log = log
        if region == "post":
            self.mems = (
                np.log10(df.Mem_post.to_numpy()) if self.log else df.Mem_post.to_numpy()
            )
        elif region == "whole":
            self.mems = (
                np.log10(df.Mem_tot.to_numpy()) if self.log else df.Mem_tot.to_numpy()
            )
        else:
            self.mems = None
        self.cyts = np.log10(df.Cyt.to_numpy()) if self.log else df.Cyt.to_numpy()
        self.l109r = (df.Genotype == "L109R").to_numpy() * 1
        self.unipol = df.UniPol.tolist()
        self.p0 = p0
        self.fix_wt = fix_wt
        self.fix_mut = fix_mut
        self.fit_D = fit_D

        # Model
        if self.log:
            self.model = model_log_paired_D if self.fit_D else model_log_paired
        else:
            self.model = model_paired

        # Output
        self.res_x = [None, None]
        self.res_y = [None, None]
        self.ka_full = [None, None]
        self.km_full = None
        self.kas = [None, None]
        self.kms = None
        self.all_fits_lower = [None, None]
        self.all_fits_upper = [None, None]
        self.cyt_dim = [None, None]
        self.mem_dim = [None, None]
        self.cyt_dim_lower = [None, None]
        self.cyt_dim_upper = [None, None]
        self.mem_dim_lower = [None, None]
        self.mem_dim_upper = [None, None]

        # Run
        self.p0_curve_fit, self.bounds_curve_fit = self.setup_curve_fit()
        self.run()

    def run(self, n_bootstrap=10000, n_x=100, interval=95):
        """
        Executes the model fitting and bootstrapping process.

        Args:
            n_bootstrap (int, optional): The number of bootstrap samples to generate. Defaults to 10000.
            n_x (int, optional): The number of points to generate for the x-axis of the result plots. Defaults to 100.
            interval (int, optional): The confidence interval for the bootstrap estimates. Defaults to 95.
        """
        # Fit the model to the full dataset
        popt_full = self.single_fit([self.cyts, self.l109r], self.mems)

        # Generate x-axis points for the plots
        self.res_x = [
            np.linspace(
                np.min(self.cyts[self.l109r == i]),
                np.max(self.cyts[self.l109r == i]),
                n_x,
            )
            for i in range(2)
        ]

        # Calculate the model predictions for the plots
        self.res_y = [
            self.model(
                [
                    self.res_x[i],
                    np.ones(len(self.res_x[i])) if i else np.zeros(len(self.res_x[i])),
                ],
                *popt_full,
            )
            for i in range(2)
        ]

        # Extract the fitted parameters
        self.ka_full = [popt_full[0], popt_full[1]]
        self.km_full = popt_full[2]

        # If fit_D is True, print D
        if self.fit_D:
            print(popt_full[3])

        # Calculate the dimer fractions for each genotype
        for i in range(2):
            self.cyt_dim[i] = 100 * dimer_fraction(
                10 ** self.res_x[i] if self.log else self.res_x[i], self.ka_full[i]
            )
            self.mem_dim[i] = 100 * dimer_fraction(
                10 ** self.res_y[i] if self.log else self.res_y[i], self.ka_full[i]
            )

        # Perform bootstrapping to estimate the parameters
        params = self.bootstrap_fitting([self.cyts, self.l109r], self.mems)
        self.kas = [params[:, 0], params[:, 1]]
        self.kms = params[:, 2]

        # Initialize arrays to store the bootstrap estimates
        all_fits = [np.zeros([n_bootstrap, n_x]) for _ in range(2)]
        all_cyt_dim = [np.zeros([n_bootstrap, n_x]) for _ in range(2)]
        all_mem_dim = [np.zeros([n_bootstrap, n_x]) for _ in range(2)]

        # Calculate the model predictions and dimer fractions for each bootstrap sample
        for j in range(2):
            for i, p in enumerate(params):
                all_fits[j][i, :] = self.model(
                    [
                        self.res_x[j],
                        np.ones(len(self.res_x[j]))
                        if j
                        else np.zeros(len(self.res_x[j])),
                    ],
                    *p,
                )
                all_cyt_dim[j][i, :] = 100 * dimer_fraction(
                    10 ** self.res_x[j] if self.log else self.res_x[j], p[j]
                )
                all_mem_dim[j][i, :] = 100 * dimer_fraction(
                    10 ** self.res_y[j] if self.log else self.res_y[j], p[j]
                )

            # Calculate the lower and upper bounds of the confidence interval for each estimate
            self.all_fits_lower[j] = np.percentile(
                all_fits[j], (100 - interval) / 2, axis=0
            )
            self.all_fits_upper[j] = np.percentile(
                all_fits[j], 50 + (interval / 2), axis=0
            )
            self.cyt_dim_lower[j] = np.percentile(
                all_cyt_dim[j], (100 - interval) / 2, axis=0
            )
            self.cyt_dim_upper[j] = np.percentile(
                all_cyt_dim[j], 50 + (interval / 2), axis=0
            )
            self.mem_dim_lower[j] = np.percentile(
                all_mem_dim[j], (100 - interval) / 2, axis=0
            )
            self.mem_dim_upper[j] = np.percentile(
                all_mem_dim[j], 50 + (interval / 2), axis=0
            )

    def setup_curve_fit(self):
        """
        Sets up the initial guess and bounds for the curve fitting process.

        Returns:
            list: The initial guess for the parameters.
            list: The lower and upper bounds for the parameters.

        """

        # Small value used to set bounds for fixed parameters
        epsilon = 0.00000001

        # Initialize bounds for the parameters
        bounds = [[-np.inf, -np.inf, -np.inf], [np.inf, np.inf, np.inf]]

        # If the wild type parameter is fixed, set its bounds to be very close to the initial guess
        if self.fix_wt:
            bounds[0][0], bounds[1][0] = self.p0[0] - epsilon, self.p0[0] + epsilon

        # If the mutant parameter is fixed, set its bounds to be very close to the initial guess
        if self.fix_mut:
            bounds[0][1], bounds[1][1] = self.p0[1] - epsilon, self.p0[1] + epsilon

        # Initialize the initial guess for the parameters
        p0 = list(self.p0)

        # If the D parameter is being fit, add it to the bounds and initial guess
        if self.fit_D:
            bounds[0].append(-np.inf)
            bounds[1].append(np.inf)
            p0.append(0)

        return p0, bounds

    def single_fit(self, cyt_l109r, mem):
        """
        Fits the model to the data.

        Args:
            cyt_l109r (list): Cytoplasmic concentrations and L109R genotype
            mem (np.array): Membrane concentrations

        Returns:
            params (np.array): The parameters of the fitted model.
        """

        popt, _ = curve_fit(
            self.model,
            np.array(cyt_l109r),
            mem,
            maxfev=10000000,
            p0=self.p0_curve_fit,
            bounds=self.bounds_curve_fit,
        )
        return popt

    def bootstrap_fitting(self, cyts_l109r, mems, n=10000):
        """
        Performs bootstrapping to estimate the parameters of the model.

        Args:
            cyts_l109r (list): Cytoplasmic concentrations and L109R genotype
            mems (np.array): Membrane concentrations
            n (int, optional): The number of bootstrap samples to generate. Defaults to 10000.

        Returns:
            params (np.array): The parameters of the fitted model for each bootstrap sample.
        """
        # Split the input list into cytoplasmic concentrations and L109R genotype
        cyts, l109r = cyts_l109r

        # Initialize an array to store the parameters for each bootstrap sample
        # The number of parameters depends on whether the D parameter is being fit
        params = np.zeros([n, 4]) if self.fit_D else np.zeros([n, 3])

        # Perform bootstrapping
        for i in range(n):
            # Initialize lists to store the bootstrap samples
            _cyts, _mems, _l109r = [], [], []

            # Generate a bootstrap sample for each genotype
            for j in range(2):
                # Select the data for the current genotype
                __cyts = cyts[l109r == j]
                __mems = mems[l109r == j]

                # Generate a bootstrap sample by randomly selecting data with replacement
                inds = np.random.choice(range(len(__cyts)), len(__cyts))
                _cyts.append(__cyts[inds])
                _mems.append(__mems[inds])
                _l109r.append(np.full(len(inds), j))

            # Compile the bootstrap samples into arrays
            _cyts = np.concatenate(_cyts)
            _mems = np.concatenate(_mems)
            _l109r = np.concatenate(_l109r)

            # Fit the model to the bootstrap sample and store the parameters
            params[i, :] = self.single_fit([_cyts, _l109r], _mems)

        # Return the parameters for each bootstrap sample
        return params
