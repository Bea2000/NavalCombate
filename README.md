# NavalCombat 🚢

## Project Overview 🕵️

**NavalCombat** is a naval combat game developed in Python for the terminal. It allows players to battle on a grid-based map, using both regular and special bombs (X, cross, and diamond) to attack their opponents. The game also features a ranking system to track player scores, and players can surrender or exit the game at any time. This project was developed during the second semester of 2020 as part of a coursework for a second-year Civil Engineering student at the **Pontificia Universidad Católica de Chile**.

### Features:

- Start a new naval battle with customizable board size.
- Bomb types: Regular and special (X, cross, and diamond-shaped).
- View and store high scores in the ranking system.
- Simple and intuitive menu navigation.
- Handles input errors gracefully, including options for retrying invalid inputs.

## Game Structure 🎮

The game offers two main sections:

1. **Main Menu**:
   - Start a new game.
   - View the ranking of scores.
   - Exit the program.
   
2. **Game Menu**:
   - View the current board.
   - Choose between regular or special bombs for attacks.
   - Check your current ranking.
   - Surrender or exit the game.

### Special Bombs:

- **X Bomb**: Attacks all cells in the shape of an "X" from the target location.
- **Cross Bomb**: Attacks all cells in a cross pattern (vertical and horizontal) from the target location.
- **Diamond Bomb**: Attacks cells in a diamond pattern centered on the target.

## How to Run the Program 💻

To run the game, follow these steps:

1. Clone the repository or download the project files:

```bash
   git clone https://github.com/your-repo/dcnavalcombat.git
   cd dcnavalcombat
```

2. Ensure you have Python installed on your system. The game was developed using Python 3.x.
3. Run the game using the following command in your terminal:

```bash
    python3 main.py
```

## Required Files:

Make sure the following files are in the same directory as main.py:

- **menu_inicio.py**: Handles the main menu operations.
- **bombas_especiales.py**: Defines the effects of the special bombs.
- **parametros.py**: Contains game parameters such as bomb radius and number of ships.
- **tablero.py**: Contains functions to display the game board.
- **puntajes.txt**: Stores player scores.

## Example Execution 🕹️

Upon running the program, you'll see the following terminal output:

```bash
*** Main Menu ***

[0] Start a New Game
[1] View Score Ranking
[2] Exit

Select an option: 0
```

- New Game Flow:

After selecting to start a new game, the player will be asked to enter a nickname:

```bash
    Enter a nickname: Bea2
The nickname must have more than 5 characters and only contain letters and numbers.

[0] Go Back
[1] Return to Main Menu

Select an option: 0
```

Upon successful input of a nickname:

```bash
    Enter a nickname: Bea2000
    Enter the board dimensions (RowsxColumns): 4x4
```

- In-Game Menu:

The game displays the initial board and provides several options for the player:

```bash
- - Game Menu - -

      A B C D
    ┌─────────┐
  0 │ ■ ■ ■ ■ │
  1 │ ■ ■ ■ ■ │
  2 │ ■ ■ ■ ■ │
  3 │ ■ ■ ■ ■ │
    ───────────
  0 │ ■ ■ B ■ │
  1 │ ■ ■ ■ ■ │
  2 │ ■ B ■ ■ │
  3 │ ■ B ■ ■ │
    └─────────┘
      A B C D

[0] Surrender
[1] Launch a Bomb
[2] Exit the Program

Enter your choice: 1
```

After choosing to launch a bomb, you will select the bomb type:

```bash
[0] Regular Bomb
[1] Special Bomb

Select bomb type: 1
[0] Cross Bomb
[1] X Bomb
[2] Diamond Bomb

Select an option: 0
```

You then input the attack coordinates:

```bash
Enter attack coordinates (ColumnRow): B2
```

The board updates to reflect the attack's result.

Expected Results :trophy:
Players will navigate through menus, input valid attack coordinates, and choose bomb types. The goal is to sink all opponent ships by strategically using different bomb types. The game concludes when either the player or the opponent wins, and the player's score is saved to the ranking list.

Example of game board after an attack:

```bash
      A B C D
    ┌─────────┐
  0 │ ■ ■ ■ ■ │
  1 │ ■ ■ X ■ │
  2 │ ■ ■ X ■ │
  3 │ ■ ■ X ■ │
    ───────────
  0 │ ■ ■ B ■ │
  1 │ ■ ■ ■ ■ │
  2 │ ■ B ■ ■ │
  3 │ ■ B ■ ■ │
    └─────────┘
      A B C D
```

## Score Ranking System 🏆

Player scores are stored in a text file (puntajes.txt). After each game, players can view the ranking and see where they stand compared to others.

## Additional Notes 📝

- Error Handling: The game gracefully handles input errors such as invalid nicknames, incorrect bomb choices, and out-of-bounds coordinates.
- Assumptions: All inputs are sanitized, and only alphanumeric characters are allowed in player nicknames.
