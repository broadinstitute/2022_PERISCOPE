These notebook generates the analysis and figure described in this Supplementary Figure.

## Before running this notebook

Before running this notebook, you will need run Supplemental_6. 
Alternatively, you can download the necessary per-plate aggregated files with the following command:

```bash
aws s3 cp --recursive --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/publication_data/2022_PERISCOPE/ ../Supplemental_6/outputs/ --exclude "*" --include "*single_cell_metadata.csv.gz"
```

Additionally, you will need to run [Profile_Aggregation](../Profile_Aggregation/), [Hit_Calling](../Hit_Calling/), [A549 Summary](../2_A549_WGS_Summary/), and [HeLa Summary](../3_HELA_WGS_Summary/).