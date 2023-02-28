import cv2
from numpy import *
import time
from picamera import PiCamera

from Colorintegration import ColorIntegration
from detect_and_track import DetectAndTrack

#image frame
height = 720
width = 1280
camera = PiCamera()
camera.resolution = (width, height)
time.sleep(2)
#for loop to index color until told to stop.
while(True):
    camera.capture("img.jpg")
    image = cv2.imread("img.jpg")
    
    print("Color Intregration:")
    print(ColorIntegration.process_image(image))

    print("Detect And Track:")
    print(DetectAndTrack.process_image(image))

    time.sleep(2)


