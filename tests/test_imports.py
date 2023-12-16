import glob
import os

import nbformat
import pytest
from nbconvert.preprocessors import ExecutePreprocessor

from src import direcslist

# Gather file list
file_list1 = sorted(glob.glob("scripts/Run/*.ipynb"))
file_list2 = []
for p in direcslist("scripts/Analysis"):
    file_list2.extend(glob.glob(p + "/*.ipynb"))
file_list2 = sorted(file_list2)
file_list = file_list1 + file_list2


@pytest.mark.parametrize("notebook_filename", file_list)
def test_nb_imports(notebook_filename):
    run_path = os.path.dirname(notebook_filename)
    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)
        first_code_cell = next(
            (cell for cell in nb.cells if cell.cell_type == "code"), None
        )
        new_nb = nbformat.v4.new_notebook(cells=[first_code_cell])
        ep = ExecutePreprocessor(kernel_name="python3")
        ep.preprocess(new_nb, {"metadata": {"path": run_path}})
