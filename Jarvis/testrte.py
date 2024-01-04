from PIL import Image, ImageGrab
import pickle
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimage
import cv2
time.sleep(3)
Image.fromarray(obj)
# ituyiguygytgyf
import numpy as np
from numpy import asarray
a = mpimage.imread("C:\\Users\\pinki\\Downloads\\g.jpg")
# grey = 0
# array1 = asarray(a, dtype="int32")
r = a[:,:,0]
g = a[:,:,1]
b = a[:,:,2]
# a3  = open("a.txt", 'w')
# a3.write(str(array1))  
# a3.close()
# a3 = open("a.txt", "r")  

greyscale = (r*0.3+g*0.59+b*0.11)
# greyscale = (r+g+b)/3

print(greyscale)
plt.imshow(greyscale, cmap='gray')
plt.show()
# print(r)
# r = array1[0,0,0]
# g = array1[0,0,1]
# b = array1[0,0,2]
# gray = []
# for i in array1:
#     for j in i:
#         grey = (np.array(([r*0.3+g*0.6+b*0.1])))
#         gray.append(
#             grey
#         )
# greyscale = np.array(gray)
# print(greyscale)

# a = np.array([array1[0,0,0:1],
# array1[0,1,0:3],
# array1[0,2,0:3],
# array1[1,0,0:3],
# array1[1,1,0:3],
# array1[1,2,0:3]])
# print(a)

# print(r)
# print(g)
# print(b)
# image = 

# # a.show()
# print(g)
#     greyscale = np.array((r+g+b)/3)
#     print(greyscale)
# array3 = np.array()
