# 2022_PERISCOPE
This repository contains supporting analyses and files for LEAD_AUTHOR et al. "PAPER TITLE".
It also includes download information for the images and profiles used in the analysis.

## Abstract

ABSTRACT_TEXT

## Computational environment

### Python

We use [conda](https://docs.conda.io/en/latest/) to manage the computational environment.
To install conda see [instructions](https://docs.conda.io/en/latest/miniconda.html).

After installing conda, execute the following to install and navigate to the environment:

```bash
# Install the conda environment
conda env create --force --file environment.yml

# Activate the environment
conda activate periscope_2022
```

## Downloading data

Cell Painting images and profiles are available at the Cell Painting Gallery on the Registry of Open Data on AWS (https://registry.opendata.aws/cellpainting-gallery/) under accession number `cpg0021-periscope`. 
Detailed download and file organization information for the Cell Painting Gallery are available at https://github.com/broadinstitute/cellpainting-gallery.

A549 data is labeled as batch `20200805_A549_WG_Screen`.
HeLa data is labeled as batch `20210422_HeLa_WG_Screen`.

### Downloading images

The image metadata will be automatically extracted from the images using the pipelines provided at https://github.com/broadinstitute/pooled-cell-painting-image-processing.
An orientation to the images is as follows:

#### `images`
`images` contains the raw images as they come off the microscope.
The images can be downloaded using the command

```bash
batch=20200805_A549_WG_Screen
plate=CP186A
session=20X_CP_CP186A
aws s3 cp \
  --no-sign-request \
  --recursive \
  s3://cellpainting-gallery/cpg0021-periscope/broad/images/${batch}/images/${plate}/${session} .
```

##### Cell Painting
Within each plate folder, Cell Painting images are organized into a single folder labeled 20X_CP_${plate}.
Each 6-well plate contains images from 1364 (for A549 screen) or 1332 (for HeLa screen) sites for each well.
There is 1 .nd2 file per site with five fluorescent images (DAPI, GFP, A594, Cy5, 750) corresonding to the cell painting images.
Sites have a 10% overlap.

##### Barcoding
Within each plate folder, barcoding images are organized into a folder per cycle for each of 12 cycles labeled 10X_c#-SBS-# where # is the cycle number.
Each 6-well plate contains images from 320 (for A549 screen) or 316 (for HeLa screen) sites for each well.
There is 1 .nd2 file per site with five fluorescent images (DAPI, Cy3, A594, Cy5, Cy7) corresponding to DNA and the four nucleotides read in SBS.
Sites have a 10% overlap.

#### `illum`
`illum` contains whole plate illumination correction images.
The images can be downloaded using the command

```bash
batch=20200805_A549_WG_Screen
plate=CP186A
aws s3 cp \
  --no-sign-request \
  --recursive \
  s3://cellpainting-gallery/cpg0021-periscope/broad/images/${batch}/illum/${plate} .
```

#### `images_aligned`
`images_aligned` contains the whole-plate illumination corrected Barcoding images where channels are aligned within cycles.
Within the `images_corrected` folder, images are nested by arm (`barcoding`) and are saved in folders by plate-well.
The images can be downloaded using the command

```bash
batch=20200805_A549_WG_Screen
plate=CP186A
aws s3 cp \
  --no-sign-request \
  --recursive \
  s3://cellpainting-gallery/cpg0021-periscope/broad/images/${batch}/images_aligned/barcoding/ . \
  --exclude "*" \
  --include "${plate}*"
```

#### `images_corrected`
`images_corrected` contains the whole-plate illumination corrected Cell Painting images and the aligned Barcoding images that have undergone channel compensation and background removal.
Within the `images_corrected` folder, images are nested by arm (`barcoding` vs. `painting`) and are saved in folders by plate-well-site.
The images can be downloaded using the command

```bash
batch=20200805_A549_WG_Screen
plate=CP186A
aws s3 cp \
  --no-sign-request \
  --recursive \
  s3://cellpainting-gallery/cpg0021-periscope/broad/images/${batch}/images_corrected/ . \
  --exclude "*" \
  --include "*${plate}*"
```


#### `images_corrected_cropped`
`images_corrected_cropped` contains stitched and cropped pseudo-site images where the pseudo-site corresponds between Cell Painting and Barcoding images. 
These are the images used in the final analysis pipeline.
Within the `images_corrected` folder, images are saved in folders by plate_well.
The images can be downloaded using the command

```bash
batch=20200805_A549_WG_Screen
plate=CP186A
aws s3 cp \
  --no-sign-request \
  --recursive \
  s3://cellpainting-gallery/cpg0021-periscope/broad/images/${batch}/images_corrected_cropped/ . \
  --exclude "*" \
  --include "${plate}*"
```


### Downloading profiles

TO BE FILLED IN