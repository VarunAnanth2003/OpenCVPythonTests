import cv2

capture = cv2.VideoCapture(0)
``
while True:
    ret, frame = capture.read()
    cv2.imshow('WebFeed', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

fheight = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
fwidth = int(capture.get( cv2.CAP_PROP_FRAME_HEIGHT)) 
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
outputVideo = cv2.VideoWriter('outputVid.avi', fourcc, 30, (fwidth, fheight))

outputVideo.release()     
capture.release()   
cv2.destroyAllWindows()