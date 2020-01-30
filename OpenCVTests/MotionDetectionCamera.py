import numpy
import cv2

#--------------------------------------------USER_INPUT--------------------------------------------#
##Choose a value between 1 and 100:
#1 -> VERY HARD to trigger detection
#100 -> VERY EASY to trigger detection
#Sets the bounds for how many pixels need to be nonZero for movement to be detected
sensitivity = 100

##Choose a value between 1 and n for both parameters, with lowrefreshRate < highrefreshRate:
#1 -> Refreshes EVERY tick
#n -> Refreshes EVERY n ticks
#lowrefreshRate is used when movement ISN'T detected, highrefreshRante is used when motion IS detected
lowrefreshRate = 3
highrefreshRate = 30
#--------------------------------------------END_OF_USER_INPUT--------------------------------------------#

refreshRate = lowrefreshRate
detected = False
capture = cv2.VideoCapture(0)
lower = numpy.array([22], numpy.uint8)
upper = numpy.array([255], numpy.uint8)
counter = 0
myFile = open("C:/Users/shrav/Desktop/MotionDetectionAlertSystem/TestArduinoFileText.txt", "w")

while True:
    ret, OGframe = capture.read()
    cv2.imshow('Pre-FilterWebFeed', OGframe)

    c = cv2.waitKey(1)
    if c == 27:
        break
cv2.destroyAllWindows()

ret, firstcap = capture.read()
cv2.imshow('InitialBackgroundImage', firstcap)
cv2.waitKey(0)

while True:
    counter = counter + 1
    if(counter > refreshRate):
        counter = 0
        ret, firstcap = capture.read()
    ret, frame = capture.read()
    diff = cv2.absdiff(firstcap, frame)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    black_mask = cv2.inRange(gray, lower, upper)
    outframe = cv2.bitwise_and(frame, frame, mask = black_mask)
    coloredpixels = cv2.countNonZero(black_mask)
                        
    if coloredpixels > ((-1000 * sensitivity) + 101000):
        detected = True
        refreshRate = highrefreshRate
    else:
        detected = False
        refreshRate = lowrefreshRate

    if detected == True:
        print ("Detected Movement")
        myFile.write("y")
        myFile.close
        myFile = open("C:/Users/shrav/Desktop/MotionDetectionAlertSystem/TestArduinoFileText.txt", "w")
    else:
        print ("No Movement Detected")
        myFile.write("n")
        myFile.close
        myFile = open("C:/Users/shrav/Desktop/MotionDetectionAlertSystem/TestArduinoFileText.txt", "w")
    realoutput = cv2.cvtColor(outframe, cv2.COLOR_RGBA2GRAY)
    finalout, contours, hierarchy = cv2.findContours(realoutput, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(finalout, contours, -1, (255,255,255), 3)
    cv2.imshow('MotionDetectionCamera', finalout)
    canRefresh = False
    c = cv2.waitKey(1)
    if c == 27:
        break

myFile.write("n")
myFile.close
capture.release()
cv2.destroyAllWindows()
