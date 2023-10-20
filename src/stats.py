import numpy as np
from typing import List, Callable
import pandas as pd


def bootstrap(data: List[np.array], func: Callable, niter: int = 1000) -> np.array:
    """

    Basic function for doing bootstrap analysis

    Args:
        data (List[np.array]): data, list of numpy arrays
        func (Callable): will perform this function on the data to calculate output
            e.g. lambda x: np.mean(x[1]) - np.mean(x[0])
        niter (int, optional): number of bootstrap samples. Defaults to 1000.

    Returns:
        np.array: ninter bootstrap values
    """

    # Results containter
    output = np.zeros(niter)

    # ninter bootstraps
    for i in range(niter):
        # Loop through datasets, taking a subsample of each with replacement
        _data = []
        for d in data:
            d_sample = d[np.random.choice(range(len(d)), len(d))]
            _data.append(d_sample)

        # Perform function on _data to calculate output
        output[i] = func(_data)

    return output


def bootstrap_effect_size_pd(
    data: pd.DataFrame, x: str, y: str, a: str, b: str, niter: int = 1000
) -> np.array:
    """

    Bootstrapping on data in a pandas dataframe to find the effect size of an intervention

    Args:
        data (pd.Dataframe): pandas dataframe containing data
        x (str): name of x variable (categorical)
        y (str): name of y variable (continuous)
        a (str): category a of x
        b (str): category b of x
        niter (int): number of bootstrap samples

    Returns:
        np.array: bootstrap values of effect size (difference between means)
    """

    # Extract data from dataframe
    data_a = data[data[x] == a][y].to_numpy()
    data_b = data[data[x] == b][y].to_numpy()

    # Perform bootstrap analysis
    return bootstrap(
        data=[data_a, data_b], func=lambda x: np.mean(x[1]) - np.mean(x[0]), niter=niter
    )
