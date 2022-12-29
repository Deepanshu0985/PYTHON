import colorsys
from turtle import color
import cv2
import numpy as np



img = cv2.imread("cartoon\cating.JPG")

gray = cv2.cvtColor (img,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)
edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)


color =cv2.bilateralFilter(img,9,250,250)

cartoon = cv2.bitwise_and(color,color,mask=edges)

cv2.imshow("Image",img)
cv2.imshow("edges",edges)
cv2.imshow("Cartoon",cartoon)
cv2.imwrite('cartoon\image.png',img)
cv2.imwrite('cartoon\edges.png',edges)
cv2.imwrite('cartoon\cartoon.png',cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

