from picamera import PiCamera
from time import sleep
from controls import * 
from vision import *
import numpy as np
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from stockfish import Stockfish
from stocky import *
import chessboard as bby

moves = []
camera = PiCamera()
camera.resolution = (1944, 1944)
board = bby.Board()
prevboard = bby.Board()

def main(): 
    side = input('Input the side you wish to play -- B or W: ')
    processed_side = side.strip() 
    print("Got: " + processed_side)
    if (processed_side != "B" and processed_side != "W"):
        print(processed_side == "W")
        print("Incorrect Side Selection")
        return
        
    while True:
        print("Capturing from camera")
        capture_board_state(camera)
        distance_to_move = process_board_state(prevboard)
        input("press Enter when you have finished making your move")
        print("Capturing from camera")
        capture_board_state(camera)
        distance_to_move2 = process_board_state(board)
        move = board.detect_move(prevboard)
        print("Calculating best move")
        robot_move = find_best_move(processed_side, moves, move)
        input("press Enter when ready to go to next move")

if __name__ == "__main__":
    main()
