This notebook generates the analysis and figure described in Figure 4.

Before running this notebook, you will need to run the [Profile_Aggregation]('../Profile_Aggregation/profile_aggregation.ipynb') notebook which will create the gene-level aggregated profiles used in generating this figure.
Alternatively, you can directly download the files using the following commands:
```bash
aws s3 cp --no-sign-request s3://cellpainting-gallery/cpg-0021-periscope/broad/workspace/profiles/'20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___HPLM___ALLWELLS_gene_aggregated.csv.gz' ../Profile_Aggregation/outputs/'20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___HPLM___ALLWELLS_gene_aggregated.csv.gz'

aws s3 cp --no-sign-request s3://cellpainting-gallery/cpg-0021-periscope/broad/workspace/profiles/'20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___DMEM___ALLWELLS_gene_aggregated.csv.gz' ../Profile_Aggregation/outputs/'20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___DMEM___ALLWELLS_gene_aggregated.csv.gz'
```