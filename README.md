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

- When game ends the winner is displayed with the option to play again or exit the game.

![screenshot](documentation/screenshot-game-end.png)

- Select yes to replay
- Select no to exit

![screenshot](documentation/screenshot-replay.png)
![screenshot](documentation/screenshot-endgame-message.png)

## Future Features
- Make the computer a more challenging opponent. 
- Make the game more difficult with different levels like (Easy, Medium, Hard) with computer opponent.
- Add different Board Sizes and allow users to choose different board sizes.
- Add a timed mode where players have a limited amount of time to make their move.
- Track and display the history of games played, including wins, losses, and draws.

## Tools & Technologies Used

- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![Python](https://img.shields.io/badge/Python-yellow?logo=python&logoColor=1572B6)](https://en.wikipedia.org/wiki/Python_(programming_language)) Used to create the application.
- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README/TESTING templates.
- [![Heroku](https://img.shields.io/badge/Heroku-purple?logo=heroku&logoColor=000000)](https://dashboard.heroku.com/apps) Used to deploy and host the application.

## Testing

#### Manual Testing

| Test | Result |
|--|--|
|When the programme runs, the welcome message appears| Pass |
|The options to select from apears after the welcome message|Pass|
|Option 1 displays the rules|Pass|
|Option 2 displays the game mode with two options to select from|Pass|
|Option 3 ends the game and a goodbye message is displayed|Pass|
|First option from the game mode display two players|Pass|
|Second option from game mode is the option to play with computer|Pass|
|Ask for username when option 1 or 2 is selected|Pass|
|Check for valid/invalid username|Pass|
|Numbers entered must be between 1 to 16|Pass|
|Occupied cells can not be slected|Pass|
|The winner is announced when the game ends|Pass|
|Options to replay or exit is given when the game ends|Pass|

## Code Validation

### Pep8 Validator

I have used the recommended [Pep8 Validator](https://pep8ci.herokuapp.com/) to validate my code.

| File | screenshot | Notes |
| --- | --- | --- |
| Run.py | ![screenshot](documentation/screenshot-pep8-validation.png) | Pass: No Errors |











