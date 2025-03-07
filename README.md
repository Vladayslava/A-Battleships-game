# A-BUTTLESHIPS-GAME

Battleship is an exciting game that brings the classic naval battle experience to your screen. This project aims to provide a fun and strategic gaming experience for anyone who loves a good challenge. By combining the traditional elements of the Battleship game with modern features, Battleship offers a fresh and engaging way to play.

This game is perfect for anyone who enjoys strategy games, from kids to adults. Whether you're a casual player looking for some fun or a serious gamer seeking a new challenge, Battleship has something for you. It's a great way to improve your strategic thinking and enjoy a modern twist on a classic game.

![Mockup](images/Responsive.jpg)

## How to Play
Battleship Showdown is a turn-based game where you and the computer take turns trying to sink each other's ships on a hidden grid. Each player has a grid with ships randomly placed.
On your turn, enter the row and column number where you want to shoot.
If you hit a ship, the cell will be marked with an 'X'.
If you miss, the cell will be marked with an 'O'.
The computer will also take its turn to guess and shoot on your grid.
The game continues until all ships of one player are sunk.
The first player to sink all of the opponent's ships wins the game. 

### Symbols Used:
 + . - Empty water
 + @ - Ship (hidden from the opponent)
 + X - Hit
 + O - Miss


## Features
### Existing Features
  + Player Grid and Computer Grid
    +  Both players, the user and the computer, have their own grids. Ships are placed randomly on these grids at the start of the game. Ships are not visible on the computer grid for the user to play fair
    ![Player Grid and Computer Grid](images/grid.jpg)
  + Game against the computer
    + The player is prompted to choose a row and a column of the computer's grid where they want to aim. Then it is displayed on the screen whether the player hit a ship or missed, as well as the computer's random choice and whether it hit a ship or not. At the end it shows the score of the player and the computer.
    ![Output of the choice of coordinates of the player and the computer and their score](images/score.jpg)
  + Player input validation
    + An input is considered an error if:
      * the player has already chosen this spot for battle
      * the number is outside the grid
      * any symbols or words were entered
      * enter is pressed without entering a number
      ![Player input validation](images/validation.jpg)
  + Future Features
    + Allows the user to select the grid size and number of ships
    + Have ships larger than 1x1
### Data Model
I decided to use a Battleship class as my model. The game creates two grids, one for the player and one for the computer.

The Battleship class stores the board size, the number of ships, the position of the ships, the guesses against each board, and details such as the number of hits for both the player and the computer, as well as the moves made by both.

The class also has methods to help play the game, such as:
  + create_grid - to initialize a grid of specified size.
  + random_place - to place ships randomly on the grid.
  + display_grid - to print out the current state of a grid.
  + get_random_move - to generate a random move within the grid.
  + validate_grid_input - to ensure the user's input is within the grid's bounds.
  + validate_answer_input - to ensure the user's answer is either 'yes' or 'no'.
  + new_game - to run all the program functions and manage the game's logic.
  + play - to start and restart the game loop.
## Testing

Please refer to the [TESTING.md](TESTING.md) file for all test-related documentation.

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
  + Steps for deployment:
    + Fork or clone this repository
    + Create a new Heroku app
    + Set the buildbacks to Python and NodeJS in that order
    + Link the Heroku app to the repository
    + Click on Deploy

## Credits

  + Code Institute for the deployment terminal 
