from picamera import PiCamera
from time import sleep
import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import chessboard as bby

def capture_board_state(camera): 
    camera.start_preview()
    for k in range(5):
        print("Capturing image " + str(k))
        camera.capture('/home/pi/Desktop/106a_project/board' + str(k) + '.jpg')
        sleep(1)
    camera.stop_preview()


def process_board_state(board, aruco_dict, parameters): 
    piecedict = ["BQ", "BK", "BB", "BR", "BN", "BP"]
    for k in range(5):
        print("Pass number " + str(k))
        frame = cv2.imread('/home/pi/Desktop/106a_project/board' + str(k) + '.jpg')
        corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
        for i in range(len(ids)):
            c = corners[i][0]
            bby.insert_piece(board, c[:, 0].mean(), c[:, 1].mean(), piecedict[ids[i][0]])
    while True:
        board.retrieve()
        human_input = input("Correct? Type Y to confirm: ")
        if human_input == "Y":
            return None
        else:
            x = input("Board edit: letter...")
            y = input("Board edit: num...")
            type = input("Board edit: piece type...")
            board.edit(x, y, type)
    return None

