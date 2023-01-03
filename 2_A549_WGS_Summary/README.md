This notebook generates the analysis and figure described in Figure 2.

Before running this notebook, you will need to run the [Profile_Aggregation]('../Profile_Aggregation/profile_aggregation.ipynb') notebook which will create the guide and gene-level aggregated profiles used in generating this figure.
Alternatively, you can directly download the files using the following command:
```bash
aws s3 cp --recursive --no-sign-request s3://cellpainting-gallery/cpg-0021-periscope/broad/workspace/profiles/ ../Profile_Aggregation/outputs/ --exclude "*" --include "20200805_A549_WG_Screen_guide_normalized_feature_select_merged_median_ALLBATCHES___CP186___ALLWELLS*"
```

Before running this notebook, you will also need to run the [Hit_Calling]('../Hit_Calling/per_feature_hit_calling.ipynb') notebook which will calculate p-values for each feature.
Alternatively, you can directly download the file using the following command:
```bash
aws s3 cp --no-sign-request s3://cellpainting-gallery/cpg-0021-periscope/broad/workspace/profiles/
```

CORUM data was downloaded from http://mips.helmholtz-muenchen.de/corum/#download using [this link](http://mips.helmholtz-muenchen.de/corum/download/releases/current/humanComplexes.txt.zip). We accessed "Human complexes: A set of all annotated human protein complexes" on 2022/12/15.
It is in the [common_files](common_files) folder and named `CORUM_humanComplexes.txt`.

STRING data was downloaded from https://string-db.org. Data was filtered to human-only and version 11.5 was downloaded with the following links:
[protein links](https://stringdb-static.org/download/protein.links.v11.5/9606.protein.links.v11.5.txt.gz)
[protein data](https://stringdb-static.org/download/protein.info.v11.5/9606.protein.info.v11.5.txt.gz)
To simplify use, we combined the data with the metadata using the following script and saved the combined data in the [common_files](common_files) folder as `STRING_data.csv.gz`.

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