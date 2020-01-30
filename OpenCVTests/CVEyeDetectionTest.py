import cv2

eyeCascade = cv2.CascadeClassifier(r"C:\Users\shrav\Desktop\opencv-master\opencv-master\data\haarcascades\haarcascade_eye.xml")

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eyeCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
    cv2.imshow('Webcam', frame)
    c = cv2.waitKey(1)
    if c == 27:
        break
capture.release()
cv2.destroyAllWindows()