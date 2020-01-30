import cv2
import numpy

##HOW TO USE:
#In the "low_x" variables, input the lower bound for color detection
#In the "upp_x" variables, input the upper bound for color detection
#This means: anything with RGB [(low_r > R > upp_r), (low_g > G > upp_g), (low_b > B > upp_b)] will show.
#All other colors will be black

#----------------------START_OF_USER_INPUT----------------------#
##Lower bound for detection
low_r = 150
low_g = 150
low_b = 150

##Upper bound for detection
upp_r = 255
upp_g = 255
upp_b = 255
#----------------------END_OF_USER_INPUT----------------------#

#----------------------START_OF_COMPUTER_PROCESSING----------------------#
faceCascade = cv2.CascadeClassifier(r"C:\\Users\\shrav\\Desktop\\opencv-master\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml")
capture = cv2.VideoCapture(0)
##ALL CALCULATIONS DONE IN BGR
lower_bound = [low_b, low_g, low_r]
upper_bound = [upp_b, upp_g, upp_r]

lower = numpy.array(lower_bound, numpy.uint8)
upper = numpy.array(upper_bound, numpy.uint8)

while True:
    ret, frame = capture.read()

    mask = cv2.inRange(frame, lower, upper)
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