import cv2

image = cv2.imread('image/Desert.jpg')


blur = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#blur = cv2.GaussianBlur(image,(7,7),0)

cv2.imshow('Desert',blur)
cv2.waitKey(0)


gX = cv2.Sobel(blur,ddepth=cv2.CV_64F, dx=1, dy=0)
gY = cv2.Sobel(blur,ddepth=cv2.CV_64F,dx=0,dy=1)

gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

added = cv2.addWeighted(gX,0.5,gY,0.5,0)

cv2.imshow('Edges',added)
cv2.waitKey(0)
