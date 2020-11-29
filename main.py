from stockfish_algo import * 
from picamera import PiCamera
from time import sleep
from controls import * 
from vision import * 
import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from stockfish import Stockfish

# Setup the aruco tag: 
aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
parameters =  aruco.DetectorParameters_create() 

# Setup stockfish. The player is always White in this case. To keep track of the moves, we add the moves to a list 
stockfish = Stockfish(parameters={"Threads": 2, "Minimum Thinking Time": 20})
moves = []
moves.append('e2e4') # Lets always play the classic e2e4 move as the first move as White

def main(): 
    while True: 
        move_arm_away()
        sleep(30)                          # Change this value to see how long we should wait 
        capture_board_state()
        robot_move = find_best_move(moves)
        distance_to_move = process_board_state(robot_move)
        move_arm(robot_move, distance_to_move) # Maybe pass in ID? 
        sleep(30)                          # Change this value to see how long we should wait 

def find_best_move():
    my_move = input('My move: ')                 # Get the player move --> The format should be e2e4 (meaning move pawn from e2 to e4)
    processed_move = my_move.strip()            # Gets rid of the player's leading/trailing white space
    moves.append(processed_move)                # Append to all moves played 
    stockfish.set_position(moves)               # Set the board position according to the moves played
    engine_move = stockfish.get_best_move()     # Stockfish finds the best move 
    moves.append(engine_move)                   # Appends the move and then loops back for the player's next move
    return engine_move                          # Returns the move the robot should play 

        