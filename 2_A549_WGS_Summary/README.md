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