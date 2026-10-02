#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 09:39:41 2026

@author: yavuzkanat
"""

#%% image processing 

"""

create a rectangle

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("A-Cat.jpg")

copy = img.copy()

cv2.imshow('Image', img)

start = (450,420)

end = (1100,950)

color =(0,0,255)

thickness = 4

reatangle = cv2.rectangle(copy,start,end,color,thickness)

plt.imshow(cv2.cvtColor(copy, cv2.COLOR_BGR2RGB))



# %% Gray 

copy1 = img.copy()

copy1 = cv2.cvtColor(copy1,cv2.COLOR_BGR2GRAY)

plt.imshow(copy1,cmap="gray")

# %% Blue Channel

copy2 = img.copy()

copy2[:,:,2] = 255

plt.imshow(copy2)
# %%

"""
image[rows, columns, channel]

copy3
│
├── 500:1060  → rows
├── 400:1000  → columns
└── 1         → Green channel
                  ↓
                = 255
                
"""

copy3 = img.copy()

copy3[420:950,450:1100,0] = 1
copy3[420:950,450:1100,2] = 1



plt.imshow(cv2.cvtColor(copy3, cv2.COLOR_BGR2RGB))
plt.show()
# %% Addition of two Digital Images with the add Function

copy4 = img.copy()

copy5 = img.copy()

add = cv2.add(copy4,copy5)

plt.imshow(cv2.cvtColor(add, cv2.COLOR_BGR2RGB))
plt.show()

# %% Addition of two Digital Images with the AddWeighted Function at Specified Weights

copy6 = img.copy()

weightedAdd = cv2.addWeighted(add,0.2,copy6,0.4,0)

plt.imshow(cv2.cvtColor(weightedAdd, cv2.COLOR_BGR2RGB))

# %% Providing Blurring (smoothing) with the Blur Function on a Digital Image

meanFilter = cv2.blur(img,(9,9))

plt.imshow(cv2.cvtColor(meanFilter, cv2.COLOR_BGR2RGB))


# %% Blurring (smoothing) with the MedianBlur Function on a Digital Image

copy7 = img.copy()

medianFilter = cv2.medianBlur(copy7,3)

plt.imshow(cv2.cvtColor(medianFilter, cv2.COLOR_BGR2RGB))

# %% Performing Erosion Morphological Operation with Erode Function on Digital Image

copy8 = img.copy()
kernel = np.ones((3,3),np.uint8)
erosion1 = cv2.erode(copy8,kernel,iterations=8)
plt.imshow(cv2.cvtColor(erosion1, cv2.COLOR_BGR2RGB))


# %% Performing the Opening Morphological Operation with the MORPH_OPEN 
# Flag used in the MorphologyEx Function on the Digital Image

copy9 = img.copy()

kernel = np.ones((3,3),np.uint8)

opening = cv2.morphologyEx(copy9,cv2.MORPH_OPEN,kernel,iterations=8)

plt.imshow(cv2.cvtColor(opening, cv2.COLOR_BGR2RGB))



# %% Performing the Opening Morphological Operation with the MORPH_CLOSE
# Flag used in the MorphologyEx Function on the Digital Image

copy10 = img.copy()

kernel = np.ones((3,3),np.uint8)

opening = cv2.morphologyEx(copy9,cv2.MORPH_CLOSE,kernel,iterations=8)

plt.imshow(cv2.cvtColor(opening, cv2.COLOR_BGR2RGB))

# %% Performing the Morphological Gradient Morphological Operation with the
# MORPH_GRADIENT Flag used in the MorphologyEx Function on the Digital Image

copy11 = img.copy()

kernel = np.ones((3,3),np.uint8)

opening = cv2.morphologyEx(copy11,cv2.MORPH_GRADIENT,kernel,iterations=8)

plt.imshow(cv2.cvtColor(opening, cv2.COLOR_BGR2RGB))

# %% Performing the Top Ha t Morphological Operation with the MORPH_TOPHAT
# Flag used in the MorphologyEx Function on the Digital Image


copy12 = img.copy()

kernel = np.ones((6,6),np.uint8)

opening = cv2.morphologyEx(copy12,cv2.MORPH_GRADIENT,kernel,iterations=8)

plt.imshow(cv2.cvtColor(opening, cv2.COLOR_BGR2RGB))
# %% Performing Thresholding Operation with THRESH_BINARY Flag on Digital Image


copy13 = img.copy()

image_gray = cv2.cvtColor(copy13,cv2.COLOR_BGR2GRAY)

ret,thresh1 = cv2.threshold(image_gray,125,255,cv2.THRESH_BINARY)

plt.imshow(cv2.cvtColor(thresh1, cv2.COLOR_BGR2RGB))

# %% Performing Thresholding Operation with THRESH_BINARY_INV Flag on Digital Image

copy13 = img.copy()

image_gray = cv2.cvtColor(copy13,cv2.COLOR_BGR2GRAY)

ret,thresh1 = cv2.threshold(image_gray,127,255,cv2.THRESH_BINARY_INV)

plt.imshow(cv2.cvtColor(thresh1, cv2.COLOR_BGR2RGB))

# %%
