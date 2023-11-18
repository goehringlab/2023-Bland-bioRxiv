# Set up conda
FROM continuumio/miniconda3
RUN conda update -n base conda

# Install mamba solver
RUN conda install -n base conda-libmamba-solver
RUN conda config --set solver libmamba

# Copy environment.yml
COPY environment.yml ./

# Create environment
RUN conda env create -f environment.yml

# Activate environment
RUN echo "source activate $(head -1 environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 environment.yml | cut -d' ' -f2)/bin:$PATH

# Copy code and data
COPY data scripts src LICENSE README.md ./
