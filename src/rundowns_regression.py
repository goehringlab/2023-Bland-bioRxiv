import numpy as np

from .stats import bootstrap


def linear_model(x, a, b):
    return a * x + b


def single_fit(cyt, mem):
    p = np.polyfit(cyt, mem, 1)
    return p


class ExponentConfidenceInterval:
    def __init__(self, df, whole_embryo=False, xmin=None, xmax=None, n_x=100):
        # Input
        self.cyts = np.log10(df.Cyt.to_numpy())
        self.mems = np.log10(
            df.Mem_post.to_numpy() if not whole_embryo else df.Mem_tot.to_numpy()
        )
        self.unipol = df.UniPol.tolist()

        # Set xmin and xmax if not provided
        xmin = xmin if xmin is not None else min(self.cyts)
        xmax = xmax if xmax is not None else max(self.cyts)

        self.res_x = np.linspace(xmin, xmax, n_x)

        # Run
        self.run()

    def run(self, n_bootstrap=10000, interval=95):
        # Analysing full dataset
        popt_full = single_fit(self.cyts, self.mems)
        self.res_y = linear_model(self.res_x, *popt_full)
        self.exponent_full = popt_full[0]

        # Bootstrapping
        params = np.array(
            bootstrap(
                data=[
                    np.c_[self.cyts, self.mems],
                ],
                func=lambda x: single_fit(x[0][:, 0], x[0][:, 1]),
                niter=n_bootstrap,
            )
        )
        self.exponents = params[:, 0]

        # Confidence interval
        all_fits = np.zeros([n_bootstrap, len(self.res_x)])
        for i, p in enumerate(params):
            all_fits[i, :] = linear_model(self.res_x, *p)
        self.all_fits_lower, self.all_fits_upper = np.percentile(
            all_fits, [(100 - interval) / 2, 50 + (interval / 2)], axis=0
        )
