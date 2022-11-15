import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from functools import reduce
from scipy.spatial import distance

from pycytominer import normalize, feature_select ,aggregate,consensus

from pycytominer.cyto_utils import output,infer_cp_features

from pycytominer.cyto_utils.util import (
    get_pairwise_correlation,
    check_correlation_method,
    infer_cp_features,
)

# load normalized plate_level profiles and merge 
dmem_plates = ['CP257A','CP257B','CP257D','CP257F','CP257H']
hplm_plates = ['CP257J','CP257K','CP257L','CP257N']

dmem_list = []

for plate in dmem_plates:
    filename = f'20210422_6W_CP257_guide_normalized_ALLBATCHES___{plate}___ALLWELLS.csv.gz'
    pre_dmem_df = pd.read_csv(filename)
    dmem_list.append(pre_dmem_df)

dmem_profile_df = pd.concat(dmem_list)


# perform feature selection on merged profiles
dmem_feature_selected_df = feature_select(
            profiles=dmem_profile_df,
            features='infer',
            samples='all',
            operation=['variance_threshold','correlation_threshold','drop_na_columns','blocklist'],
            na_cutoff= 0,
            corr_threshold=0.9
        )

dmem_feature_selected_df.to_csv('20210422_6W_CP257_guide_normalized_feature_select_merged_ALLBATCHES___DMEM___ALLWELLS.csv.gz')

# perform median aggregation on profiles
dmem_median_df= aggregate(
                    population_df=dmem_feature_selected_df, 
                    strata=['Metadata_Foci_Barcode_MatchedTo_GeneCode' ,'Metadata_Foci_Barcode_MatchedTo_Barcode'], 
                    features='infer', 
                    operation='median' 
                    )

dmem_median_df.to_csv('20210422_6W_CP257_guide_normalized_feature_select_median_merged_ALLBATCHES___DMEM___ALLWELLS.csv.gz',index = False)