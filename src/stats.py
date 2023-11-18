import numpy as np
from typing import List, Callable
import pandas as pd
import os


def bootstrap(data: List[np.array], func: Callable, niter: int = 10000) -> list:
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
    return np.array(
        bootstrap(
            data=[data_a, data_b],
            func=lambda x: np.mean(x[1]) - np.mean(x[0]),
            niter=niter,
        )
    )


def add_stats_table_row(
    figure: str,
    panel: str,
    sample_a: str,
    sample_b: str,
    measure: str, 
    comparisons: np.array,
    key: str,
    df_path: str = "../../../data/stats_table.csv",
):
    """_summary_

    Args:
        figure (str): _description_
        panel (str): _description_
        sample_a (str): _description_
        sample_b (str): _description_
        measure (str): _description_
        units (str): _description_
        comparisons (np.array): _description_
        comparison (str, optional): _description_. Defaults to "B-A".
        df_path (str, optional): _description_. Defaults to "../../../data/stats_table.csv".
    """

    # Import existing stats table
    if os.path.exists(df_path):
        df = pd.read_csv(df_path)
    else:
        df = pd.DataFrame()

    # Delete row if row already exists
    if not len(df.index[df['Key'] == key].tolist()) == 0:
        df = df.drop(df.index[df['Key'] == key].tolist()[0])

    # Create row
    row = {
        "Figure": figure,
        "Panel": panel,
        "Sample A": sample_a,
        "Sample B": sample_b,
        'Measure': measure, 
        "Effect size (B-A)": '{:.3g}'.format(np.mean(comparisons)),
        "95% CI (lower)": '{:.3g}'.format(np.percentile(comparisons, 2.5)),
        "95% CI (upper)": '{:.3g}'.format(np.percentile(comparisons, 97.5)),
        'Key': key
    }

    # Add row to dataframe
    df = pd.concat([df, pd.DataFrame(row, index=[0])], axis=0, ignore_index=True)

    # Order dataframe
    df = df.sort_values(by=["Figure", "Panel"])

    # Save dataframe
    df.to_csv(df_path, index=False)