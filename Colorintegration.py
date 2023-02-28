import cv2
# from numpy import *
import numpy as np

class ColorIntegration:
    def __init__(self):
        #initialize tolarance specs
        required = np.array([10,10,10])
        utolarance = np.array([0,0,0])
        ltolarance = np.array([0,0,0])
        utolarance = required+10
        ltolarance = required-10
        #image frame
        height = 720
        width = 1280
    def process_image(image):
        color = np.array(image[int(height/2),int(width/2)])
        # print(color)
        if all(ltolarance<color) and all(utolarance>color):
            return str(color) + "True"
        else:
            return str(color) + "False"