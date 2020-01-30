import cv2
import numpy

faceCascade = cv2.CascadeClassifier(r"C:\Users\shrav\Desktop\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")
capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
        cv2.rectangle(frame, (x+int(w/2), y+int(h/2)), (x+int(w/2), y+int(h/2)), (0, 0, 0), 5)

        if (x+int(w/2)) < 320:
            print("Turn Right")
        else:
            print("Turn Left")

        if (y+int(h/2)) < 240:
            print("Turn Up")
        else:
            print("Turn Down")

    cv2.imshow('Webcam', frame)
    
    c = cv2.waitKey(1)
    if c == 27:
        break

capture.release()
cv2.destroyAllWindows()