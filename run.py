import random

rows = 5
columns = 6

class Board:
    """
    This is the main board. This class sets the number of ships, 
    it allows the player to play against the computer. 
    
    """
    def __init__(self, size, board, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.type = type
        self.guesses = []
        self.ships = []



    def random_pick():
        pass   

    def play_again():
        pass
    


    play_again()

