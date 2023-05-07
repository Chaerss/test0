import numpy as np
import cv2
import math
from PIL import Image
img = Image.open('albert Ainstain.png')
image = np.array(img)
gray_img=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
print(gray_img.shape)
gray_img = cv2.resize(gray_img,(100,100))
cv2.imshow("ainsten",gray_img)
key = cv2.waitKey(0)

def pingyi(nps,X,Y):
 print(len(nps)+Y,len(nps[0])+X)
 npt = np.zeros((len(nps)+Y,len(nps[0])+X))
 for i in range(len(nps)):
     for j in range(len(nps[0])):
        npt[Y+i][X+j] = nps[i][j]
 return npt

def jingxiang(nps):
 print(len(nps),len(nps[0]))
 npt = np.zeros((len(nps),len(nps[0])))
 for i in range(len(nps)):
     for j in range(len(nps[0])):
        npt[i][j] = nps[i][len(nps[0])-j-1]
 return npt

def ImageRotate(image):
    h, w = image.shape[:2] 
    center = (w // 2, h // 2)  
    angle = 45  
    scale = 0.8  
    M = cv2.getRotationMatrix2D(center=center, angle=-angle, scale=scale)  
    image_rotation = cv2.warpAffine(src=image, M=M, dsize=(w, h), borderValue=(255, 255, 255))
    return image_rotation
z = pingyi(gray_img,50,0)
s = jingxiang(gray_img)
d = ImageRotate(gray_img)
data1=np.array(z,dtype='uint8')
data2=np.array(s,dtype='uint8')
data3=np.array(d,dtype='uint8')
cv2.imshow("PY",data1)
cv2.imshow("JX",data2)
cv2.imshow("XZ",data3)
key = cv2.waitKey(0)
