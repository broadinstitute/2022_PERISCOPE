These notebook generates the analysis and figure described in this Supplementary Figure.

## Before running this notebook

Before running this notebook, you will need to download single cell profiles for each of the screens.
Note that these are very large files.

```bash
aws s3 cp --recursive --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/profiles/HeLa/single_cell/ inputs/

aws s3 cp --recursive --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/profiles/A549/single_cell/ inputs/
```

# Outputs

All individual figure panels as generated for the manuscript are output to [outputs/figure_panels](outputs/figure_panels/).

The metadata from single cell profiles are aggregated on a per-plate basis for HeLa and A549 screens. 
Additionally, the per-plate metadata is aggregated per-experiment for HeLa_DMEM, HeLa_HPLM, and A549 screens.
The per-plate aggregated files can be downloaded with the following command:

```bash
aws s3 cp --recursive --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/publication_data/2022_PERISCOPE/ outputs/ --exclude "*" --include "*single_cell_metadata.csv.gz"
```