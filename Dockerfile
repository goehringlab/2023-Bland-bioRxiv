# Set up conda
FROM continuumio/miniconda3
RUN conda update -n base conda

# Install fast solver
RUN conda install -n base conda-libmamba-solver
RUN conda config --set solver libmamba

# Copy environment.yml
COPY environment.yml /tmp/environment.yml

# Copy code
RUN git clone --depth 1 https://github.com/tsmbland/Bland-et-al-2023.git

# Create environment
RUN conda env create -f /tmp/environment.yml

# Activate environment
RUN echo "source activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH