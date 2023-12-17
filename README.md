## Optimized dimerization of the PAR-2 RING domain drives cooperative and selective membrane recruitment for robust feedback-driven cell polarization 

[![CC BY 4.0][cc-by-shield]][cc-by]
[![run with docker](https://img.shields.io/badge/run%20with-docker-0db7ed?logo=docker)](https://www.docker.com/)

Complete analysis code for the paper `"Optimized dimerization of the PAR-2 RING domain drives cooperative and selective membrane recruitment for robust feedback-driven cell polarization" (Bland et al., 2023)` [BioRxiv link](https://www.biorxiv.org/content/10.1101/2023.08.10.552581v1)


## Code structure

Notebooks used to perform the analysis in the paper and generate most of the figure panels are found in `scripts`.
This is split into two sections:

- __`Run`__: notebooks used to perform quantification on raw images, and save results in the `data` folder (e.g. `ph_quantify.ipynb` outputs the data file `ph_quantification.csv`). Running these scripts requires access to the raw data repository (i.e. image files, see below). 
- __`Analysis`__: notebooks used to perform downstream analysis on the quantification results from above and generate figure panels (which are saved in a series of `Figs` folders). Most figures can be created without access to the raw data repository, but some do require access to raw data (e.g. panels displaying specific images). Also includes SEC-MALS analysis and modelling.

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
Figure EV1: [A-D][a8492], [E][a4134]\
Figure EV3: [B-C][a5302]\
Figure EV4: [B-D][a9263]\
Figure EV5: [A][a8752], [C-D][a2111], [F][a6427], [G][a9147]\
Figure S1: [D][a7601]\
Figure S2: [B-F][a6801], [G][a1912]\
Figure S3: [A-D][a6824]

Core code is found in `src`. Also relies heavily on the [par-segmentation](https://github.com/goehringlab/par-segmentation) and [discco](https://github.com/tsmbland/discco) packages.

## Data availability

The entire dataset will be made publicly available (~7.5 GB). 

The vast majority of the data is image data, found in the __`Imaging`__ folder. This is organised into a series of folders representing different experiments, and subfolders representing experimental conditions (worm strain, date, RNAi, acquisition settings). Data for individual embryos are further separated into folders. Within each embryo folder you will find:
- Raw images (one for each channel including DIC)
- An autofluorescence-corrected image (`af_corrected.tif`), generated from the raw images using [SAIBR](https://github.com/goehringlab/saibr_fiji_plugin)
- A preliminary manual ROI (`ROI_manual.txt`) generated using the [matplotlib-polyroi](https://github.com/tsmbland/matplotlib-polyroi) package
- An optimised ROI (`ROI_fit.txt`) generated using the [par-segmentation](https://github.com/goehringlab/par-segmentation) package
- An `nd` file containing metadata

Also includes the following datasets:
- __`AlphaFold`__: a PDB file for the PAR-2 RING domain dimer
- __`Sequence alignments`__: FASTA and Jalview files for the RING domain sequence alignments
- __`SEC MALS`__: Raw SEC-MALS data for the PAR-2 RING domain


## Installation

Package requirements are listed in `requirements.txt`

To ensure reproducibility, it is best to run the project in a Docker container. To do this, perform the following steps:

&#8291;1. Make sure [Docker](https://www.docker.com/products/docker-desktop/) is installed and open on your machine 

&#8291;2. Download/clone the code and navigate to the project directory

&#8291;3. Build the Docker container

    docker-compose build

&#8291;4. Once the build has completed, run the docker container

    docker-compose run -p 8888:8888 app

&#8291;5. Open Jupyter

    jupyter notebook --ip 0.0.0.0 --no-browser --allow-root

This will print a couple of URLs at the bottom of your terminal. Copy and paste the second of these into your browser to open up Jupyter.

NOTE: If you're using the raw data, you must either place it inside the project directory as a folder named `raw_data`, or change the path in `docker-compose.yaml` where indicated. Otherwise, you should delete this line.

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/

[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
