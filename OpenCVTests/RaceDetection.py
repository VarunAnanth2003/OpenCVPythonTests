import cv2
import numpy

faceCascade = cv2.CascadeClassifier(r"C:\Users\shrav\Desktop\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")
capture = cv2.VideoCapture(0)

##ALL IN BGR COLOR FORMS
#----------------------------BROWN_BOUNDS----------------------------#
br_lower_bound = [10, 50, 10]
br_upper_bound = [20, 200, 255]
lower_br = numpy.array(br_lower_bound, numpy.uint8)
upper_br = numpy.array(br_upper_bound, numpy.uint8)

#----------------------------WHITE_BOUNDS----------------------------#
w_lower_bound = [50, 0, 100]
w_upper_bound = [255, 100, 255]
lower_w = numpy.array(w_lower_bound, numpy.uint8)
upper_w = numpy.array(w_upper_bound, numpy.uint8)

while True:
    ret, frame = capture.read()
    cv2.imshow('UnfilteredBGR', frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('UnfilteredHSV', hsv)

#----------------------------BROWN----------------------------#
    mask_br = cv2.inRange(hsv, lower_br, upper_br)
    outframe_br = cv2.bitwise_and(frame, frame, mask = mask_br)
    gray = cv2.cvtColor(outframe_br, cv2.COLOR_BGR2GRAY)
    faces_br = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    for (x, y, w, h) in faces_br:
        cv2.rectangle(outframe_br, (x, y), (x+w, y+h), (19, 69, 139), 5)
    cv2.imshow('ColorFilteredPic_BR', outframe_br)

#----------------------------WHITE----------------------------#
    mask_w = cv2.inRange(hsv, lower_w, upper_w)
    outframe_w = cv2.bitwise_and(frame, frame, mask = mask_w)
    gray = cv2.cvtColor(outframe_w, cv2.COLOR_BGR2GRAY)
    faces_w = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    for (x, y, w, h) in faces_w:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 5)

    cv2.imshow('ColorFilteredPic_W', outframe_w)
    c = cv2.waitKey(1)
    if c == 27:
        break

capture.release()
cv2.destroyAllWindows()
