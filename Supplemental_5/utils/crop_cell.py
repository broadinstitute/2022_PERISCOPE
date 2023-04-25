"""
@author: mhaghigh
"""

import numpy as np


def crop_single_cell_image(image, xCenter,yCenter,halfBoxSize):

    im_h,im_w=image.shape;
#     print(im_w,im_h)
    before_y_pad=0
    after_y_pad=0
    before_x_pad=0
    after_x_pad=0

    if xCenter-halfBoxSize<0:
        before_x_pad=abs(xCenter-halfBoxSize)

    if yCenter-halfBoxSize<0:
        before_y_pad=abs(yCenter-halfBoxSize)

    if xCenter+halfBoxSize>im_w:
        after_x_pad=abs(im_w-xCenter-halfBoxSize)

    if yCenter+halfBoxSize>im_h:
        after_y_pad=abs(im_h-yCenter-halfBoxSize)

    image_cropped=image[np.maximum(yCenter-halfBoxSize,0):np.minimum(yCenter+halfBoxSize,im_h),\
                        np.maximum(xCenter-halfBoxSize,0):np.minimum(xCenter+halfBoxSize,im_w)]
#     print('image_cropped',image_cropped.shape)
    if np.max([before_y_pad, after_y_pad,before_x_pad, after_x_pad])>0:
        image_cropped=np.pad(image_cropped, ((before_y_pad, after_y_pad), (before_x_pad, after_x_pad)), 'minimum')
#         print('image_cropped',image_cropped.shape)

    return image_cropped