import cv2
import numpy

capture = cv2.VideoCapture(0)
## ALL CALCULATIONS DONE IN BGR
lower_bound = [175, 175, 175] ##Lower bound for detection
upper_bound = [255, 255, 255] ##Upper bound for detection

lower = numpy.array(lower_bound, numpy.uint8)
upper = numpy.array(upper_bound, numpy.uint8)

while True:
    ret, frame = capture.read()

    mask = cv2.inRange(frame, lower, upper)
    outframe = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('UnfilteredWebcam', frame)
    cv2.imshow('ColorFilteredWebcam', outframe)

    c = cv2.waitKey(1)
    if c == 27:
        break

capture.release()
cv2.destroyAllWindows()