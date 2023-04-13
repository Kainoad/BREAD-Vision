import cv2
from numpy import *
import time
from picamera2 import Picamera2

from Colorintegration import ColorIntegration
from detect_and_track import DetectAndTrack

#image frame
height = 720
width = 1280
camera = Picamera2()
# camera.start_preview(Preview.QTGL)
# preview_config = picam2.create_preview_configuration()
capture_config = camera.create_still_configuration(main={"size": (width, height)})


# picam2.configure(preview_config)
camera.configure(capture_config)
camera.start()
# camera.resolution = (width, height)

time.sleep(2)
#for loop to index color until told to stop.
while(True):
    # camera.capture("img.jpg")
    # image = cv2.imread("img.jpg")
    # image = picam2.switch_mode_and_capture_image(capture_config)
    camera.capture_file("img.jpg")
    image = cv2.imread("img.jpg")
    
    print("Color Intregration:")
    print(ColorIntegration.process_image(image))

    print("Detect And Track:")
    print(DetectAndTrack.process_image(image))

    time.sleep(2)


