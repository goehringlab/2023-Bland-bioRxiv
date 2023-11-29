# PYDEVD_DISABLE_FILE_VALIDATION=1 TF_CPP_MIN_LOG_LEVEL=3 python run_all.py

import glob
import os
import time

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError

from src import direcslist

# Gather file list
file_list1 = sorted(glob.glob("Run/*.ipynb"))

file_list2 = []
for p in direcslist("Analysis"):
    file_list2.extend(glob.glob(p + "/*.ipynb"))
file_list2 = sorted(file_list2)
file_list = file_list1 + file_list2

# Start timer
start_time = time.time()

# Execute notebooks and save output
num_notebooks = len(file_list)
for i, f in enumerate(file_list):
    run_path = os.path.dirname(f)
    with open(f) as file:
        nb = nbformat.read(file, as_version=4)
        ep = ExecutePreprocessor(kernel_name="python3")
        try:
            print("Running", f, ":", i + 1, "/", num_notebooks)
            out = ep.preprocess(nb, {"metadata": {"path": run_path}})
        except CellExecutionError:
            out = None
            msg = 'Error executing the notebook "%s".\n' % f
            print(msg)
        except TimeoutError:
            msg = 'Timeout executing the notebook "%s".\n' % f
            print(msg)
        finally:
            # Save output
            nbformat.write(nb, f)

# Time elapsed
elapsed_time = time.time() - start_time
print(
    "Finished! (%s minutes, %s seconds)"
    % (int(elapsed_time // 60), int(elapsed_time % 60))
)
