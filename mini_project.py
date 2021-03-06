# -*- coding: utf-8 -*-
"""Mini Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zGaJyei-no8fyfFJlVnc_PPf7rbaTNKp
"""

from google.colab.patches import cv2_imshow
import cv2
from matplotlib import pyplot as plt
import numpy as np
import math

from google.colab import drive
drive.mount('/content/drive')

"""Showing Image"""

img = cv2.imread('/content/drive/MyDrive/Files for colab/flower.jpg')
cv2_imshow(img)

"""# Computing Histogram

Computing Histogram using cv2
"""

img = cv2.imread('/content/drive/MyDrive/Files for colab/sample.png', 0)
cv2_imshow(img)
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

"""Computing Histogram using own defined function"""

def histogram_comp(image):
    height = image.shape[0]
    width = image.shape[1]
    histogram = np.zeros([256], np.int32)

    for x in range(0, height):
        for y in range(0, width):
            histogram[image[x, y]] += 1
    return histogram

def plot_histogram(histogram):
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Intensity level")
    plt.ylabel("Intensity frequency")
    plt.xlim([0, 256])
    plt.plot(histogram)
    plt.savefig("Histogram_sample.jpg")

input_image = cv2.imread('/content/drive/MyDrive/Files for colab/histogram image.jpg', 0)
input_image = cv2.resize(input_image, (800, 600))
img = input_image
histogram_grayscale = histogram_comp(img)
for i in range(0, len(histogram_grayscale)):
    print("Histogram[", i, "]: ", histogram_grayscale[i])
plot_histogram(histogram_grayscale)

"""# Histogram Equilization"""

s = img.shape
cv2_imshow(img)
#input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
#cv2_imshow(input_image)
x = histogram_grayscale.reshape(1,256)
y = np.array([])
y = np.append(y, x[0, 0])

for i in range(255):
  k = x[0, i+1] + y[i]
  y = np.append(y, k)
y = np.round((y/(s[0]*s[1]))*(256-1))

for i in range(s[0]):
  for j in range(s[1]):
    k = img[i, j]
    img[i, j] = y[k]
equalized = histogram_comp(img)
plot_histogram(equalized)
cv2_imshow(img)

"""Histogram Equalization using Cv2 Function"""

img = input_image
#img = np.full((100,80,3), 12, dtype = np.uint8)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(img)
plot_histogram(equalized)
cv2_imshow(img)

"""# Histogram Streching"""

img = input_image
x = histogram_grayscale.reshape(1,256)
y = np.zeros((1,256))

for i in range(256):
  if x[0,i] == 0: y[0, i] = 0
  else : y[0, i] = i
min = np.min(y[np.nonzero(y)])
max = np.max(y[np.nonzero(y)])

strech = np.round(((255-0)/(max-min))*(y-min))
strech[strech<0] = 0
strech[strech>255] = 255

for i in range(s[0]):
  for j in range(s[1]):
    k = img[i, j]
    img[i, j] = strech[0, k]
streched = histogram_comp(img)
plot_histogram(streched)
cv2_imshow(img)

"""# Simple Thresholding"""

def simpleThresolding(tvalue,img):
    for row in range(0,img.shape[0]):
        for col in range(0,img.shape[1]):
            if img[row][col] >= tvalue:
                img[row][col]=255
            else:
                img[row][col]=0
    return img

img = cv2.imread('/content/drive/MyDrive/Files for colab/2020CSB064 PENUGONDA_S - 9.bmp')
cv2.resize(img, (800, 600))
cv2_imshow(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_thres = simpleThresolding(150, img)
cv2_imshow(img_thres)

"""# Adaptive Thresholding"""

img =  cv2.imread('/content/drive/MyDrive/Files for colab/2020CSB064 PENUGONDA_S - 2.bmp')

#_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2_imshow(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2);
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2_imshow(th2)
cv2_imshow(th3)

"""# OTSU Thresholding"""

img = input_image
histogram = cv2.calcHist([img], [0], None, [255], [0,255])
within = []

from skimage.filters import threshold_otsu
img =  cv2.imread('/content/drive/MyDrive/Files for colab/2020CSB064 PENUGONDA_S - 10.bmp')
cv2_imshow(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = threshold_otsu(img)
img_thres = simpleThresolding(thresh, img)
cv2_imshow(img_thres)

for i in range(len(histogram)):
  x, y = np.split(histogram, [i])
  x1 = np.sum(x)/(img.shape[0]*img.shape[1])
  y1 = np.sum(y)/(img.shape[0]*img.shape[1])
  x2 = np.sum([j*t for j, t in enumerate(x)])/np.sum(x)
  y2 = np.sum([j*t for j, t in enumerate(y)])/np.sum(y)
  x3 = np.sum([(j-x2)**2*t for j, t in enumerate(x)])/np.sum(x)
  x3 = np.nan_to_num(x3)
  y3 = np.sum([(j-y2)**2*t for j, t in enumerate(y)])/np.sum(y)
  within.append(x1*x3 + y1*y3)
m = np.argmin(within)
print(m)

"""# Filtering"""

img = input_image
#img =  cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel = np.ones((5,5),np.float32)/25
dst= cv2.filter2D(img ,-1,kernel)

#averaging method
blur =cv2.blur(img,(5,5))
#Gaussian method
gblur=cv2.GaussianBlur(img,(5,5),0)
#salt and paper filter
median =cv2.medianBlur(img,5)
#bilateral filter
bilateralFilter=cv2.bilateralFilter(img,9,75,75)

titles =['image','2D Convolution','blur','gaussianblur','median','bilateralFilter']
images = [img,dst,blur,gblur,median,bilateralFilter]

for i in range (6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])



"""# Image Segmentation using Histogram"""

from skimage.io import imread, imshow
from skimage.color import rgb2gray, rgb2hsv
from skimage.morphology import area_opening
from skimage.exposure import histogram
from skimage.filters import threshold_otsu

chico = imread('/content/drive/MyDrive/Files for colab/tree.png')
imshow(chico);

th_values = np.linspace(0, 1, 11)
fig, axis = plt.subplots(2, 5, figsize=(15,8))
chico_gray = rgb2gray(chico)
for th, ax in zip(th_values, axis.flatten()):
    
    chico_binarized = chico_gray < th
    ax.imshow(chico_binarized)
    ax.set_title('$Threshold = %.2f$' % th)

freq, bins = histogram(chico_gray)
plt.step(bins, freq*1.0/freq.sum())
plt.xlabel('Intensity value')
plt.ylabel('Fraction of pixels');

def masked_image(image, mask):
    r = image[:,:,0] * mask
    g = image[:,:,1] * mask
    b = image[:,:,2] * mask
    return np.dstack([r,g,b])

fig, ax = plt.subplots(1, 2, figsize=(12,6))
thresh = threshold_otsu(chico_gray)
chico_otsu  = chico_gray < thresh
ax[0].imshow(chico_otsu)
filtered = masked_image(chico, chico_otsu)
ax[1].imshow(filtered)

fig, ax = plt.subplots(1, 3, figsize=(15,6))
ax[0].imshow(chico[:,:,0], cmap='Reds')
ax[0].set_title('Red')
ax[1].imshow(chico[:,:,1], cmap='Greens')
ax[1].set_title('Green')
ax[2].imshow(chico[:,:,2], cmap='Blues')
ax[2].set_title('Blue');