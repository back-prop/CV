import cv2
import numpy as np

image = cv2.imread('image/19612_cam-image_array_.jpg')
#image = cv2.imread('image/16002_cam-image_array_.jpg')
blur = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('GC',blur)
cv2.waitKey(0)

edges = cv2.Canny(blur,225,250)

cv2.imshow('non-auto',edges)
cv2.waitKey(0)

def auto_canny(image,sigma=0.33):

    med = np.median(image)
    lower = int(max(0,(1-sigma)*med))
    upper = int(min(255,(1+sigma)*med))
    new_edges = cv2.Canny(image,lower,upper)

    return new_edges

cv2.imshow('Auto-Canny',auto_canny(blur))
cv2.waitKey(0)
