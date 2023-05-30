`Common files` are input files generated outside of this workflow and used in multiple notebooks within this workflow.

## Barcodes.csv

`Barcodes.csv` contains sgRNA sequences, gene identifiers, and metadata about guide design for our whole genome library.
The columns within are as described:  
design = an identifier for sub-pool libraries of nontargeting and targeting sgRNAs  
dialout =  primer identifiers for oligo amplification  
gene_id = gene information for each sgRNA  
gene_symbol = gene information for each sgRNA  
oligo = complete oligo sequences required for sgRNA amplification and cloning  
sgRNA = the complete 20-nucleotide sgRNA sequence  
source = the original library source for each sgRNA  

## annotated_gene_sets.json

`annotated_gene_sets.json` is a dictionary of gene group names (e.g. signaling pathways, protein clusters) and the genes within. 
These were manually curated by biologists. 
Most used the Gene Ontology Resource accessed from http://geneontology.org or the Kegg Pathway Database from https://www.genome.jp/kegg/pathway.html as a starting point.
It is used at multiple points for functional classification of groups of genes.

# CORUM_humanComplexes.txt

CORUM data was downloaded from http://mips.helmholtz-muenchen.de/corum/#download using [this link](http://mips.helmholtz-muenchen.de/corum/download/releases/current/humanComplexes.txt.zip). We accessed "Human complexes: A set of all annotated human protein complexes" on 2022/12/15.
It is in the [common_files](common_files) folder and named `CORUM_humanComplexes.txt`.

# STRING_data.csv.gz

STRING data was downloaded from https://string-db.org. Data was filtered to human-only and version 11.5 was downloaded with the following links:
[protein links](https://stringdb-static.org/download/protein.links.v11.5/9606.protein.links.v11.5.txt.gz)
[protein data](https://stringdb-static.org/download/protein.info.v11.5/9606.protein.info.v11.5.txt.gz)
To simplify use, we combined the data with the metadata using the following script and saved the combined data in the [common_files](../common_files) folder as `STRING_data.csv.gz`.

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