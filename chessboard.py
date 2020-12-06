class Board:
    def __init__(self):
        self.A1 = ". "
        self.A2 = ". "
        self.A3 = ". "
        self.A4 = ". "
        self.A5 = ". "
        self.A6 = ". "
        self.A7 = ". "
        self.A8 = ". "
        
        self.B1 = ". "
        self.B2 = ". "
        self.B3 = ". "
        self.B4 = ". "
        self.B5 = ". "
        self.B6 = ". "
        self.B7 = ". "
        self.B8 = ". "
        
        self.C1 = ". "
        self.C2 = ". "
        self.C3 = ". "
        self.C4 = ". "
        self.C5 = ". "
        self.C6 = ". "
        self.C7 = ". "
        self.C8 = ". "
        
        self.D1 = ". "
        self.D2 = ". "
        self.D3 = ". "
        self.D4 = ". "
        self.D5 = ". "
        self.D6 = ". "
        self.D7 = ". "
        self.D8 = ". "
        
        self.E1 = ". "
        self.E2 = ". "
        self.E3 = ". "
        self.E4 = ". "
        self.E5 = ". "
        self.E6 = ". "
        self.E7 = ". "
        self.E8 = ". "
        
        self.F1 = ". "
        self.F2 = ". "
        self.F3 = ". "
        self.F4 = ". "
        self.F5 = ". "
        self.F6 = ". "
        self.F7 = ". "
        self.F8 = ". "
        
        self.G1 = ". "
        self.G2 = ". "
        self.G3 = ". "
        self.G4 = ". "
        self.G5 = ". "
        self.G6 = ". "
        self.G7 = ". "
        self.G8 = ". "
        
        self.H1 = ". "
        self.H2 = ". "
        self.H3 = ". "
        self.H4 = ". "
        self.H5 = ". "
        self.H6 = ". "
        self.H7 = ". "
        self.H8 = ". "
    def retrieve(self):
        for row in range(8, 0, -1):
            print(" ".join([getattr(self, letter + str(row)) for letter in "ABCDEFGH"]))
    def edit(self, x, y, type):
        return place(self, x, y, type)
    def detect_move(self, prev_board)
        for row in range(1, 9):
            for letter in "ABCDEFGH"
                prev = getattr(prev_board, letter + str(row))
                next = getattr(self, letter + str(row))
                if prev != ". " and next == ". "
                    start = letter.lower() + str(row)
                if next != ". " and prev == ". "
                    end = letter.lower() + str(row)
        return start+end
    
    def reset(self):
        self.A1 = ". "
        self.A2 = ". "
        self.A3 = ". "
        self.A4 = ". "
        self.A5 = ". "
        self.A6 = ". "
        self.A7 = ". "
        self.A8 = ". "
        
        self.B1 = ". "
        self.B2 = ". "
        self.B3 = ". "
        self.B4 = ". "
        self.B5 = ". "
        self.B6 = ". "
        self.B7 = ". "
        self.B8 = ". "
        
        self.C1 = ". "
        self.C2 = ". "
        self.C3 = ". "
        self.C4 = ". "
        self.C5 = ". "
        self.C6 = ". "
        self.C7 = ". "
        self.C8 = ". "
        
        self.D1 = ". "
        self.D2 = ". "
        self.D3 = ". "
        self.D4 = ". "
        self.D5 = ". "
        self.D6 = ". "
        self.D7 = ". "
        self.D8 = ". "
        
        self.E1 = ". "
        self.E2 = ". "
        self.E3 = ". "
        self.E4 = ". "
        self.E5 = ". "
        self.E6 = ". "
        self.E7 = ". "
        self.E8 = ". "
        
        self.F1 = ". "
        self.F2 = ". "
        self.F3 = ". "
        self.F4 = ". "
        self.F5 = ". "
        self.F6 = ". "
        self.F7 = ". "
        self.F8 = ". "
        
        self.G1 = ". "
        self.G2 = ". "
        self.G3 = ". "
        self.G4 = ". "
        self.G5 = ". "
        self.G6 = ". "
        self.G7 = ". "
        self.G8 = ". "
        
        self.H1 = ". "
        self.H2 = ". "
        self.H3 = ". "
        self.H4 = ". "
        self.H5 = ". "
        self.H6 = ". "
        self.H7 = ". "
        self.H8 = ". "
        
def insert_piece(Board, x, y, type):
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
            return helper_y(Board, key, y, type)
    print("Piece outside of boundaries")
    return False

def helper_y(Board, keyer, y, type):
    y_options = {
    "8": [174, 414],
    "7": [415, 611],
    "6": [612, 795],
    "5": [796, 1000],
    "4": [1001, 1168],
    "3": [1169, 1360],
    "2": [1361, 1554],
    "1": [1555, 1777]
    }
    for key, value in y_options.items():
        if value[0] <= y <= value[1]:
            return place(Board, keyer, key, type)
    print("Piece outside of boundaries")
    return False

def place(Board, letter, num, type):
    if ((letter == "A") and (num == "1")):
        Board.A1 = type
    if ((letter == "A") and (num == "2")):
        Board.A2 = type
    if ((letter == "A") and (num == "3")):
        Board.A3 = type
    if ((letter == "A") and (num == "4")):
        Board.A4 = type
    if ((letter == "A") and (num == "5")):
        Board.A5 = type
    if ((letter == "A") and (num == "6")):
        Board.A6 = type
    if ((letter == "A") and (num == "7")):
        Board.A7 = type
    if ((letter == "A") and (num == "8")):
        Board.A8 = type
    if ((letter == "B") and (num == "1")):
        Board.B1 = type
    if ((letter == "B") and (num == "2")):
        Board.B2 = type
    if ((letter == "B") and (num == "3")):
        Board.B3 = type
    if ((letter == "B") and (num == "4")):
        Board.B4 = type
    if ((letter == "B") and (num == "5")):
        Board.B5 = type
    if ((letter == "B") and (num == "6")):
        Board.B6 = type
    if ((letter == "B") and (num == "7")):
        Board.B7 = type
    if ((letter == "B") and (num == "8")):
        Board.B8 = type
    if ((letter == "C") and (num == "1")):
        Board.C1 = type
    if ((letter == "C") and (num == "2")):
        Board.C2 = type
    if ((letter == "C") and (num == "3")):
        Board.C3 = type
    if ((letter == "C") and (num == "4")):
        Board.C4 = type
    if ((letter == "C") and (num == "5")):
        Board.C5 = type
    if ((letter == "C") and (num == "6")):
        Board.C6 = type
    if ((letter == "C") and (num == "7")):
        Board.C7 = type
    if ((letter == "C") and (num == "8")):
        Board.C8 = type
    if ((letter == "D") and (num == "1")):
        Board.D1 = type
    if ((letter == "D") and (num == "2")):
        Board.D2 = type
    if ((letter == "D") and (num == "3")):
        Board.D3 = type
    if ((letter == "D") and (num == "4")):
        Board.D4 = type
    if ((letter == "D") and (num == "5")):
        Board.D5 = type
    if ((letter == "D") and (num == "6")):
        Board.D6 = type
    if ((letter == "D") and (num == "7")):
        Board.D7 = type
    if ((letter == "D") and (num == "8")):
        Board.D8 = type
    if ((letter == "E") and (num == "1")):
        Board.E1 = type
    if ((letter == "E") and (num == "2")):
        Board.E2 = type
    if ((letter == "E") and (num == "3")):
        Board.E3 = type
    if ((letter == "E") and (num == "4")):
        Board.E4 = type
    if ((letter == "E") and (num == "5")):
        Board.E5 = type
    if ((letter == "E") and (num == "6")):
        Board.E6 = type
    if ((letter == "E") and (num == "7")):
        Board.E7 = type
    if ((letter == "E") and (num == "8")):
        Board.E8 = type
    if ((letter == "F") and (num == "1")):
        Board.F1 = type
    if ((letter == "F") and (num == "2")):
        Board.F2 = type
    if ((letter == "F") and (num == "3")):
        Board.F3 = type
    if ((letter == "F") and (num == "4")):
        Board.F4 = type
    if ((letter == "F") and (num == "5")):
        Board.F5 = type
    if ((letter == "F") and (num == "6")):
        Board.F6 = type
    if ((letter == "F") and (num == "7")):
        Board.F7 = type
    if ((letter == "F") and (num == "8")):
        Board.F8 = type
    if ((letter == "G") and (num == "1")):
        Board.G1 = type
    if ((letter == "G") and (num == "2")):
        Board.G2 = type
    if ((letter == "G") and (num == "3")):
        Board.G3 = type
    if ((letter == "G") and (num == "4")):
        Board.G4 = type
    if ((letter == "G") and (num == "5")):
        Board.G5 = type
    if ((letter == "G") and (num == "6")):
        Board.G6 = type
    if ((letter == "G") and (num == "7")):
        Board.G7 = type
    if ((letter == "G") and (num == "8")):
        Board.G8 = type
    if ((letter == "H") and (num == "1")):
        Board.H1 = type
    if ((letter == "H") and (num == "2")):
        Board.H2 = type
    if ((letter == "H") and (num == "3")):
        Board.H3 = type
    if ((letter == "H") and (num == "4")):
        Board.H4 = type
    if ((letter == "H") and (num == "5")):
        Board.H5 = type
    if ((letter == "H") and (num == "6")):
        Board.H6 = type
    if ((letter == "H") and (num == "7")):
        Board.H7 = type
    if ((letter == "H") and (num == "8")):
        Board.H8 = type
    return True
