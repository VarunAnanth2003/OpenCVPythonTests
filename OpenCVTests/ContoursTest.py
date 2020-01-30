import cv2
import numpy

img = cv2.imread(r"C:\Users\shrav\Desktop\Most pics and vids\EscapeAchievementSnip.png")

bwimg = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)

ret, thresh = cv2.threshold(bwimg,100,100,100)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("img", im2)
cv2.waitKey(0)