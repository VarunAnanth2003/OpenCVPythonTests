import cv2
import numpy

img = cv2.imread(r"C:\Users\shrav\Desktop\Most pics and vids\EscapeAchievementImage.png")
## Note that all colors are in BGR form, NOT RGB.
lower_bound = [0, 0, 0] ##Lower bound for detection
upper_bound = [255, 255, 255] ##Upper bound for detection

lower = numpy.array(lower_bound, numpy.uint8)
upper = numpy.array(upper_bound, numpy.uint8)
mask = cv2.inRange(img, lower, upper)
outimg = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow('Image', outimg)
cv2.waitKey(0)