import pandas as pd
def custom_create_image_path_cols(params, df_p_s, channels):
    """
    The following columns are needed for generation of single cell images,\
    if you already have it just modify the config file,
    if not you have to generate them
    """

    paths = params["paths"]
    meta_cols = params["meta_cols"]
    viz_cols = params["viz_cols"]
    batch = params["paths"]["batch_folder"]

    for ch in channels:
        df_p_s["PathName_Corr" + ch] = (
            paths["root_dir"]
            + "images/"
            + paths["batch_folder"]
            + "/images_corrected_cropped/"
            + df_p_s[meta_cols["plate"]]
            + "_"
            + df_p_s[meta_cols["well"]]
            + "/Corr"
            + ch
        )

        df_p_s["FileName_Corr" + ch] = (
            "Corr"
            + ch
            + "_"
            + "Site_"
            + df_p_s[meta_cols["site"]].astype(str)
            + ".tiff"
        )

    df_p_s["Path_Outlines"] = (
        paths["root_dir"]
        + "workspace/analysis/"
        + batch
        + "/"
        + df_p_s[meta_cols["plate"]]
        + "-"
        + df_p_s[meta_cols["well"]]
        + "-"
        + df_p_s[meta_cols["site"]].astype(str)
        + "/"
        + "CorrDNA_Site_"
        + df_p_s[meta_cols["site"]].astype(str)
        + "_Overlay.png"
    )

    return df_p_s