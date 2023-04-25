"""
@author: mhaghigh
"""
import pandas as pd
import numpy as np

################################################################################
def handle_nans(
    df_input, cp_features, thrsh_null_ratio=0.05, thrsh_std=0.0001, fill_na_method=None
):
    """
    from the all df_input columns extract cell painting measurments
    the measurments that should be used for analysis

    Inputs:
    df_input: dataframes with all the annotations available in the raw data
    fill_na_method: 'interpolate' or 'median' or None
                    interpolate makes sense for single cell data of arrayed experiment since it fills NA values
                    to the nearest cell values
    Outputs: cp_features, cp_features_analysis

    """

    print("cp_features:", len(cp_features))
    object_type_columns = df_input[cp_features].select_dtypes([object]).columns
    df_input[object_type_columns] = df_input[object_type_columns].apply(
        pd.to_numeric, errors="coerce"
    )


    cols2remove_manyNulls = [
        i
        for i in cp_features
        if (df_input[i].isnull().sum(axis=0) / df_input.shape[0]) > thrsh_null_ratio
    ]
    cols2remove_lowVars = (
        df_input[cp_features]
        .std()[df_input[cp_features].std() < thrsh_std]
        .index.tolist()
    )

    cols2removeCP = cols2remove_manyNulls + cols2remove_lowVars
#     print("cols2remove_manyNulls", cols2remove_manyNulls)

#     print("cols2remove_lowVars", cols2remove_lowVars)

    cp_features_analysis = list(set(cp_features) - set(cols2removeCP))
    print(
        "len cp_features_analysis/nan cols/low vars:",
        len(cp_features_analysis),
        len(cols2remove_manyNulls),
        len(cols2remove_lowVars),
    )


    df_p_s = df_input.drop(cols2removeCP, axis=1)

    if fill_na_method == "median":
        df_p_s.loc[:, cp_features_analysis] = df_p_s.loc[
            :, cp_features_analysis
        ].fillna(df_p_s[cp_features_analysis].median())
    elif fill_na_method == "interpolate":
        df_p_s.loc[:, cp_features_analysis] = df_p_s.loc[
            :, cp_features_analysis
        ].interpolate()
    elif fill_na_method == "drop-rows":
        print("before dropping nan rows: ", df_p_s.shape)
        #         print('1',df_p_s.shape,df_p_s.dropna(subset=cp_features_analysis).reset_index(drop=True).shape)
        df_p_s = df_p_s.dropna(subset=cp_features_analysis).reset_index(drop=True)
        print("after dropping nan rows: ", df_p_s.shape)

    elif (
        fill_na_method == "interpolate_sim_col"
    ):  # interpolate based on the columns with highest correlation
        print("Not implemented yet! Nothing got dropped! ")


    return df_p_s, cp_features_analysis