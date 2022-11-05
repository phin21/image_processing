import cv2 as cv 
import numpy as np
img = cv.imread("osi123-1.jpg")
(h, w) = img.shape[0:2]
for i in range(h):
    for j in range(w):
        r = 255-img [i][j][0]
        g = 255- img [i][j][1]
        b =255- img [i][j][2]
        
        img [i][j] = [r,g,b]
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()
