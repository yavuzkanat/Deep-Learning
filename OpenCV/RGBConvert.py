import cv2
import numpy as np

#%% Load & Normal İmage 
img = cv2.imread("OpenCV/A-Cat.jpg")

cv2.imshow('Image', img)

"""
he parameter of this function is the number of
miliseconds the function waits for a keypress. 
With a value of 0 the function waits indefinitely.
"""
cv2.waitKey(0)

cv2.destroyAllWindows()

image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#%% Gray Image
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('gray_image.jpg', gray_image)

cv2.imshow("Gray", gray_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

#%% Canny algorithm

Canny_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

""" Detects edges in the input image. 
 The two parameters define the lower and upper 
 thresholds for edge detection."""

edges = cv2.Canny(gray_image,100,100)

cv2.imshow("Canny", edges)

cv2.waitKey(0)

cv2.destroyAllWindows()

#%% Using Numpy 

"""
Different from the more common RGB ordering, OpenCV uses the ordering BGR.
"""

img = np.zeros((5, 5, 3), np.uint8)

img[:] = (0, 0, 0) 

img[0, 0] = (0, 0, 255)

img[0, 1] = (0, 255, 0)

img[0, 2] = (255, 0, 0)

img[0, 3] = (0, 0, 0)

img[0, 4] = (0, 90, 0)

img[1, 0] = (0, 0, 255)

img[1, 1] = (10, 125, 0)

img[1, 2] = (20, 250, 100)

img[1, 3] = (30, 0, 230)

img[1, 4] = (40, 60, 0)

img[2, 0] = (0, 120, 255)

img[2, 1] = (10, 125, 188)

img[2, 2] = (20, 250, 250)

img[2, 3] = (30, 0, 230)

img[2, 4] = (40, 60, 220)

cv2.imshow('RGB',img)

cv2.waitKey(0)

cv2.destroyAllWindows()




#%% Draw a line 
"""
image where the line is added
• start point p0
• end point p1
• line color
• line thickness

"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
CYAN = (255, 255, 0)
MAGENTA = (255, 0, 255)
YELLOW = (0, 255, 255)

p0 = 10, 10
p1 = 300, 90
p2 = 500, 10

cv2.line(img, p0, p1, RED, 2)
cv2.line(img, p1, p2, YELLOW, 5)

cv2.imshow('Lines',img)

cv2.waitKey(0)

cv2.destroyAllWindows()

#%% Making Images Darker or Lighter   


img = cv2.imread("OpenCV/A-Cat.jpg")

mg = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
M = np.ones(img.shape, dtype='uint8') * 40
M2 = np.ones(img.shape, dtype='uint8') * 120
M3 = np.ones(img.shape, dtype='uint8') * 180
brighter = cv2.add(img, M)
darker = cv2.subtract(img, M)
darker2 = cv2.subtract(img, M2)
darker3 = cv2.subtract(img, M3)
img2 = np.hstack([img, brighter, darker,darker2,darker3])
cv2.imshow('window', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


#%% Extracting an object based on hue



import cv2 as cv
import numpy as np

img = cv.imread('OpenCV/2.jpeg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
def trackbar(x):
    lower = (x, 30, 30)
    upper = (x+5, 250, 250)
    mask = cv.inRange(hsv, lower, upper)
    img2 = cv.bitwise_and(img, img, mask=mask)
    cv.imshow('window', np.vstack([img, img2]))
cv.imshow('window', img)

cv.createTrackbar('hue','window', 0, 179, trackbar)
cv.waitKey(0)
cv.destroyAllWindows()

#%% Color spaces

"""Change the color space."""
import cv2 as cv
import numpy as np
img = cv.imread('OpenCV/A-Cat.jpg')
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
M = np.ones(img.shape, dtype='uint8') * 40
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
xx = cv.cvtColor(img, cv.COLOR_BGR2HLS)
xx2 = cv.cvtColor(img, cv.COLOR_BGR2YUV)
img2 = np.hstack([img, hsv, lab,xx,xx2])
cv.imshow('window', img2)
cv.waitKey(0)
cv.destroyAllWindows()
