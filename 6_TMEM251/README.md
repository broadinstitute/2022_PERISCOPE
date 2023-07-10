This notebook generates some of the analysis described in Figure 7.

Before running this notebook, you will need to run the [Profile_Aggregation](Profile_Aggregation) notebook which will create the gene-level aggregated profiles used in generating this figure. Alternatively, you can directly download the file using the following commands:

```bash
aws s3 cp --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/profiles/HeLa/20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___DMEM___ALLWELLS_gene_aggregated.csv.gz ../Profile_Aggregation/outputs/HeLa/20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___DMEM___ALLWELLS_gene_aggregated.csv.gz
```