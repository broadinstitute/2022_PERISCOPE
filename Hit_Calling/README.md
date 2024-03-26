This notebook inputs profiles and generates "hit lists" of genes that show significant perturbation either to their entire profile or features coming from a single channel.

This notebook requires hours to days of computation time for a normal desktop computer on a genome-scale dataset.

## Inputs

To run this notebook you will first need to run [Profile_Aggregation](../Profile_Aggregation) which generates the following profiles that are used as inputs for this notebook:
`20200805_A549_WG_Screen_guide_normalized_feature_select_median_merged_ALLBATCHES___CP186___ALLWELLS.csv.gz`  
`20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___DMEM___ALLWELLS.csv.gz`  
`20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___HPLM___ALLWELLS.csv.gz` 

Alternatively, you can skip Profile Aggregation by directly downloading the profiles with the following command:
```bash
aws s3 cp --recursive --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/profiles/ ../Profile_Aggregation/ --exclude "*" --include "20200805_A549_WG_Screen_guide_normalized_feature_select_median_merged_ALLBATCHES___CP186___ALLWELLS.csv.gz" --include "20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___DMEM___ALLWELLS.csv.gz" --include "20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___HPLM___ALLWELLS.csv.gz"
```

The other file used in generating this data is included in the repository and is as follows:  
`CCLE_expression_A549_HeLa.csv` is granular gene expression data for HeLa and A549 cells, subsetted from `CCLE_expression.csv`, downloaded from the Broad Institute DepMap portal at https://depmap.org/.
This .csv was generated from the `DepMap Public 21Q4` view and downloaded from [this link](https://depmap.org/portal/download/all/?releasename=DepMap+Public+21Q4&filename=CCLE_expression.csv).
Samples were mapped in `CCLE_expression.csv` using `sample_info.csv` downloaded from [this link](https://depmap.org/portal/download/all/?releasename=DepMap+Public+21Q4&filename=sample_info.csv) and the folowing code:  
```python3
HeLa_alias = sample_info.loc[sample_info["stripped_cell_line_name"] == 'HELA', "DepMap_ID"].squeeze()
A549_alias = sample_info.loc[sample_info["stripped_cell_line_name"] == 'A549', "DepMap_ID"].squeeze()
print (f'HeLa alias is {HeLa_alias}.\n A549 alias is {A549_alias}.')
```
`HeLa alias is ACH-001086.`
`A549 alias is ACH-000681.`

CCLE_expression.csv was subsetted to just A549 and HeLa cell data with the following code:
```python3
import pandas as pd
CCLE_expression = pd.read_csv("CCLE_expression.csv")
CCLE_expression = CCLE_expression.loc[
    CCLE_expression[CCLE_expression.columns[0]].isin(['ACH-001086','ACH-000681'])
]
CCLE_expression = CCLE_expression.rename(
    columns={CCLE_expression.columns[0]: "Gene"}).transpose().reset_index()
CCLE_expression.columns = CCLE_expression.iloc[0]
CCLE_expression = CCLE_expression[1:].rename(columns={'ACH-001086':'HeLa','ACH-000681':'A549'})
# Simplify gene names
for i in range(len(CCLE_expression.index)):
    CCLE_expression.iloc[i,0] = CCLE_expression.iloc[i,0].split()[0]
CCLE_expression.to_csv('inputs/CCLE_expression_HeLa_A549.csv', index=False)
```

## Outputs

This notebook generates the following statistical descriptions of the significance of each feature for each gene:  
`HeLa_DMEM_significant_features_mann_whitney_p_values.csv` and `HeLa_DMEM_significant_features_mann_whitney_u_values.csv`  
`HeLa_HPLM_significant_features_mann_whitney_p_values.csv` and `HeLa_HPLM_significant_features_mann_whitney_u_values.csv`  
`A549_significant_features_mann_whitney_p_values.csv` and `A549_significant_features_mann_whitney_u_values.csv`

If you would like to skip running this notebook, you can directly download the outputs with the following command:
```bash
aws s3 cp --recursive --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/publication_data/2022_PERISCOPE outputs/ --exclude "*" --include "*_mann_whitney_*"
```

This notebook also generates a per-cell line summary of the how the CCLE expression data maps to our data that is used as an input to other notebooks.
The .json files are loaded as dictionaries where `zero_express_list` is the list of all unexpressed genes in DepMap data, `all_genes_list` is the list of all genes in our dataset, `zero_tpm_list` is the list of all genes in our dataset that are unexpressed according to DepMap data, and `expressed_gene_list` is a list of all genes in our dataset that are expressed according to DepMap data.
The files are:  
`A549_CCLE_expression_summary.json` and `HeLa_CCLE_expression_summary.json`.

This notebook also generates a histogram of the significant features per gene for each experiment.
The files are:  
`A549_significant_features_histogram.png`  
`HeLa_DMEM_significant_features_histogram.png`  
`HeLa_HPLM_significant_features_histogram.png`  
