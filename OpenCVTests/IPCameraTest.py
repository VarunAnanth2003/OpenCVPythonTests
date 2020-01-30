import cv2
import numpy
import urllib
import requests

url = "http://192.168.1.13:8080/shot.jpg"
url_resp = urllib.request.urlopen(url)
img_array = numpy.array(bytearray(url_resp.read()), dtype=numpy.uint8)
img = cv2.imdecode(img_array, -1)
cv2.imshow("Image", img)
cv2.waitKey(0)