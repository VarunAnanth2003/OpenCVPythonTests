import cv2
import numpy

##HOW TO USE:
#In the "low_x" variables, input the lower bound for color detection
#In the "upp_x" variables, input the upper bound for color detection
#This means: anything with RGB [(low_h > R > upp_h), (low_s > G > upp_s), (low_v > B > upp_v)] will show.
#All other colors will be black

#----------------------START_OF_USER_INPUT----------------------#
##Lower bound for detection
low_h = 10
low_s = 100
low_v = 20

##Upper bound for detection
upp_h = 20
upp_s = 255
upp_v = 100
#----------------------END_OF_USER_INPUT----------------------#

#----------------------START_OF_COMPUTER_PROCESSING----------------------#
faceCascade = cv2.CascadeClassifier(r"C:\Users\shrav\Desktop\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")
capture = cv2.VideoCapture(0)
##ALL CALCULATIONS DONE IN HSV
lower_bound = [low_h, low_s, low_v]
upper_bound = [upp_h, upp_s, upp_v]

lower = numpy.array(lower_bound, numpy.uint8)
upper = numpy.array(upper_bound, numpy.uint8)

while True:
    ret, frame = capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower, upper)
    outframe = cv2.bitwise_and(frame, frame, mask = mask)
    gray = cv2.cvtColor(outframe, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(outframe, (x, y), (x+w, y+h), (0, 255, 0), 5)

    cv2.imshow('UnfilteredWebcam', frame)
    cv2.imshow('ColorFilteredWebcam', outframe)

    c = cv2.waitKey(1)
    if c == 27:
        break

capture.release()
cv2.destroyAllWindows()
#----------------------END_OF_COMPUTER_PROCESSING----------------------#
