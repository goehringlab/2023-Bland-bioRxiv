import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.colors as mc
import colorsys
import random

np.random.seed(12345)

raw_data_path = "/Users/blandt/Desktop/PaperData/"

"""
Plotting

"""

def lighten(color, amount=1.8):
    try:
        c = mc.cnames[color]
    except:
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
