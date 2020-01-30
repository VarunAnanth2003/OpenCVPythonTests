import cv2
import numpy

##Gets .xml haarcascade
faceCascade = cv2.CascadeClassifier(r"C:\Users\shrav\Desktop\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")

##Sets video source to computer webcam
capture = cv2.VideoCapture(0)
while True:
    ##Capture each frame from a webcam (because it is in a loop) which makes it a video
    ret, frame = capture.read()

    ##Converts image to grayscale for cascading/facial detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ##This detects the face from the grayscale webcam
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    ##Draws a green rectangle around the faces detected
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    ##Displays colored webcam feed
    cv2.imshow('Webcam', frame)
    
    ##ESC to quit
    c = cv2.waitKey(1)
    if c == 27:
        break

##After break, shuts down systems
capture.release()
cv2.destroyAllWindows()