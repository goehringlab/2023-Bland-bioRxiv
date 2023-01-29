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


## Data

Think about options for making entire dataset publicly available (e.g. EBI BioImage archive)

## Notebooks

Notebooks used to perform the analysis in the paper and generate all the figures are found in _scripts_.
This is split into two sections:

- __Raw analysis__: notebooks used to perform quantification on raw images. Running these scripts requires access to the
  main data repository (i.e. image files). 
- __Downstream analysis and figures__: notebooks used to perform downstream analysis on the quantification results from
  above and generate figures.
  Most of these can be run without access to the main data repository, but some do require access to raw data (e.g. figures showing specific embryos).
  These notebooks are marked with an underscore at the end of their file name.
  Also includes SEC-MALS analysis and modelling.

Code for creating specific figure panels (to do: create links):

[n0]: scripts/Downstream%20analysis%20and%20figures/Dimer%20model%20fitting/00%20ProcessData.ipynb
[n1]: scripts/Downstream%20analysis%20and%20figures/Dimer%20model%20fitting/01%20Figures.ipynb
[n2]: scripts/Downstream%20analysis%20and%20figures/Dimer%20model%20fitting/01%20Figures2.ipynb
[n3]: scripts/Downstream%20analysis%20and%20figures/Dimer%20model%20fitting/02%20All%20fits.ipynb
[n4]: scripts/Downstream%20analysis%20and%20figures/Dimer%20model%20solving/01%20Solve%20model.ipynb
[n5]: scripts/Downstream%20analysis%20and%20figures/GCN4/Figures%20PRBH_.ipynb
[n6]: scripts/Downstream%20analysis%20and%20figures/GCN4/Figures%20S241A_.ipynb
[n7]: scripts/Downstream%20analysis%20and%20figures/GCN4/Figures%20fragment_.ipynb
[n8]: scripts/Downstream%20analysis%20and%20figures/GCN4/Figures%20par3%20mut_.ipynb
[n9]: scripts/Downstream%20analysis%20and%20figures/GCN4/Figures_.ipynb
[n10]: scripts/Downstream%20analysis%20and%20figures/Model%20nonlinearity/Figs.ipynb
[n11]: scripts/Downstream%20analysis%20and%20figures/Optogenetics%20analysis/Optogenetics%20figures_.ipynb
[n12]: scripts/Downstream%20analysis%20and%20figures/PH%20rundown/Figs_log_transformed.ipynb
[n13]: scripts/Downstream%20analysis%20and%20figures/Polarised%20vs%20uniform/Figures_.ipynb
[n14]: scripts/Downstream%20analysis%20and%20figures/Quantification%20method/Comparison%20to%20old%20method_.ipynb
[n15]: scripts/Downstream%20analysis%20and%20figures/Quantification%20method/Schematic%20membrane%20profile.ipynb
[n16]: scripts/Downstream%20analysis%20and%20figures/Quantification%20method/Schematic.ipynb
[n17]: scripts/Downstream%20analysis%20and%20figures/Quantification%20model%20calibration%20comparison/Figures%20bgcurves.ipynb
[n18]: scripts/Downstream%20analysis%20and%20figures/Quantification%20summary%20table/Results%20table%202.ipynb
[n19]: scripts/Downstream%20analysis%20and%20figures/Quantification%20summary%20table/Results%20table.ipynb
[n20]: scripts/Downstream%20analysis%20and%20figures/RING%20PH/Figures_.ipynb
[n21]: scripts/Downstream%20analysis%20and%20figures/RING%20combined%20mutants/Untitled.ipynb
[n22]: scripts/Downstream%20analysis%20and%20figures/RING%20fragment/Figures_.ipynb
[n23]: scripts/Downstream%20analysis%20and%20figures/Rundowns%20regression/Fitting%20log%20transformed.ipynb
[n24]: scripts/Downstream%20analysis%20and%20figures/Rundowns%20regression/Schematic.ipynb
[n25]: scripts/Downstream%20analysis%20and%20figures/SEC%20MALS/Titration_curves.ipynb
[n26]: scripts/Downstream%20analysis%20and%20figures/SEC%20MALS/Traces_.ipynb
[n27]: scripts/Downstream%20analysis%20and%20figures/SEC%20MALS/xml_extract_.ipynb
[n28]: scripts/Downstream%20analysis%20and%20figures/SEC%20MALS/xml_extract_L109R_.ipynb
[n29]: scripts/Downstream%20analysis%20and%20figures/Three%20compartment%20model/Equilibrium.ipynb
[n30]: scripts/Downstream%20analysis%20and%20figures/Three%20compartment%20model/Kinetic.ipynb
[n31]: scripts/Downstream%20analysis%20and%20figures/Three%20compartment%20model/Prefactor.ipynb
[n32]: scripts/Downstream%20analysis%20and%20figures/mlc-4%20RNAi/Quantification%20figs.ipynb
[n33]: scripts/Downstream%20analysis%20and%20figures/mlc-4%20RNAi/SAIBR%20figs_.ipynb
[n34]: scripts/Downstream%20analysis%20and%20figures/nop-1/2cell%20asymmetry.ipynb
[n35]: scripts/Downstream%20analysis%20and%20figures/nop-1/Lethality.ipynb


Figure 1: D, E, F, G\
Figure 2: C, D, E, F, G, H, I\
Figure 3: B, C, D, E, F, G, H, I\
Figure 4: A, B, C, D, E\
Figure 5: A, C, D, E, F, G, H\
Figure S1: C, D, F, G\
Figure S2\
Figure S5: B\
Figure S5: B, C\
Table S1\
Table S3

## Full analysis

To perform all analysis and generate all figures:

    cd scripts
    python run_all_notebooks.py

This will create and populate a series of 'Figs' folders in _scripts_ containing PNGs of individual figure panels.
Will take around half an hour to run depending on the machine.
Note, running the complete analysis requires access to raw data.
If you have access to this data, be sure to specify the _data_path_ variable in _src/helpers.py_.
If you don't have access to the raw data set, run

    python run_all_notebooks.py --data-access=False

and it will only run notebooks that don't require raw data access. 

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/

[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg