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
import chessboard as bby

# Setup the aruco tag: 
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters =  aruco.DetectorParameters_create() 

# Setup stockfish. The player is always White in this case. To keep track of the moves, we add the moves to a list 
stockfish = Stockfish(parameters={"Threads": 2, "Minimum Thinking Time": 20})
moves = []

# Setup Camera 
camera = PiCamera()
camera.resolution = (1944, 1944)

board = bby.Board()

def main(): 
    print("Capturing from camera")
    capture_board_state(camera)
    distance_to_move = process_board_state(board, aruco_dict, parameters)
    side = input('Input the side you wish to play -- B or W: ')
    processed_side = side.strip() 
    print("Got: " + processed_side)
    if (processed_side != "B" and processed_side != "W"):
        print(processed_side == "W")
        print("Incorrect Side Selection")
        return
    robot_move = find_best_move(processed_side)
    print("Calculating best move")
    print("Robot's move: " + robot_move)
    print("done")
    
def find_best_move(side):
    if side == 'W':
        my_move = input('My move: ')                 # Get the player move --> The format should be e2e4 (meaning move pawn from e2 to e4)
        processed_move = my_move.strip()            # Gets rid of the player's leading/trailing white space
        moves.append(processed_move)                # Append to all moves played 
        stockfish.set_position(moves)               # Set the board position according to the moves played
        engine_move = stockfish.get_best_move()     # Stockfish finds the best move 
        moves.append(engine_move)                   # Appends the move and then loops back for the player's next move
    else: # Basically flip the order if we are playing as black
        stockfish.set_position(moves)               # TODO: Check if empty array errors
        engine_move = stockfish.get_best_move()    
        moves.append(engine_move)                  
        my_move = input('My move: ')                
        processed_move = my_move.strip()           
        moves.append(processed_move)              
    return engine_move                          # Returns the move the robot should play 

if __name__ == "__main__":
    main()
