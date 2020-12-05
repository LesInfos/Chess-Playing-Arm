class Board:
    def __init__(self):
        self.A1 = None
        self.A2 = None
        self.A3 = None
        self.A4 = None
        self.A5 = None
        self.A6 = None
        self.A7 = None
        self.A8 = None
        
        self.B1 = None
        self.B2 = None
        self.B3 = None
        self.B4 = None
        self.B5 = None
        self.B6 = None
        self.B7 = None
        self.B8 = None
        
        self.C1 = None
        self.C2 = None
        self.C3 = None
        self.C4 = None
        self.C5 = None
        self.C6 = None
        self.C7 = None
        self.C8 = None
        
        self.E1 = None
        self.E2 = None
        self.E3 = None
        self.E4 = None
        self.E5 = None
        self.E6 = None
        self.E7 = None
        self.E8 = None
        
        self.F1 = None
        self.F2 = None
        self.F3 = None
        self.F4 = None
        self.F5 = None
        self.F6 = None
        self.F7 = None
        self.F8 = None
        
        self.G1 = None
        self.G2 = None
        self.G3 = None
        self.G4 = None
        self.G5 = None
        self.G6 = None
        self.G7 = None
        self.G8 = None
        
        self.H1 = None
        self.H2 = None
        self.H3 = None
        self.H4 = None
        self.H5 = None
        self.H6 = None
        self.H7 = None
        self.H8 = None
        
def insert_piece(Board, x, y, type)
    x_options = {
    "A": [181, 400],
    "B": [401, 590],
    "C": [591, 780],
    "D": [781, 970],
    "E": [971, 1160],
    "F": [1161, 1350],
    "G": [1351, 1543],
    "H": [1544, 1777]
    }
    for key, value in x_options.items():
        if value[0] <= x <= value[1]:
            return helper_y(key, y, type)
    print("Piece outside of boundaries")
    return False

def helper_y(Board, keyer, y, type):
    y_options = {
    "1": [174, 414],
    "2": [415, 611],
    "3": [612, 795],
    "4": [796, 1000],
    "5": [1001, 1168],
    "6": [1169, 1360],
    "7": [1361, 1554],
    "8": [1555, 1777]
    }
    for key, value in y_options.items():
        if value[0] <= y <= value[1]:
            return place(Board, keyer, key, type)
    print("Piece outside of boundaries")
    return False

def place(Board, letter, num, type):
    (Board.A1 = type) if ((letter == "A") and (num == "1"))
    (Board.A2 = type) if ((letter == "A") and (num == "2"))
    (Board.A3 = type) if ((letter == "A") and (num == "3"))
    (Board.A4 = type) if ((letter == "A") and (num == "4"))
    (Board.A5 = type) if ((letter == "A") and (num == "5"))
    (Board.A6 = type) if ((letter == "A") and (num == "6"))
    (Board.A7 = type) if ((letter == "A") and (num == "7"))
    (Board.A8 = type) if ((letter == "A") and (num == "8"))
    (Board.B1 = type) if ((letter == "B") and (num == "1"))
    (Board.B2 = type) if ((letter == "B") and (num == "2"))
    (Board.B3 = type) if ((letter == "B") and (num == "3"))
    (Board.B4 = type) if ((letter == "B") and (num == "4"))
    (Board.B5 = type) if ((letter == "B") and (num == "5"))
    (Board.B6 = type) if ((letter == "B") and (num == "6"))
    (Board.B7 = type) if ((letter == "B") and (num == "7"))
    (Board.B8 = type) if ((letter == "B") and (num == "8"))
    (Board.C1 = type) if ((letter == "C") and (num == "1"))
    (Board.C2 = type) if ((letter == "C") and (num == "2"))
    (Board.C3 = type) if ((letter == "C") and (num == "3"))
    (Board.C4 = type) if ((letter == "C") and (num == "4"))
    (Board.C5 = type) if ((letter == "C") and (num == "5"))
    (Board.C6 = type) if ((letter == "C") and (num == "6"))
    (Board.C7 = type) if ((letter == "C") and (num == "7"))
    (Board.C8 = type) if ((letter == "C") and (num == "8"))
    (Board.D1 = type) if ((letter == "D") and (num == "1"))
    (Board.D2 = type) if ((letter == "D") and (num == "2"))
    (Board.D3 = type) if ((letter == "D") and (num == "3"))
    (Board.D4 = type) if ((letter == "D") and (num == "4"))
    (Board.D5 = type) if ((letter == "D") and (num == "5"))
    (Board.D6 = type) if ((letter == "D") and (num == "6"))
    (Board.D7 = type) if ((letter == "D") and (num == "7"))
    (Board.D8 = type) if ((letter == "D") and (num == "8"))
    (Board.E1 = type) if ((letter == "E") and (num == "1"))
    (Board.E2 = type) if ((letter == "E") and (num == "2"))
    (Board.E3 = type) if ((letter == "E") and (num == "3"))
    (Board.E4 = type) if ((letter == "E") and (num == "4"))
    (Board.E5 = type) if ((letter == "E") and (num == "5"))
    (Board.E6 = type) if ((letter == "E") and (num == "6"))
    (Board.E7 = type) if ((letter == "E") and (num == "7"))
    (Board.E8 = type) if ((letter == "E") and (num == "8"))
    (Board.F1 = type) if ((letter == "F") and (num == "1"))
    (Board.F2 = type) if ((letter == "F") and (num == "2"))
    (Board.F3 = type) if ((letter == "F") and (num == "3"))
    (Board.F4 = type) if ((letter == "F") and (num == "4"))
    (Board.F5 = type) if ((letter == "F") and (num == "5"))
    (Board.F6 = type) if ((letter == "F") and (num == "6"))
    (Board.F7 = type) if ((letter == "F") and (num == "7"))
    (Board.F8 = type) if ((letter == "F") and (num == "8"))
    (Board.G1 = type) if ((letter == "G") and (num == "1"))
    (Board.G2 = type) if ((letter == "G") and (num == "2"))
    (Board.G3 = type) if ((letter == "G") and (num == "3"))
    (Board.G4 = type) if ((letter == "G") and (num == "4"))
    (Board.G5 = type) if ((letter == "G") and (num == "5"))
    (Board.G6 = type) if ((letter == "G") and (num == "6"))
    (Board.G7 = type) if ((letter == "G") and (num == "7"))
    (Board.G8 = type) if ((letter == "G") and (num == "8"))
    (Board.H1 = type) if ((letter == "H") and (num == "1"))
    (Board.H2 = type) if ((letter == "H") and (num == "2"))
    (Board.H3 = type) if ((letter == "H") and (num == "3"))
    (Board.H4 = type) if ((letter == "H") and (num == "4"))
    (Board.H5 = type) if ((letter == "H") and (num == "5"))
    (Board.H6 = type) if ((letter == "H") and (num == "6"))
    (Board.H7 = type) if ((letter == "H") and (num == "7"))
    (Board.H8 = type) if ((letter == "H") and (num == "8"))
    return True
