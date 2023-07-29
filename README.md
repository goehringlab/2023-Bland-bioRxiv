## Optimized dimerization of the PAR-2 RING domain drives cooperative and selective membrane recruitment for robust feedback-driven cell polarization 

[![CC BY 4.0][cc-by-shield]][cc-by]

Complete analysis code for the paper `"Optimized dimerization of the PAR-2 RING domain drives cooperative and selective membrane recruitment for robust feedback-driven cell polarization" (Bland et al., 2023)`


## Code structure

Notebooks used to perform the analysis in the paper and generate most of the figure panels are found in _scripts_.
This is split into two sections:

- __Run__: notebooks used to perform quantification on raw images, and save results in the _data_ folder (e.g. _ph_quantify.ipynb_ outputs the data file _ph_quantification.csv_). Running these scripts requires access to the raw data repository (i.e. image files, see below). 
- __Analysis__: notebooks used to perform downstream analysis on the quantification results from above and generate figure panels (which are saved in a series of '_Figs_' folders). Most figures can be created without access to the raw data repository, but some do require access to raw data (e.g. panels displaying specific images). Also includes SEC-MALS analysis and modelling.

Notebooks for creating specific figure panels:

[a5302]: scripts/Analysis/6HNL/6HNL.ipynb
[a1912]: scripts/Analysis/DimerModelFitting/02_AllFits.ipynb
[a5698]: scripts/Analysis/DimerModelFitting/00_ProcessData.ipynb
[a6801]: scripts/Analysis/DimerModelFitting/01_Figures.ipynb
[a5093]: scripts/Analysis/DimerModelSolving/SolveModel.ipynb
[a6684]: scripts/Analysis/GCN4/Fragment.ipynb
[a5514]: scripts/Analysis/GCN4/Par3Mut.ipynb
[a1834]: scripts/Analysis/GCN4/Par2GCN4.ipynb
[a9246]: scripts/Analysis/GCN4/PRBH.ipynb
[a9263]: scripts/Analysis/meiosis/Figures.ipynb
[a9397]: scripts/Analysis/Mlc4/SAIBR.ipynb
[a4186]: scripts/Analysis/Mlc4/Quantification.ipynb
[a5886]: scripts/Analysis/ModelNonlinearity/Figs.ipynb
[a3255]: scripts/Analysis/Nop1/Lethality.ipynb
[a3572]: scripts/Analysis/Nop1/2cellAsymmetry.ipynb
[a9147]: scripts/Analysis/optogenetics/Optogenetics.ipynb
[a0226]: scripts/Analysis/PhRundown/FigsLogTransformed.ipynb
[a1487]: scripts/Analysis/PolarisedVsUniform/Figures.ipynb
[a2111]: scripts/Analysis/QuantificationCalibrationComparison/Figures.ipynb
[a6427]: scripts/Analysis/QuantificationMethod/MethodComparison.ipynb
[a4447]: scripts/Analysis/QuantificationMethod/SchematicMembraneProfile.ipynb
[a8752]: scripts/Analysis/QuantificationMethod/Schematic.ipynb
[a4134]: scripts/Analysis/QuantificationSummaryTable/ResultsTable.ipynb
[a7601]: scripts/Analysis/RingCombinedMutants/Figures.ipynb
[a3603]: scripts/Analysis/RingFragment/Figures.ipynb
[a5616]: scripts/Analysis/RingPh/Figures.ipynb
[a6085]: scripts/Analysis/RundownsRegression/PlotLinearScale.ipynb
[a3476]: scripts/Analysis/RundownsRegression/Schematic.ipynb
[a8492]: scripts/Analysis/RundownsRegression/FittingLogTransformed.ipynb
[a5498]: scripts/Analysis/SecMals/TitrationCurves.ipynb
[a9706]: scripts/Analysis/SecMals/Traces.ipynb
[a5004]: scripts/Analysis/SecMals/XmlExtract.ipynb
[a6824]: scripts/Analysis/ThreeCompartmentModel/Kinetic.ipynb
[a1883]: scripts/Analysis/ThreeCompartmentModel/Prefactor.ipynb
[a8987]: scripts/Analysis/ThreeCompartmentModel/Equilibrium.ipynb


Figure 1: [D-E][a1487], [F][a0226], [G][a8492]\
Figure 2: [A][a3603], [B][a5616], [F-G][a9706], [H][a5498], [I][a1487], [J][a8492], [K][a3572], [L][a3255]\
Figure 3: [B-D][a5886], [F][a6801]\
Figure 4: [A-B][a1834], [C][a6684], [D][a9397], [E][a4186]\
Figure 5: [A][a8987], [C-D][a6824], [E-F][a5514], [G-H][a9246]\
Figure S1: [A][a8752], [C-D][a2111], [F][a6427], [G][a9147]\
Figure S2: [A-H][a8492]\
Figure S4: [B][a7601]\
Figure S6: [B-F][a6801]\
Figure S7: [A-B][a5302]\
Figure S8: [B-D][a9263]\
Figure S9: [A-D][a6824]\
[Table S2][a4134]\
[Table S4][a1912]

Core code is found in _src_. Also relies heavily on the [par-segmentation](https://github.com/tsmbland/par-segmentation) and [discco](https://github.com/tsmbland/discco) packages.

## Data availability

The entire dataset will be made publicly available. 

The vast majority of the data is image data, found in the __Imaging__ folder. This is organised into a series of folders representing different experiments, and subfolders representing experimental conditions (worm strain, date, RNAi, acquisition settings). Data for individual embryos are further separated into folders. Within each embryo folder you will find:
- Raw images (one for each channel including DIC)
- An autofluorescence-corrected image (_af_corrected.tif_), generated from the raw images using [SAIBR](https://github.com/goehringlab/saibr_python)
- A preliminary manual ROI (_ROI_manual.txt_)
- An optimised ROI (_ROI_fit.txt_) generated using the [par-segmentation](https://github.com/tsmbland/par-segmentation) package
- An nd file containing metadata

Also includes the following datasets:
- __AlphaFold__: a PDB file for the PAR-2 RING domain dimer
- __Sequence alignments__: FASTA and Jalview files for the RING domain sequence alignments
- __SEC MALS__: Raw SEC-MALS data for the PAR-2 RING domain

If you decide to download the raw data, you must specify _raw_data_path_ in _src/helpers.py_

## Installation

To install on your local machine, run the following:

&#8291;1. Clone the repository:

    git clone --depth 1 https://github.com/tsmbland/Bland-et-al-2023.git
    cd Bland-et-al-2023

&#8291;2. Create conda environment:

    conda env create -f environment.yml

&#8291;3. Activate conda environment:

    conda activate par2_paper

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/

[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg