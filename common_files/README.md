`Common files` are input files generated outside of this workflow and used in multiple notebooks within this workflow.

`Barcodes.csv` is 
The columns within are as described:
design,
dialout,
gene_id,
gene_symbol,
oligo,
sgRNA,
source,
spots_per_oligo,
subpool

`annotated_gene_sets.json` is a dictionary of gene group names (e.g. signaling pathways, protein clusters) and the genes within. 
These were manually curated by biologists. 
Most used the Gene Ontology Resource accessed from http://geneontology.org or the Kegg Pathway Database from https://www.genome.jp/kegg/pathway.html as a starting point.
It is used at multiple points for functional classification of groups of genes.