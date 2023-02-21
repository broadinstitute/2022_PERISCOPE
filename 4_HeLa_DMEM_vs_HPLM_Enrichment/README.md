This notebook generates the analysis and figure described in Figure 4.

Before running this notebook, you will need to run the [Profile_Aggregation]('../Profile_Aggregation/profile_aggregation.ipynb') notebook which will create the gene-level aggregated profiles used in generating this figure.
Alternatively, you can directly download the files using the following commands:
```bash
aws s3 cp --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/profiles/'20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___HPLM___ALLWELLS_gene_aggregated.csv.gz' ../Profile_Aggregation/outputs/'20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___HPLM___ALLWELLS_gene_aggregated.csv.gz'

aws s3 cp --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/profiles/'20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___DMEM___ALLWELLS_gene_aggregated.csv.gz' ../Profile_Aggregation/outputs/'20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___DMEM___ALLWELLS_gene_aggregated.csv.gz'
```

To run this notebook you will also first need to run [Hit_Calling](../Hit_Calling) which generates the following statistical descriptions of the significance of each feature for each gene:  
`HeLa_DMEM_significant_features_mann_whitney_p_values.csv`
`HeLa_HPLM_significant_features_mann_whitney_p_values.csv`

If you would like to skip running Hit Calling, you can directly download the outputs with the following command:
```bash
aws s3 cp --recursive --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/XXXXXXX ../outputs/ --exclude "*" --include "*_mann_whitney_*"
```

The other file used in generating this data is included in the repository and is `CCLE_expression_A549_HeLa.csv`. Details of this file are explained in the [README.md for Hit Calling](../Hit_Calling/README.md).