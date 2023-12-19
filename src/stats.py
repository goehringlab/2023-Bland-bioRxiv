import os
from typing import Callable, List

import numpy as np
import pandas as pd


def bootstrap(data: List[np.array], func: Callable, niter: int = 10000) -> list:
    """
    Basic function for doing bootstrap analysis.

    Args:
        data (List[np.array]): data, list of numpy arrays
        func (Callable): will perform this function on the data to calculate output
            e.g. lambda x: np.mean(x[1]) - np.mean(x[0])
        niter (int, optional): number of bootstrap samples. Defaults to 10000.

    Returns:
        np.array: ninter bootstrap values
    """

    # Results containter
    output = []

    # ninter bootstraps
    for i in range(niter):
        # Loop through datasets, taking a subsample of each with replacement
        _data = []
        for d in data:
            d_sample = d[np.random.choice(range(len(d)), len(d))]
            _data.append(d_sample)

        # Perform function on _data to calculate output
        output.append(func(_data))

    return output


def bootstrap_effect_size_pd(
    data: pd.DataFrame, x: str, y: str, a: str, b: str, niter: int = 10000
) -> np.array:
    """
    Bootstrapping on data in a pandas dataframe to find the effect size of an intervention.

    Args:
        data (pd.Dataframe): pandas dataframe containing data
        x (str): name of x variable (categorical)
        y (str): name of y variable (continuous)
        a (str): category a of x
        b (str): category b of x
        niter (int): number of bootstrap samples

    """

    # Extract data from dataframe
    data_a = data[data[x] == a][y].to_numpy()
    data_b = data[data[x] == b][y].to_numpy()

    # Sample size
    sample_size_a = len(data_a)
    sample_size_b = len(data_b)

    # Calculate effect size
    effect_size = np.mean(data_b) - np.mean(data_a)

    # Perform bootstrap analysis
    probability_distribution = np.array(
        bootstrap(
            data=[data_a, data_b],
            func=lambda x: np.mean(x[1]) - np.mean(x[0]),
            niter=niter,
        )
    )

    return effect_size, probability_distribution, (sample_size_a, sample_size_b)


def add_stats_table_row(
    figure: str,
    panel: str,
    sample_a: str,
    sample_b: str,
    measure: str,
    effect_size: float,
    sample_size: tuple,
    probability_distribution: np.array,
    key: str,
    df_path: str = "../../../data/stats_table.csv",
):
    # Import existing stats table
    if os.path.exists(df_path):
        df = pd.read_csv(df_path)
    else:
        df = pd.DataFrame()

    # Delete row if row already exists
    if "Key" in df.columns and not len(df.index[df["Key"] == key].tolist()) == 0:
        df = df.drop(df.index[df["Key"] == key].tolist()[0])

    # Create row
    row = {
        "Figure": figure,
        "Panel": panel,
        "Sample A": sample_a,
        "Sample B": sample_b,
        "Measure": measure,
        "Sample size A": sample_size[0],
        "Sample size B": sample_size[1],
        "Effect size (B-A)": "{:.3g}".format(effect_size),
        "95% CI (lower)": "{:.3g}".format(np.percentile(probability_distribution, 2.5)),
        "95% CI (upper)": "{:.3g}".format(
            np.percentile(probability_distribution, 97.5)
        ),
        "Key": key,
    }

    # Add row to dataframe
    df = pd.concat([df, pd.DataFrame(row, index=[0])], axis=0, ignore_index=True)

    # Format columns
    df["Sample size A"] = df["Sample size A"].astype(int)
    df["Sample size B"] = df["Sample size B"].astype(int)

    # Order dataframe
    df = df.sort_values(by=["Figure", "Panel"])

    # Save dataframe
    df.to_csv(df_path, index=False)
