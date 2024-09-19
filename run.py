from random import randint

scores = {"player1": 0, "computer": 0}

class Board:
    """
    This is the main board. This class sets the board size, number of ships, 
    and player1's name. It allows the player to play against the computer. 
    
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print("".join(row))


    def new_game(self):
        """
        Start a new game. Sets the board size and number of ships, resets the scores and initialises the boards.
        """
        size = 10
        num_ships = 5
        scores["player1"] = 0
        scores["computer"] = 0
        print("_"*35)
        print("Welcome to my WORLD OF BATTLES!!")
        print(f"Board size {size}, Number of ships: {num_ships}")
        print("Top left corner is row: 0, col: 0")
        print("_"*35)
        player1_name = input("Please insert your name:\n")
        print("_"*35)


        self.print()


    
    
board = Board(10, 2, 'sean', 'hard')
board.new_game()