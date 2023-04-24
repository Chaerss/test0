import numpy as np
import cv2
import math
from PIL import Image
img = Image.open('albert Ainstain.png')
image = np.array(img)
print("a:",image)
print(image.shape)
gray_img=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
a = gray_img
print(gray_img.shape)
#print(len(gray_img))
cv2.imshow("ainsten",gray_img)
key = cv2.waitKey(0)
for i in range(len(gray_img)):
    for j in range(len(gray_img[0])):
        gray_img[i][j] = gray_img[i][j]*0.9 -5
print(gray_img)
cv2.imshow("LINEart",gray_img)
key = cv2.waitKey(0)
gray_img = a
for i in range(len(gray_img)):
    for j in range(len(gray_img[0])):
        if gray_img[i][j] <100:
           gray_img[i][j] = gray_img[i][j]*0.9 
        if gray_img[i][j] >=100 and gray_img[i][j] <170 :
           gray_img[i][j] = gray_img[i][j]*1
        if gray_img[i][j] >=170 and gray_img[i][j] >170 :
           gray_img[i][j] = gray_img[i][j]*0.7
cv2.imshow("DIVIDE_LINEart",gray_img)
key = cv2.waitKey(0)
gray_img = a
for i in range(len(gray_img)):
    for j in range(len(gray_img[0])):
        gray_img[i][j] = math.log(gray_img[i][j]+1) -2
cv2.imshow("LOG_LINEart",gray_img)
key = cv2.waitKey(0)