import cv2
import numpy as np
image = cv2.imread('image/16002_cam-image_array_.jpg')


image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(image,(7,7),0)

cv2.imshow('Desert',blur)
cv2.waitKey(0)

gX = cv2.Sobel(blur,ddepth=cv2.CV_64F,dx=1,dy=0)
gY = cv2.Sobel(blur,ddepth=cv2.CV_64F,dx=0,dy=1)

gradient = np.sqrt(np.square(gX),np.square(gY))
orient = np.arctan(gY,gX)*(180/np.pi)%180

idx = np.where(orient >= 100,orient,-1)
idx = np.where(idx <=180,idx,-1)

mask = np.zeros(image.shape,dtype='uint8')
mask[idx > -1] = 255

cv2.imshow('Mask',mask)
cv2.waitKey(0)
