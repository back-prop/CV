'''
# Created by Srikanth Adya at 3/14/2019

'''

import cv2
import argparse

#Parse input arguments to get the image file path
ag = argparse.ArgumentParser()
ag.add_argument("-i","--image",required=True,help="Path to image file to be read")
args = vars((ag.parse_args()))

#Read image file using imread function
image = cv2.imread(args['image'])

#display read in image using imshow function
cv2.imshow('Image',image)
cv2.waitKey(0)

# Display the image size
# Note width is in the second column
print("Width is %d pixels",image.shape[1])
print("Height is %d pixels",image.shape[0])

# Write the image to a new file
cv2.imwrite('NewImage.JPG',image)
cv2.destroyAllWindows()

# Slice the image into 4 slices
# To do that we need the center of the image which is given by

cX = int(image.shape[1]/2)
cY = int(image.shape[0]/2)

print(cY,cX)
tL = image[0:cY,0:cX]
tR = image[0:cY,cX:image.shape[1]]
lL = image[cY:image.shape[0],0:cX]
lR = image[cY:image.shape[0],cX:image.shape[1]]

cv2.imwrite('TopLeft.png',tL)
cv2.imwrite('TopRight.png',tR)
cv2.imwrite('LowerRight.png',lR)
cv2.imwrite('Lowerleft.png',lL)

# Array Slice to change color of pixel

#image[0:cY,0:cX] = [0,255,0]
#cv2.imshow('ColoredImage',image)
#cv2.waitKey(0)

print(image[225,111])
