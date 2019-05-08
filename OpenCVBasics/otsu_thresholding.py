import cv2

image = cv2.imread('image/threshold_example.png')
cv2.imshow('Coins',image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blured = cv2.GaussianBlur(gray,(7,7),0)

(T,thresholdInv) = cv2.threshold(blured,200,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)


cv2.imshow('Output',cv2.bitwise_and(image, image, mask=thresholdInv))
cv2.waitKey(0)
print(T)
