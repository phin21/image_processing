
import cv2 as cv 
import numpy as np
img = cv.imread("osi123-1.jpg")
(h, w) = img.shape[0:2]
for i in range(h):
    for j in range(w):
        r = img [i][j][0]
        g = img [i][j][1]
        b = img [i][j][2]
        
        gv = r*0.299 + g*0.587 + b*0.114
        img [i][j] = gv
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()

