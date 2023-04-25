"""
@author: mhaghigh
"""
import pickle
import pandas as pd

################################################################################


def extract_cpfeature_names(df_input):
    """
    from the all df_input columns extract cell painting measurments
    the measurments that should be used for analysis

    Inputs:
    df_input: dataframes with all the annotations available in the raw data

    Outputs: cp_features, cp_features_analysis

    """

    cp_features = df_input.columns[
        df_input.columns.str.contains("Cells_|Cytoplasm_|Nuclei_")
    ].tolist()
    locFeature2beremoved = list(
        filter(lambda x: "_X" in x or "_Y" in x or "_x" in x or "_y" in x, cp_features)
    )
    metadataFeature2beremoved = list(filter(lambda x: "etadata" in x, cp_features))

    blackListFeatures = df_input.columns[
        df_input.columns.str.contains(
            "Nuclei_Correlation_Manders_"
            "|Nuclei_Correlation_RWC_|Nuclei_Granularity_14_|Nuclei_Granularity_15_|Nuclei_Granularity_16_"
        )
    ].tolist()

    if 0:  # changed to the above approach as the below fixed hard coded one was
        with open("./blackListFeatures.pkl", "rb") as f:
            blackListFeatures = pickle.load(f)

    cp_features_analysis = list(
        set(cp_features)
        - set(locFeature2beremoved)
        - set(metadataFeature2beremoved)
        - set(blackListFeatures)
    )

    return cp_features, cp_features_analysis
