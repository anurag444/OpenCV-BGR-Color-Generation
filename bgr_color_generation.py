import numpy as np
import cv2


def printVal(x):
    print(x)


# Creating a black image
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('B', 'image', 0,255,printVal)
cv2.createTrackbar('G','image',0,255,  printVal)
cv2.createTrackbar('R', 'image', 0, 255, printVal)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0XFF
    if k==27:
        break

    # Getting the value of bgr
    b = cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G','image')
    r= cv2.getTrackbarPos('R', 'image')

    # Setting the bgr to img
    img[:] = [b,g,r]
cv2.destroyAllWindows()