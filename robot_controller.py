import pi_servo_hat
import time

chessboard_binding_dict = {
    "d7": [65,41],
    "d5": [75,32],
    "e7": [66,34],
    "e5": [77,24]
}

def makemove(stockfish_move):
    origin = stockfish_move[0:2]
    destin = stockfish_move[2:4]

    test = pi_servo_hat.PiServoHat()
    test.restart()
    input("Prepping servos. Press Enter to continue...")
    test.move_servo_position(0, 0)
    test.move_servo_position(1, 0)
    test.move_servo_position(2, 0)
    test.move_servo_position(3, 120)
    x0 = chessboard_binding_dict[origin][0]
    x1 = chessboard_binding_dict[origin][1]
    time.sleep(1)

    for i in range(int(x0)):
        test.move_servo_position(0, i)
        time.sleep(0.02)
    for i in range(int(x1)):
        test.move_servo_position(1, i)
        time.sleep(0.02)
    time.sleep(2)

    test.move_servo_position(2, 130)
    time.sleep(1)

    for i in range (120, 16, -1):
        test.move_servo_position(3,i)
        time.sleep(0.001)
    time.sleep(2)
    test.move_servo_position(2, 0)
    time.sleep(1)

    for i in range(int(x0), 0, -1):
        test.move_servo_position(0, i)
        time.sleep(0.02)
    for i in range(int(x1), 0, -1):
        test.move_servo_position(1, i)
        time.sleep(0.02)
    x0 = chessboard_binding_dict[destin][0]
    x1 = chessboard_binding_dict[destin][1]
    for i in range(int(x0)):
        test.move_servo_position(0, i)
        time.sleep(0.02)
    for i in range(int(x1)):
        test.move_servo_position(1, i)
        time.sleep(0.02)
    time.sleep(2)

    test.move_servo_position(2, 130)
    time.sleep(1)
    for i in range(16, 120):
        test.move_servo_position(3,i)
        time.sleep(0.001)
    time.sleep(2)
    test.move_servo_position(2, 0)
    time.sleep(1)

    print("Cleaning up")
    test.move_servo_position(0, 0)
    test.move_servo_position(1, 0)
    test.move_servo_position(2, 0)
    test.move_servo_position(3, 120)
    time.sleep(1)
    test.restart()
    print("Move from " + origin + " to " + destin +" complete.")
