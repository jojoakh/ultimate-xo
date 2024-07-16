# Ultimate xo 

## A Tic Tac Toe Game

> This is a python tic-tac-toe game which is played between two people, a player can choose to player with another player or play with the computer. One player plays 'X' and the other player plays 'O', the players take turns in placing their marks on a grid of four by four cells. If a player gets four marks in a row horizontally, vertically, or diagonally, the player wins the game.

### **[Live link](https://ultimate-xo-4e6620460ba8.herokuapp.com/)**

# Flowchart

To create the process of this project i used 
[Lucid chart](https://lucid.app/documents#/templates?folder_id=home).

Below is the flowchart of this project, it shows the entire design and concept of the program.

![Lucid Flow Chart](documentation/flowchart.png)

## Features

### Existing Features

### **User Flow**

- **Welcome Message**
    - Upon running the application the user is greeted with a welcome message, and options to select from.
    - I used [ASCII Art](https://www.asciiart.eu/) to create the welcome message.

![screenshot](documentation/screenshot-welcome-message.png)

- **Rules**
    - When the user selects option 1 the rules appears.

![screenshot](documentation/screenshot-rules.png)

- If the user selects a number outside 1, 2, or 3 it returns an invalid message with the opportunity to pick again.

![screenshot](documentation/screenshot-invalid-choice.png)

- **Start Game**

    ***Game mode***
    - When the user selects option 2, the game mode appears for the user to either select 2 players or play with the computer.

![screenshot](documentation/screenshot-game-mode.png)

- When the first option is selected, which is 2 players, it prompts entering of username for player 1 and player 2.
- When the second option is selected, which is play with computer, the user is asked to enter a username.

![screenshot](documentation/screenshot-username.png)
![screenshot](documentation/screenshot-computer.png)

- Username validation

![screenshot](documentation/screenshot-username-validation.png)

- Display the board to begin the game

![screenshot](documentation/screenshot-board.png)

- Input validation and error checking.
    - User must enter numbers between 1 to 16.
    - User must enter only numbers.

![screenshot](documentation/screenshot-invalid-input.png)

- User can not select already occupied cell.

![screenshot](documentation/screenshot-occupied-cell.png)










