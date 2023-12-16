import colorsys
import os
import random

import matplotlib as mpl
import matplotlib.colors as mc
import numpy as np
import seaborn as sns
from matplotlib.ticker import FuncFormatter

random.seed(12345)
np.random.seed(12345)

""" 
Path to the raw data

"""

if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/../raw_data/"):
    raw_data_path = os.path.dirname(os.path.abspath(__file__)) + "/../raw_data/"
else:
    raw_data_path = None


"""
Setup notebooks

"""


def nb_setup():
    # Random seed
    random.seed(12345)
    np.random.seed(12345)

    # Matplotib setup
    mpl.rcParams["pdf.fonttype"] = 42
    mpl.rcParams["ps.usedistiller"] = "xpdf"
    mpl.rc("font", **{"family": "sans-serif", "sans-serif": ["Myriad Pro"]})


"""
Plotting

"""


def dataplot(
    data,
    x,
    y,
    ax,
    order,
    width=0.4,
    linewidth=1,
    transform=None,
    offset=0,
    color=None,
    hue=None,
    palette=None,
    marker="o",
    linewidth_mean=1,
):
    """

    Main function for swarmplots in the paper

    Args:
        data (_type_): pandas dataframe
        x (_type_): name of x axis variable (categorical variable)
        y (_type_): name of y axis variable (continuous variable)
        ax (_type_): axis
        order (_type_): order of categorical values
        width (float, optional): width of mean line. Defaults to 0.4.
        linewidth (int, optional): linewidth for points. Defaults to 1.
        transform (_type_, optional): for moving the points left or right. Defaults to None.
        offset (int, optional): offset value for the mean line. Defaults to 0.
        color (_type_, optional): color of points (if using single color). Defaults to None.
        hue (_type_, optional): categorical variable for hue. Defaults to None.
        palette (_type_, optional): dictionary for hue. Defaults to None.
        marker (str, optional): marker style for points. Defaults to 'o'.
        linewidth_mean (int, optional): thickness of mean line. Defaults to 1.
    """

    # Calculate means
    df_mean = [data[data[x] == o][y].mean() for o in order]

    # Draw mean lines
    [
        ax.hlines(
            y,
            i + offset - width / 2,
            i + offset + width / 2,
            zorder=100,
            color="k",
            linewidth=linewidth_mean,
        )
        for i, y in enumerate(df_mean)
    ]

    # Draw points
    sns.swarmplot(
        data=data,
        x=x,
        y=y,
        ax=ax,
        order=order,
        linewidth=linewidth,
        transform=transform,
        color=color,
        hue=hue,
        palette=palette,
        marker=marker,
    )


def lighten(color, amount=1.8):
    try:
        c = mc.cnames[color]
    except:  # noqa
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], max(0, min(1, amount * c[1])), c[2])


def _fake_log(x, pos):
    "The two args are the value and tick position"
    return r"$10^{%d}$" % (x)


fake_log = FuncFormatter(_fake_log)


def minor_ticks(ax, x=True, y=True):
    # Get axis limits
    xrange = ax.get_xlim()
    yrange = ax.get_ylim()

    # Create minor x ticks
    if x:
        minor_x_ticks = np.array([])
        for i in range(int(np.floor(xrange[0])), int(np.ceil(xrange[1]))):
            a = np.log10(np.linspace(10**i, 10 ** (i + 1), 10))
            minor_x_ticks = np.append(minor_x_ticks, a)
        ax.set_xticks(minor_x_ticks, minor=True)

    # Create minor y ticks
    if y:
        minor_y_ticks = np.array([])
        for i in range(int(np.floor(yrange[0])), int(np.ceil(yrange[1]))):
            a = np.log10(np.linspace(10**i, 10 ** (i + 1), 10))
            minor_y_ticks = np.append(minor_y_ticks, a)
        ax.set_yticks(minor_y_ticks, minor=True)

    # Restore axis limits
    ax.set_xlim(*xrange)
    ax.set_ylim(*yrange)


class random_grouped_scatter:
    def __init__(self, linewidth=0.1, edgecolors="k", s=20):
        self.points = []
        self.linewidth = linewidth
        self.edgecolors = edgecolors
        self.s = s

    def add(self, x, y, color, marker="o"):
        for _x, _y in zip(x, y):
            self.points.append({"x": _x, "y": _y, "color": color, "marker": marker})

    def plot(self, ax):
        random.shuffle(self.points)
        for p in self.points:
            ax.scatter(
                p["x"],
                p["y"],
                linewidth=self.linewidth,
                edgecolors=self.edgecolors,
                s=self.s,
                color=p["color"],
                marker=p["marker"],
            )


@FuncFormatter
def log_molar_to_micromolar(x, pos):
    "The two args are the value and tick position"
    return r"$10^{%d}$" % (x + 6)


"""
Array manipulation

"""


def fold(array):
    return (array[:50][::-1] + array[50:]) / 2
