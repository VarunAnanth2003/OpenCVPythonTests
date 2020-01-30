import cv2
import numpy
import urllib
import requests

url = "http://192.168.1.13:8080/shot.jpg"

while True:
    url_resp = urllib.request.urlopen(url)
    img_array = numpy.array(bytearray(url_resp.read()), dtype=numpy.uint8)
    img = cv2.imdecode(img_array, -1)
    cv2.namedWindow("Stream", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Stream", 720, 540)

    cv2.imshow("Stream", img)

    c = cv2.waitKey(1)
    if c == 27:
        break

cv2.VideoCapture