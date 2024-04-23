"""
@author: mhaghigh
"""

import numpy as np
import skimage


def CP_to_RGB_single(im_cp, channels):
    """
    This function takes a cell paiting image (as channels last array) and converts it to RGB

    Inputs:
    ++ im_cp   (np array) size --> (width)x(height)x(channels):
    input dataframe contains single cells profiles as rows (make sure it has "Nuclei_Location_Center_X"or"Y" columns)

    ++ channels (dtype: list): list of channels to be displayed as columns of output image
           example: channels=['Mito','AGP','Brightfield','ER','DNA','Outline']

    Returns:
    colorImage0 (np array): dims-> width , height , 3 (RGB channels)

    """
    import matplotlib.colors as mcolors

    depth = 65535
    channels_colormap = {
        "DNA": "Blue",
        "ER": "Green",
        "RNA": "Yellow",
        "AGP": "Red",
        "Mito": "Magenta",
        "DAPI": "Blue",
        "WGA": "Red",
        "Phalloidin": "Yellow",
    }

    channel_colors = [
        np.array(mcolors.to_rgb(channels_colormap[c])) * depth for c in channels
    ]

    comb_pars = [1 / im_cp.shape[2]] * im_cp.shape[2]
    colorImagesList = []
    for i in range(im_cp.shape[2]):
        image_gray = im_cp[:, :, i]
        image_color = (
            (skimage.color.gray2rgb(image_gray).astype(float) / depth)
            * channel_colors[i]
            * comb_pars[i]
        )
        colorImagesList.append(image_color)

    colorImage0 = sum(colorImagesList)  # .astype(np.uint8)

    colorImage0 = skimage.exposure.rescale_intensity(
        colorImage0, out_range=(0, 255)
    ).astype(np.uint8)

    colorImagesList2 = [
        skimage.exposure.rescale_intensity(colim, out_range=(0, 255)).astype(np.uint8)
        for colim in colorImagesList
    ]

    return colorImage0, colorImagesList2
