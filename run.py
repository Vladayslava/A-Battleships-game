import random

GRID_SIZE = 5

NUM_SHIPS = 5


class Battleship:

    def __init__(self):
        self.player_grid = self.create_grid()
        self.computer_grid = self.create_grid()
        self.player_hits = 0
        self.computer_hits = 0
        self.player_moves = []
        self.computer_moves = []

    def create_grid(self):
        return [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


    def place_ships(self, grid):
        ships_placed = 0
        while ships_placed < NUM_SHIPS:
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            if grid[row][col] == '.':
                grid[row][col] = '@'
                ships_placed += 1

    def display_grid(self, grid):
        for row in grid:
            print(''.join(row))
            print()

    def get_random_move(self):
        return random.randint(0, GRID_SIZE - 1),
        random.randint(0, GRID_SIZE - 1)

    def make_move(self, grid, row, col):
        if grid[row][col] == '@':
            grid[row][col] = 'X'
            return True
        elif grid[row][col] == '.':
            grid[row][col] = 'O'
            return False

    def validate_date(self, player_row, player_col):
        try:
            player_row, player_col  = int(player_row), int(player_col)

            if not(0 <= player_row < GRID_SIZE and 0 <= player_col < GRID_SIZE):
                raise InvalidInputError(f'Error: Enter numbers from 0 to {GRID_SIZE - 1}.')


            if [player_row, player_col] in self.player_moves:
                raise InvalidInputError('Error: This location has already been selected. Try again.')

        except ValueError:
            raise InvalidInputError('Error: Enter numbers.')

        self.player_moves.append([player_row,player_col])
        return player_row, player_col


            

    def new_game(self):
        print("Welcome to BATTLESHIPS game!")
        print(f"There will be {NUM_SHIPS} ships placed on a {GRID_SIZE} grid, randomly located around.")
        print("Top left corner is row: 0, col: 0")
        print("You can select row and column to indicate where to shoot.")
        print("If all ships are found faster than your opponent, you win, otherwise you will lose")


    #  Designation:
    #  '.' = empty space
    #  'X' = ship hit by bullet
    #  'O' = miss because it didn't hit the ship.
    #  '@' = the ship that is yours


        place_ships(self.player_grid)
        place_ships(self.computer_grid)

        player_hits = 0
        computer_hits = 0

        while self.player_hits < NUM_SHIPS and computer_hits < NUM_SHIPS:
            print("Your grid:")
            display_grid(player_grid)

            print("Computer grid:")
            display_grid([['.' if cell == '@' else cell in row]for row in computer_grid])

            player_row = int(input(f"Enter row between {0-GRID_SIZE-1}"))
            player_col = int(input(f"Enter col between {0-GRID_SIZE-1}"))

            if computer_grid[player_row][player_col] == '@':
                print('Player got a hit!')
                computer_grid[player_row][player_col] = 'X'
                player_hits += 1
            else:
                print('Player missed this time')
                computer_grid[player_row][player_col] = 'O'

            computer_row, computer_col = get_random_move()
            print(f'Computer guessed:({computer_row},{computer_col})')

            if player_grid[computer_row][computer_col] == '@':
                print('Computer got a hit!')
                player_grid[computer_row][computer_col] = 'X'
                computer_hits += 1
            else:
                print('Computer missed this time')
                player_grid[computer_row][computer_col] = 'O'

            print(f'Your hits:{player_hits}. Computer hits:{computer_hits}')

        if player_hits == NUM_SHIPS:
            print: ('Congratulations! You won!')
        else:
            print: ('The computer won! Try again!')

if __name__ == "__main__":
    game = Battleship()
    game.new_game()
