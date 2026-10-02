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
import matplotlib.pyplot as plt

img = cv2.imread("A-Cat.jpg")

cv2.imshow('Image', img)

start = (450,420)

end = (1100,950)

color =(0,0,255)

thickness = 4

reatangle = cv2.rectangle(img,start,end,color,thickness)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))



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

    
