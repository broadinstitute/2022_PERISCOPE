"""
@author: mhaghigh
"""
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans
from . import extract_cpfeature_names
from . import handle_nans

################################################################################


def extract_single_cell_samples(df_p_s, n_cells, cell_selection_method):
    """
    This function select cells based on input cell_selection_method

    Inputs:
    ++ df_p_s   (pandas df) size --> (number of single cells)x(columns):
    input dataframe contains single cells profiles as rows

    ++ n_cells (dtype: int): number of cells to extract from the input dataframe

    ++ cell_selection_method (str):
        - 'random' - generate n randomly selected cells
        - 'representative' - clusters the data and sample from the "closest to mean cluster"

    Returns:
    dff (pandas df): sampled input dataframe

    """

    (
        cp_features,
        cp_features_analysis_0,
    ) = extract_cpfeature_names.extract_cpfeature_names(df_p_s)
    df_p_s, cp_features_analysis = handle_nans.handle_nans(
        df_p_s, cp_features_analysis_0
    )

    #     print("heloo")
    #     print(cp_features)
    if cell_selection_method == "random":
        dff = (
            df_p_s.reset_index(drop=True)
            .sample(n=n_cells, replace=False)
            .reset_index(drop=True)
        )

    elif cell_selection_method == "representative":
        df_p_s[cp_features_analysis] = df_p_s[cp_features_analysis].interpolate()
        if df_p_s.shape[0] > 60:
            n_cells_in_each_cluster_unif = 30
        else:
            n_cells_in_each_cluster_unif = int(df_p_s.shape[0] / 5)

        n_clusts = int(df_p_s.shape[0] / n_cells_in_each_cluster_unif)
        kmeans = KMeans(n_clusters=n_clusts).fit(
            np.nan_to_num(df_p_s[cp_features_analysis].values)
        )
        clusterLabels = kmeans.labels_
        df_p_s["clusterLabels"] = clusterLabels
        mean_clus = kmeans.predict(
            df_p_s[cp_features_analysis]
            .mean()
            .values[
                np.newaxis,
            ]
        )
        df_ps = df_p_s[df_p_s["clusterLabels"] == mean_clus[0]]
        dff = (
            df_ps.reset_index(drop=True)
            .sample(n=np.min([n_cells, df_ps.shape[0]]), replace=False)
            .reset_index(drop=True)
        )


    return dff, cp_features_analysis
