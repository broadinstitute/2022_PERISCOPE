### Calculation of guide level profiles from the A549 plate level profiles for the PERISCOPE manuscript. ###
### Script by Meraj Ramezani(mramezan@broadinstitute.org) ###
# Import relevant librariesimport pandas as pd
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
plates = ['CP186A','CP186B','CP186C','CP186D','CP186E','CP186F','CP186G','CP186H','CP186N']


df_list = []

for plate in plates:
    filename = f'20200805_A549_WG_Screen_guide_normalized_ALLBATCHES___{plate}___ALLWELLS.csv.gz'
    pre_df = pd.read_csv(filename)
    df_list.append(pre_df)

profiles_df = pd.concat(df_list)

# perform feature selection on merged profiles
feature_selected_df = feature_select(
            profiles=profiles_df,
            features='infer',
            samples='all',
            operation=['variance_threshold','correlation_threshold','drop_na_columns','blocklist'],
            na_cutoff= 0,
            corr_threshold=0.9
        )

feature_selected_df.to_csv('20200805_A549_WG_Screen_guide_normalized_feature_select_merged_ALLBATCHES___CP186___ALLWELLS.csv.gz', index=False)

# perform median aggregation on profiles
median_df = aggregate(
                    population_df = feature_selected_df, 
                    strata=['Metadata_Foci_Barcode_MatchedTo_GeneCode' ,'Metadata_Foci_Barcode_MatchedTo_Barcode'], 
                    features='infer', 
                    operation='median' 
                    )

median_df.to_csv('20200805_A549_WG_Screen_guide_normalized_feature_select_merged_median_ALLBATCHES___CP186___ALLWELLS.csv.gz',index = False)