import random

GRID_SIZE = 5

NUM_SHIPS = 5

class BattleshipGame:

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


    def create_grid():
        return [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    def place_ships(grid):
        ships_placed = 0
        while ships_placed < NUM_SHIPS:
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            if grid[row][col] == '.':
                grid[row][col] = '@'
                ships_placed += 1

    def display_grid(grid):
        for row in grid:
            print(''.join(row))
            print()

    def get_random_move():
        return random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)

    def make_move(grid, row, col):
        if grid[row][col] = '@':
            grid[row][col] == 'X'
            return True
        elif grid[row][col] = '.': 
            grid[row][col] = 'O'
            return False
        
    def game():
        player_grid = create_grid()
        computer_grid = create_grid()
        place_ships(player_grid)
        place_ships(computer_grid)

        player_hits = 0
        computer_hits = 0

        while player_hits < NUM_SHIPS and computer_hits < NUM_SHIPS:
            print("Your grid:")
            display_grid(player_grid)

            print("Computer grid:")
            display_grid([['.' if cell == '@' for cell in row]for row in computer_grid])

 



