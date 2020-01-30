import cv2
import numpy

#Color Ranges
lower = numpy.array([225,225,225], numpy.uint8)
upper = numpy.array([255,255,255], numpy.uint8)
pixel = (20,20,20)
image_hsv = None

capture = cv2.VideoCapture(0)
#Original Color-Filter
ret, img = capture.read()
while True:
    def pick_color(event,x,y,flags,param):
            pixel = image_hsv[y,x]
    ret, OGframe = capture.read()
    #filterimg = cv2.inRange(OGframe, lower, upper)
    #outimg = cv2.bitwise_and(OGframe, OGframe, mask = filterimg)
    cv2.imshow('Pre-FilterWebFeed', OGframe)
    image_bgr = cv2.cvtColor(OGframe, cv2.COLOR_BGR2RGB)
    print(pixel)
    c = cv2.waitKey(1)
    if c == 27:
        break
cv2.destroyAllWindows()

#Contoured Feed
while True:
    ret, frame = capture.read()
    filterimg = cv2.inRange(frame, lower, upper)
    outimg = cv2.bitwise_and(frame, frame, mask = filterimg)

    bwimg = cv2.cvtColor(outimg, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(bwimg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)
    kernel = numpy.ones((10,10),numpy.uint8)
    eroded = cv2.erode(bwimg, kernel)
    newimg, contours, hierarchy = cv2.findContours(eroded,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    output = cv2.drawContours(newimg, contours, -1, (0,0,0), 3)

    cv2.imshow("Feed", output)
    c = cv2.waitKey(1)
    if c == 27:
        break

capture.release()
cv2.destroyAllWindows()