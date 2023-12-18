import os
import random

import matplotlib as mpl
import numpy as np

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
    mpl.rcParams["figure.dpi"] = 150
    mpl.rcParams["pdf.fonttype"] = 42
    mpl.rcParams["svg.fonttype"] = "none"
    mpl.rcParams["ps.usedistiller"] = "xpdf"
    mpl.rc("font", **{"family": "sans-serif", "sans-serif": ["Arial"]})
    mpl.rcParams["mathtext.fontset"] = "custom"
    mpl.rcParams["mathtext.rm"] = "Arial"
    mpl.rcParams["mathtext.it"] = "Arial:italic"
    mpl.rcParams["mathtext.bf"] = "Arial:bold"


"""
Array manipulation

"""


def fold(array):
    return (array[:50][::-1] + array[50:]) / 2
