This notebook generates the analysis and figure described in Figure 3.

This notebook requires ~30 minutes computation time for a normal desktop computer on a genome-scale dataset.

## Before running this notebook

To run this notebook you will first need to run [Profile_Aggregation](../Profile_Aggregation) which generates the following profiles that are used as inputs for this notebook:
`20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___DMEM___ALLWELLS_gene_aggregated.csv.gz`  
`20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___HPLM___ALLWELLS_gene_aggregated.csv.gz` 

Alternatively, you can skip Profile Aggregation by directly downloading the profiles with the following command:
```bash
aws s3 cp --recursive --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/profiles/HeLa/ ../Profile_Aggregation/outputs/ --exclude "*" --include "20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___DMEM___ALLWELLS_gene_aggregated.csv.gz" --include "20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___HPLM___ALLWELLS_gene_aggregated.csv.gz"
```

To run this notebook you will also first need to run [Hit_Calling](../Hit_Calling) which generates the following statistical descriptions of the significance of each feature for each gene:  
`HeLa_DMEM_significant_features_mann_whitney_p_values.csv`
`HeLa_HPLM_significant_features_mann_whitney_p_values.csv`

If you would like to skip running Hit Calling, you can directly download the outputs with the following command:
```bash
aws s3 cp --recursive --no-sign-request s3://cellpainting-gallery/cpg0021-periscope/broad/workspace/publication_data/2022_PERISCOPE ../Hit_Calling/outputs/ --exclude "*" --include "*_mann_whitney_*"
```

## Other inputs

CORUM data was downloaded from http://mips.helmholtz-muenchen.de/corum/#download using [this link](http://mips.helmholtz-muenchen.de/corum/download/releases/current/humanComplexes.txt.zip). We accessed "Human complexes: A set of all annotated human protein complexes" on 2022/12/15.
It is in the [inputs](inputs) folder and named `CORUM_humanComplexes.txt`.

STRING data was downloaded from https://string-db.org. Data was filtered to human-only and version 11.5 was downloaded with the following links:
[protein links](https://stringdb-static.org/download/protein.links.v11.5/9606.protein.links.v11.5.txt.gz)
[protein data](https://stringdb-static.org/download/protein.info.v11.5/9606.protein.info.v11.5.txt.gz)
To simplify use, we combined the data with the metadata using the following script and saved the combined data as `STRING_data.csv`.

```python3
import pandas as pd
ppi_data = pd.read_csv('9606.protein.links.v11.5.txt.gz',sep = ' ')
p_names = pd.read_csv('9606.protein.info.v11.5.txt.gz',sep = '\t')

p_names_dic = {p_names.iloc[i]['#string_protein_id']:p_names.iloc[i]['preferred_name'] for i in range(len(p_names))}

p1 = list(ppi_data.protein1)
p2 = list(ppi_data.protein2)
score = list(ppi_data.combined_score)

p1_named = [p_names_dic.get(item)  for item in p1]
p2_named = [p_names_dic.get(item)  for item in p2]

ppi_data_name = pd.DataFrame(list(zip(p1_named, p2_named, score)),
               columns =['protein1', 'protein2','combined_score'])
ppi_data_name.to_csv('STRING_data.csv.gz',index=False)
```