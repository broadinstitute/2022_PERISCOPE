This notebook inputs profiles and generates "hit lists" of genes that show significant perturbation either to their entire profile or features coming from a single channel.

To run the notebooks you will need to download the following files to the `inputs_data` folder.
These are the profiles used to generate the "hit lists".  
`20200805_A549_WG_Screen_guide_normalized_feature_select_median_merged_ALLBATCHES___CP186___ALLWELLS.csv.gz`  
`20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___DMEM___ALLWELLS.csv.gz`  
`20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___HPLM___ALLWELLS.csv.gz` 

The following command will download these files:
```bash
aws s3 sync --no-sign-request s3://cellpainting-gallery/cpg-0021-periscope/broad/workspace/profiles/ inputs_data --exclude "*" --include "20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___*" --include "20200805_A549_WG_Screen_guide_normalized_feature_select_median_merged_ALLBATCHES___*"
```

Other files used in generating this data are included in the repository and are as follows:
`CCLE_expression_HeLa.csv` is granular gene expression data for HeLa cells.  
`CCLE_expression_A549.csv` is granular gene expression data for A549 cells. 
The granular expression data is filtered from CCLE_expression.csv, downloaded from the Broad Institute DepMap portal at https://depmap.org/.
These .csvs were generated from the `DepMap Public 22Q2` view.