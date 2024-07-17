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
        self.random_place(self.player_grid)
        self.random_place(self.computer_grid)

    def create_grid(self):
        grid = []
        for _ in range(GRID_SIZE):
            row = []
            for _ in range(GRID_SIZE):
                row.append('.')
            grid.append(row)
        return grid

    def random_place(self, grid):
        ships_placed = 0
        while ships_placed < NUM_SHIPS:
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            if grid[row][col] == '.':
                grid[row][col] = '@'
                ships_placed += 1

    def display_grid(self, grid):
        for row in grid:
            print(' '.join(row))
        print()

    def get_random_move(self):
        return random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)

    def validate_input(self, prompt, existing_moves):
        while True:
            try:
                value = int(input(prompt))
                if 0 <= value < GRID_SIZE:
                    return value
                else:
                    print(f"Please enter a number between 0 and {GRID_SIZE - 1}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def new_game(self):
        """
        Run all program functions
        """

        print("Welcome to BATTLESHIPS game!")
        print(f"There will be {NUM_SHIPS} ships placed on a {GRID_SIZE} grid, randomly located around.")
        print("Top left corner is row: 0, col: 0")
        print("You can select row and column to indicate where to shoot.")
        print("If all ships are found faster than your opponent, you win, otherwise you will lose\n")

        while self.player_hits < NUM_SHIPS and self.computer_hits < NUM_SHIPS:
            print("Your grid:")
            self.display_grid(self.player_grid)

            print("Computer grid:")
            hidden_grid = []
            for row in self.computer_grid:
                hidden_ships = []
                for cell in row:
                    if cell == '@':
                        hidden_ships.append('.')
                    else:
                        hidden_ships.append(cell)
                hidden_grid.append(hidden_ships)
            self.display_grid(hidden_grid)

            player_row = self.validate_input(f"Enter row between 0 and {GRID_SIZE - 1}: \n", self.player_moves)
            player_col = self.validate_input(f"Enter col between 0 and {GRID_SIZE - 1}: \n", self.player_moves)

            if (player_row, player_col) in self.player_moves:
                print("this coordinate. Try again.")
                continue
            else:
                self.player_moves.append((player_row, player_col))

            if self.computer_grid[player_row][player_col] == '@':
                print('Player got a hit!')
                self.computer_grid[player_row][player_col] = 'X'
                self.player_hits += 1
            else:
                print('Player missed this time')
                self.computer_grid[player_row][player_col] = 'O'

            while True:
                computer_row, computer_col = self.get_random_move()
                if (computer_row, computer_col) not in self.computer_moves:
                    self.computer_moves.append((computer_row, computer_col))
                    break

            print(f'Computer guessed: ({computer_row},{computer_col})')

            if self.player_grid[computer_row][computer_col] == '@':
                print('Computer got a hit!')
                self.player_grid[computer_row][computer_col] = 'X'
                self.computer_hits += 1
            else:
                print('Computer missed this time')
                self.player_grid[computer_row][computer_col] = 'O'

            print(f'Your hits: {self.player_hits}. Computer hits: {self.computer_hits}')

        if self.player_hits == NUM_SHIPS:
            print('Congratulations! You won!')
        else:
            print('The computer won! Try again!')

if __name__ == "__main__":
    game = Battleship()
    game.new_game()
