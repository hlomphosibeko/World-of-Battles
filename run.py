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


    def present_board():
        """
        Chooses random row and random column to position the ship.
        """
        x = random_point(10)
        y = random_point(10)
        board.add_ship(x, y)

    def revelling(computer_board, player1_board):
        """
        Playing the game.
        """
        for i in range(10):
            print(f"{player1_board.name}'s Board")
            player1_board.print()
            print(f"{computer_board.name}'s Board")
            computer_board.print()
            results = make_guess(computer_board)
            print(f"{player1_board.name} guessed: {computer_board.guesses[-1]}")
            print(f"{player1_board.name} {results}ed!!!")
            if results == "Hit":
                scores["player1"] = scores["player1"]+1
            answer = make_guess(player1_board)
            print(f"{computer_board.name} guessed: {player1_board.guesses[-1]}")
            print(f"{computer_board.name} {answer}ed!!!")

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

        player1_board = Board(size, num_ships, player1_name, type="player1")
        computer_board = Board(size, num_ships, player1_name, type="computer")

        for _ in range(num_ships):
            present_board(player1_board)
            present_board(computer_board)
        play_game(computer_board, player1_board)

        self.print()


    
    
board = Board(10, 2, 'sean', 'hard')
board.new_game()