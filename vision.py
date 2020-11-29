from picamera import PiCamera
from time import sleep
import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd



def capture_board_state(): 
    camera = PiCamera()
    camera.start_preview()
    camera.capture('/home/pi/Desktop/106a_project/board.jpg')
    sleep(5)                # Give sometime to capture the board state in case things go wrong
    camera.stop_preview()

def process_board_state(robot_move): 
    frame = cv2.imread('/home/pi/Desktop/106a_project/board.jpg')
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray_img, aruco_dict, parameters=parameters)

    # TODO: Figure out how which ID maps the piece in which we want to move and return the distance
    # TODO: Return the distance to move the piece of the desired location 

    # TODO: For testing -- delete after: 
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
    plt.figure()
    plt.imshow(frame_markers)
    for i in range(len(ids)):
        c = corners[i][0]
        plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label = "id={0}".format(ids[i]))
    plt.legend()
    plt.show()


