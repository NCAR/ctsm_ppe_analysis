# ctsm_ppe_analysis
Analysis of the Community Terrestrial Systems Model (CTSM) perturbed parameter ensemble (PPE) output.

### Startup tips

1. This repository only works on the NCAR HPC presently
2. You should clone the full repository rather than downloading individual notebooks
3. We provide a python environment that will provide the various packages referenced herein.

### Creating the ppe-py environment on casper

1. log into casper via ssh
2. cd ctsm_ppe_analysis (or wherever you cloned this repo)
3. module load conda
4. conda env create -f environment.yml (this can take 15+ minutes)
5. this only needs to be performed once

### Using the templates

1. log into jupyterhub.hpc.ucar.edu via a web browser
2. see quickstart info: https://www2.cisl.ucar.edu/resources/jupyterhub-ncar
3. click production and then select the Default server
4. we usually select the casper batch queue
5. I typically make the following two edits:

    Specify Memory per Node in GB (-l mem=N)

    14

    Wall Time HH:MM:SS (24-hour max)

    12:00
6. launch server
7. navigate (using the left side panel) to ctsm_ppe_analysis/notebooks and select a notebook
8. select [conda env: miniconda3-ppe-py] as your kernel (top right)
9. now you should be able to run any of the templates cell by cell