# Extended Data Figure 9

## Inputs

`Funk_et_al_2022_Supplement-Table_S1.xlsx` and `Funk_et_al_2022_Supplement-Table_S2.xlsx` were downloaded from [doi:10.1016/j.cell.2022.10.017](https://doi.org/10.1016%2Fj.cell.2022.10.017) on 03/27/2024.

To run the full notebook, you will need to download the single-cell data from Funk et al. 2022, available at Harvard Dataverse: <https://doi.org/10.7910/DVN/VYKTI5>.
The single cell data is ~300 GB so we have not included it in our data inputs in this repository.

## Outputs

The `Funk_et_al_2022_data_subsample_aggregated_{n}_cells.csv` outputs are stored in the Cell Painting Gallery instead of in this Github repository.
The following command will download the files:
"""bash
aws s3 cp s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/publication_data/2022_PERISCOPE/ outputs/ --recursive --exclude "*" --include "Funk_et_al_2022_subsample_aggregated" --no-sign-request
"""
