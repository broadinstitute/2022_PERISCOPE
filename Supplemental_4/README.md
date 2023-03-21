This notebook generates the analysis and figure described in Figure 2.

## Before running this notebook

Before running this notebook, you will need to run the [Hit_Calling]('../Hit_Calling/per_feature_hit_calling.ipynb') notebook which will calculate p-values for each feature.
Alternatively, you can directly download the files using the following command:

```bash
aws s3 cp --recursive --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/publication_data/2022_PERISCOPE ../Hit_Calling/outputs/ --exclude "*" --include "*_mann_whitney_*"
```

## Other inputs

HeLa genetic dependencies estimated using the DEMETER2 model were downloaded [at this link](https://figshare.com/ndownloader/files/13515395), Version 6, 2020-04-09 release and saved as `D2_combined_gene_dep_scores.csv`.
To simplify use, we filtered the data to `HeLa` only using the following script and saved it as `D2_combined_gene_dep_scores_HeLa.csv`.
```python3
import pandas as pd
HeLa_gene_effect = pd.read_csv(os.path.join('/Users/eweisbar/Downloads/','D2_combined_gene_dep_scores.csv')).set_index('Unnamed: 0')
HeLa_gene_effect = HeLa_gene_effect['HELA_CERVIX'].to_frame().reset_index().rename(columns={'Unnamed: 0':'Gene','HELA_CERVIX':'Effect'})
HeLa_gene_effect[['Gene','extra']] = HeLa_gene_effect.Gene.str.split(' ', expand = True)
HeLa_gene_effect = HeLa_gene_effect[['Gene','Effect']]
HeLa_gene_effect.to_csv('D2_combined_gene_dep_scores_HeLa.csv',index=False)
```

# Outputs

All individual figure panels as generated for the manuscript are output to [outputs/figure_panels](outputs/figure_panels/).
