import cv2
from numpy import *
import time
from picamera import PiCamera
#initialize tolarance specs
required=array([10,10,10])
utolarance=array([0,0,0])
ltolarance=array([0,0,0])
utolarance=required+10
ltolarance=required-10
#image frame
height = 720
width = 1280
camera = PiCamera()
camera.resolution = (1280, 720)
time.sleep(2)
#for loop to index color until told to stop.
while(True):
    camera.capture("img.jpg")
    image = cv2.imread("img.jpg")
    color=array(image[int(height/2),int(width/2)])
    print(color)
    if all(ltolarance<color) and all(utolarance>color):
        print("True")
    else:
        print("False")
