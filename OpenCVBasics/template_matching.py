import cv2

template = cv2.imread('image/template.png')

source = cv2.imread('image/source.png')



result = cv2.matchTemplate(source,template,cv2.TM_CCOEFF)
(minVal,maxVal,minloc,(x,y)) = cv2.minMaxLoc(result)


