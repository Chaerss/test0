import cv2
import numpy as np
import os
from PIL import Image

#计算雾化图像的暗通道
def dark_channel(img, size = 15):
    r, g, b = cv2.split(img)
    min_img = cv2.min(r, cv2.min(g, b))#取最暗通道
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    dc_img = cv2.erode(min_img,kernel)
    return dc_img

#估计全局大气光值
def get_atmo(img_dark_0,img):
    img_dark= img_dark_0
    Ar= img_dark_0
    Ag= img_dark_0
    Ab= img_dark_0
    max = np.max(img_dark)
    for i in range(len(img_dark)):
     for j in range(len(img_dark[0])):
        if img_dark[i][j] > 0.95*max:
          img_dark[i][j] = 1
        else:
          img_dark[i][j] = 0
    for i in range(len(img_dark)):
     for j in range(len(img_dark[0])):
        Ar[i][j] = img[i][j][0]* img_dark[i][j]
        Ag[i][j] = img[i][j][1]* img_dark[i][j]
        Ab[i][j] = img[i][j][2]* img_dark[i][j]
    A= np.zeros((800,1201,3))
    for z in range(3):
     for i in range(len(img_dark)):
       for j in range(len(img_dark[0])):
         if z ==0:
           A[i][j][z] = Ar[i][j]
         if z ==1:
           A[i][j][z] = Ag[i][j]
         if z ==2:
           A[i][j][z] = Ab[i][j]
    return A
#估算透射率图
def get_trans(img,A,img_dark):
   tdark=img
   t=np.zeros(3)
   min = np.min(img_dark)
   for i in range(len(img_dark)):
     for j in range(len(img_dark[0])):
        if img_dark[i][j] == min:
           a=i
           b=j
   for d in range(3):
     print(img.shape)
     print(A.shape)
     print(t.shape)
     t[d] = 1 - img[a][b][d]/A[a][b][d]
   for z in range(3):
     for i in range(len(img_dark)):
       for j in range(len(img_dark[0])):
         tdark[i][j][z] = t[z]
   return tdark

def fogdissipate(I):
  dark = dark_channel(I)
  A = get_atmo(dark,I)
  t = get_trans(I,A,dark)
  J = (I-A)/t +A
  return J
image = cv2.imread('TRAINfog.png')
cv2.imshow('basic',image)
key = cv2.waitKey(0)
J = fogdissipate(image)
J=np.array(J,dtype='uint8')
cv2.imshow('fogdissipate',J)
key = cv2.waitKey(0)
