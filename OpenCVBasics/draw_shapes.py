import cv2
import numpy as np
#initialize a canvas to draw on 
canvas = np.zeros((300,300,3))

# Initialize colors
green = (0,255,0)
red = (0,0,255)
blue = (255,0,0)
white = (255,255,255)

# Draw a green line from top let to bottom right
image = cv2.line(canvas, (0,0), (300,300),green)

# Draw a red line from top right to bottom left 3px thick
image = cv2.line(canvas, (0,300), (300,0),red, 3)

# Draw a red rectangle with 2px thick line
image = cv2.rectangle(canvas, (50,50),(150,100), red, 2)

# Draw a red rectangle with solid blue color fill 
image = cv2.rectangle(canvas, (30,10),(50,20), blue, -1)

cv2.imshow('Image',image)
cv2.waitKey()

# Initialize new canvas 
canvas = np.zeros((300,300,3),dtype='uint8')

# Draw 5 concentric circles
# notice the Floor division // (Divides and returns the integer value of the quotient. It dumps the digits after the decimal.)
(centerX,centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
for i in range(0,150,25):
    image = cv2.circle(canvas, (centerX,centerY),i,white)
cv2.imshow('Image',image)
cv2.waitKey()

# Draw many circles with random location and size
canvas = np.zeros((300,300,3))

print('Green',green)
for i in range(0,25):
    #np.random.seed(42)
    pt = np.random.randint(0,high=300,size=(2,))
    color = np.random.randint(0,high=256,size=(3,)).tolist()
    print(np.array(color))
    r = np.random.randint(5,high=150)
    image_cir = cv2.circle(canvas, tuple(pt), r, color, -1)
cv2.imshow('Image',image_cir)
cv2.waitKey()

