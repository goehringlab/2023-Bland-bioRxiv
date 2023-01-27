# Bland et al., 2023

[![CC BY 4.0][cc-by-shield]][cc-by]

Complete analysis code for Bland et al., 2023

## Installation

To install on your local machine, run the following:

&#8291;1. Clone the repository:

    git clone https://github.com/tsmbland/Bland-et-al-2023.git
    cd Bland-et-al-2023

&#8291;2. Create conda environment:

    conda env create -f environment.yml

&#8291;3. Activate conda environment:

    conda activate par2_paper


## Notebooks

Notebooks used to perform the analysis in the paper and generate all the figures are found in _scripts_.
This is split into two sections:

- __Raw analysis__: notebooks used to perform quantification on raw images. Running these scripts requires access to the
  main data repository (i.e. image files), which can be made available on request
- __Downstream analysis and figures__: notebooks used to perform downstream analysis on the quantification results from
  above and generate figures.
  Most of these can be run without access to the main data repository, but some do require access to raw data (these
  notebooks are
  marked with an underscore at the end of the file name).
  Also includes SEC-MALS analysis and modelling

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/

[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg