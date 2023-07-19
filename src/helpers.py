import numpy as np
from matplotlib.ticker import FuncFormatter
import pandas as pd
import seaborn as sns
from par_segmentation import *
from discco import ImageQuant2

np.random.seed(12345)

data_path = '/Users/blandt/Desktop/PaperData/'
if data_path:
    data_access = True

def lighten(color, amount=1.8):
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], max(0, min(1, amount * c[1])), c[2])


def _fake_log(x, pos):
    'The two args are the value and tick position'
    return r'$10^{%d}$' % (x)


fake_log = FuncFormatter(_fake_log)


def minor_ticks(ax, x=True, y=True):
    # Get axis limits
    xrange = ax.get_xlim()
    yrange = ax.get_ylim()

    # Create minor x ticks
    if x:
        minor_x_ticks = np.array([])
        for i in range(int(np.floor(xrange[0])), int(np.ceil(xrange[1]))):
            a = np.log10(np.linspace(10 ** i, 10 ** (i + 1), 10))
            minor_x_ticks = np.append(minor_x_ticks, a)
        ax.set_xticks(minor_x_ticks, minor=True)

    # Create minor y ticks
    if y:
        minor_y_ticks = np.array([])
        for i in range(int(np.floor(yrange[0])), int(np.ceil(yrange[1]))):
            a = np.log10(np.linspace(10 ** i, 10 ** (i + 1), 10))
            minor_y_ticks = np.append(minor_y_ticks, a)
        ax.set_yticks(minor_y_ticks, minor=True)

    # Restore axis limits
    ax.set_xlim(*xrange)
    ax.set_ylim(*yrange)
