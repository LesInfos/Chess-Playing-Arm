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

stockfish = Stockfish(parameters={"Threads": 2, "Minimum Thinking Time": 20})

def find_best_move(side, moves, detected_move):
    if side == 'W':
        print("Detected Move: " + detected_move)
        human_input = input('Press Y if detected_move is correct: ')
        if human_input == "Y":
            my_move = detected_move
        else:
            my_move = input('Input your actual move: ')
        processed_move = my_move.strip()
        moves.append(processed_move)
        stockfish.set_position(moves)
        engine_move = stockfish.get_best_move()
        moves.append(engine_move)
        print("Robot move: " + engine_move)
    else:
        stockfish.set_position(moves)
        engine_move = stockfish.get_best_move()
        moves.append(engine_move)
        my_move = input('My move: ')
        processed_move = my_move.strip()
        moves.append(processed_move)
    return engine_move
