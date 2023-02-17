This notebook generates the analysis and figure described in Figure 2.

## Before running this notebook

Before running this notebook, you will need to run the [Profile_Aggregation]('../Profile_Aggregation/profile_aggregation.ipynb') notebook which will create the guide and gene-level aggregated profiles used in generating this figure.
Alternatively, you can directly download the files using the following command:
```bash
aws s3 cp --recursive --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/profiles/A549/ ../Profile_Aggregation/outputs/ --exclude "*" --include "20200805_A549_WG_Screen_guide_normalized_feature_select_merged_median_ALLBATCHES___CP186___ALLWELLS*"
```

Before running this notebook, you will also need to run the [Hit_Calling]('../Hit_Calling/per_feature_hit_calling.ipynb') notebook which will calculate p-values for each feature.
Alternatively, you can directly download the file using the following command:
```bash
aws s3 cp --recursive --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/publication_data/2022_PERISCOPE ../Hit_Calling/outputs/ --exclude "*" --include "*_mann_whitney_*"
```

## Other inputs

CRISPR Gene Effect data was downloaded from DepMap 22Q4 Public files [at this link](https://depmap.org/portal/download/all/?releasename=DepMap+Public+22Q4&filename=CRISPRGeneEffect.csv). 
To simplify use, we filtered the data to `A549` only using the following script and saved it as CRISPRGeneEffect_A549.csv.
See [README.md for Hit Calling](../Hit_Calling/README.md) for description of how to find A549 alias.
```python3
import pandas as pd
gene_effect = pd.read_csv('CRISPRGeneEffect.csv')
# Subset to A549 data
gene_effect = gene_effect.loc[gene_effect[gene_effect.columns[0]]=='ACH-000681',gene_effect.columns[1:]]
# Transpose data and clean labels
gene_effect = gene_effect.T.reset_index().rename(columns={'index':'Gene',404:'Effect'})
for i in range(len(gene_effect.index)):
    gene_effect.iloc[i,0] = gene_effect.iloc[i,0].split()[0]
gene_effect.to_csv('CRISPRGeneEffect_A549.csv',index=False)
```

# Outputs

All individual figure panels as generated for the manuscript are output to [outputs/figure_panels](outputs/figure_panels/).

The number of significant features per channel for whole cell hits and compartment hits are saved to [outputs](outputs) as `A549_plate_level_median_per_feat_sig_genes_5_fdr_compartment_specific_hits.csv` and `A549_plate_level_median_per_feat_sig_genes_5_fdr_whole_cell_hits.csv`.