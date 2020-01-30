import cv2
import numpy

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    cv2.imshow("Camera", frame)
    c = cv2.waitKey(1)
    if c == 27:
        break

capture.release()
cv2.destroyAllWindows()