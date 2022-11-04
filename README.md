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

## Replicating our workflow

All of our data is publicly available so that our entire workflow can be replicated.
However, many of the processing steps require significant computational resources and cannot be replicated on an average personal computer.
To address this, we have provided many intermediate files.
Input images, intermediate processed images, and the final images used for analysis are available as described in [Downloading images](#downloading-images).
Input profiles, intermediate processed profiles, and the final profiles used for analysis are available as described in [Downloading profiles](#downloading-profiles).

Each folder in this repository contains the input files used, logical intermediates generated, and/or a README file describing how to download any that are too large for the repository.

We have described a minimal example you can use, where possible, to practice using our workflow.
However, it is very important to understand that extracting meaningful biology is only possible at scale so any minimal examples are to be used for technical but not biological understanding.

## Downloading data

Cell Painting images and profiles are available at the Cell Painting Gallery on the Registry of Open Data on AWS (https://registry.opendata.aws/cellpainting-gallery/) under accession number `cpg0021-periscope`.
Detailed download and file organization information for the Cell Painting Gallery are available at https://github.com/broadinstitute/cellpainting-gallery.

A549 data is labeled as batch `20200805_A549_WG_Screen` and may also be referred to as `CP186` in some file names.

HeLa data is labeled as batch `20210422_HeLa_WG_Screen` and may also be referred to a `CP257` in some file names.
DMEM and HPLM conditions were separated by plate.
DMEM plates are 'CP257A','CP257B','CP257D','CP257F', and 'CP257H'.
HPLM_plates are 'CP257J','CP257K','CP257L', and 'CP257N'.

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
There is 1 .nd2 file per site with five fluorescent images (DAPI, GFP, A594, Cy5, 750) corresponding to the cell painting images.
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

Image-based profiles were generated using the Pooled Cell Painting [Profiling Template](https://github.com/broadinstitute/pooled-cell-painting-profiling-template) and [Profiling Recipe](https://github.com/broadinstitute/pooled-cell-painting-profiling-recipe).
Configuration for A549 profile generation is found in [this repository](https://github.com/broadinstitute/CP186-A549-WG).
Configuration for HeLa profile generation is found in [this repository](https://github.com/broadinstitute/CP257-HeLa-WG).

Find listed below the filenames for all of the profiles generated.

| Dataset | Aggregate_Method | Aggregate_Level | Aggregate_Group | Normalize | Feature_Select | Second_Aggregate_Method | Second_Aggregate_Level | Second_Normalize | Third_Aggregate_Method | Third_Aggregate_Level | File_Name |
|----|----|----|----|----|----|----|----|----|----|----|----|
| A549 | Median | Gene  | Plate | N | N | N | N | N | N | N | 20200805_A549_WG_Screen_gene_ALLBATCHES___{PLATE}___ALLWELLS.csv.gz |
| A549 | Median | Gene  | Plate | Standardize | N | N | N | N | N | N | 20200805_A549_WG_Screen_gene_normalized_ALLBATCHES___{PLATE}___ALLWELLS.csv.gz |
| A549 | Median | Guide | Plate | N | N | N | N | N | N | N | 20200805_A549_WG_Screen_guide_ALLBATCHES___{PLATE}___ALLWELLS.csv.gz |
| A549 | Median | Guide | Plate | Standardize | N | N | N | N | N | N | 20200805_A549_WG_Screen_guide_normalized_ALLBATCHES___{PLATE}___ALLWELLS.csv.gz |
| A549 | Median | Guide | Plate | Standardize | N | Median | Y | N | N | N | 20200805_A549_WG_Screen_guide_normalized_median_merged_ALLBATCHES_ALLWELLS.csv.gz |
| HeLa | Median | Guide | Plate | N | N | N | N | N | N | N | 20210422_6W_CP257_guide_ALLBATCHES___{PLATE}___ALLWELLS.csv |
| HeLa | Median | Gene  | Plate | N | N | N | N | N | N | N | 20210422_6W_CP257_gene_ALLBATCHES___{PLATE}___ALLWELLS.csv |
| HeLa | Median | Gene  | Plate | Standardize | N | N | N | N | N | N | 20210422_6W_CP257_gene_normalized_ALLBATCHES___{PLATE}___ALLWELLS.csv |
| HeLa | Median | Guide | Plate | Standardize | N | N | N | N | N | N | 20210422_6W_CP257_guide_normalized_ALLBATCHES___{PLATE}___ALLWELLS.csv |
| HeLa | Median | Guide | Plate | Standardize | N | Median | DMEM | N | N | N | 20210422_6W_CP257_guide_normalized_median_merged_ALLBATCHES___DMEM___ALLWELLS.csv |
| HeLa | Median | Guide | Plate | Standardize | N | Median | HPLM | N | N | N | 20210422_6W_CP257_guide_normalized_median_merged_ALLBATCHES___HPLM___ALLWELLS.csv |


Download profiles using the following command
Note that `filehead` is the filename before the first `___`.
```bash
dataset=HeLa
filehead=20200805_A549_WG_Screen_gene_ALLBATCHES
aws s3 cp \
  --no-sign-request \
  s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/profiles/${dataset} . \
  --exclude "*" \
  --include "${filehead}*"
```

#### `single cell profiles`

The HeLa dataset has the additional resource of single cell profiles, available on a per-plate or per-guide basis.

Download per-plate single cell profiles using the following command.
```bash
dataset=HeLa
aws s3 cp \
  --no-sign-request \
  --recursive \
  s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/profiles/${dataset}/single_cell/ . \
```

Download per-guide single cell profiles using the following command.
Note that you can enter a specific guide (e.g. `AAAAAAAACCCACCTTTCCG`) or a gene name (e.g. `HSPA8`) to download data for all four of its guides.
While single cell by-guide profiles are relatively small, download may be slow as the download command has to list the whole folder.
```bash
dataset=HeLa
guide=AAAAAAAACCCACCTTTCCG
aws s3 cp \
  --no-sign-request \
  --recursive \
  s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/profiles/${dataset}/single_cell/ . \
  --exclude "*"
  --include "*${guide}*"
```
