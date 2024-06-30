import random

"""
BATTLESHIPS
How it will work:
There will be 4 ships placed on a 5x5 grid, randomly located around.
You can select row and column to indicate where to shoot.
Every hit or miss will be shown on the grid.
If all ships are found faster than your opponent, you win.
 otherwise you will lose

 Designation:
 '.' = empty space
 'X' = ship hit by bullet
 'O' = miss because it didn't hit the ship.
 '@' = the ship that is yours
"""
class BattleshipGame:

    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.player_board = [['O' for x in range(grid_size)] for y in range(grid_size)]
        self.computer_board = [['O' for x in range(grid_size)] for y in range(grid_size)]
        self.computer_ships = []
        self.player_ships = []
        self.player_hits = 0
        self.computer_hits = 0
        self.place_ships(self.player_board)
        self.place_ships(self.computer_board)

    def place_ships(self, board):
        ships_placed = 0
        while ships_placed < 4:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if board[x][y]=='O'
                board[x][y]='X'
                if board is self.player_board:
                    self.player_ships.append((x, y))
                else:
                    self.computer_ships.append((x, y))
                ships_placed += 1



