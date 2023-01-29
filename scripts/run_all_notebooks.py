import sys

sys.path.append('../src')
from helpers import *
import glob
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError
import argparse

# Parse args
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--data-access', default='True', required=False)
args = parser.parse_args()
data_access = args.data_access == 'True'

# Gather file list
file_list1 = []
for p in direcslist('Raw analysis'):
    file_list1.extend(glob.glob(p + '/*.ipynb'))
file_list1 = sorted(file_list1)
file_list2 = []
for p in direcslist('Downstream analysis and figures'):
    file_list2.extend(glob.glob(p + '/*.ipynb'))
file_list2 = sorted(file_list2)

# Filter file list
if not data_access:
    file_list = [f for f in file_list2 if not f[-7] == '_']  # remove scripts that require raw data
else:
    file_list = file_list1 + file_list2

# Execute notebooks and output
num_notebooks = len(file_list)
for i, f in enumerate(file_list):
    run_path = os.path.dirname(f)
    with open(f) as file:
        nb = nbformat.read(file, as_version=4)
        ep = ExecutePreprocessor(kernel_name='python3')
        try:
            print('Running', f, ':', i + 1, '/', num_notebooks)
            out = ep.preprocess(nb, {'metadata': {'path': run_path}})
        except CellExecutionError:
            out = None
            msg = 'Error executing the notebook "%s".\n' % f
            print(msg)
        except TimeoutError:
            msg = 'Timeout executing the notebook "%s".\n' % f
            print(msg)
        # finally:
        #     # Save output
        #     nbformat.write(nb, f)
