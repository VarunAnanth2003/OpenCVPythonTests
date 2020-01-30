import cv2
import numpy

capture = cv2.VideoCapture(0)

lower_rgb = numpy.array([150,150,150], numpy.uint8)
upper_rgb = numpy.array([255,255,255], numpy.uint8)

while True:
    ret, frame = capture.read()
    mask = cv2.inRange(frame, lower_rgb, upper_rgb)

    cv2.imshow("Camera", mask)
    
    c = cv2.waitKey(1)
    if c == 27:
        break

capture.release()
cv2.destroyAllWindows()