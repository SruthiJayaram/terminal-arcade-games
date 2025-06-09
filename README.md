# 🕹️ Terminal Arcade Game Suite

Welcome to the **Arcade Game Suite** — a collection of classic terminal-based games in Python where you play against the computer! 🎮

---

## 🎯 What's Inside?

| Game             | Description                          |
|------------------|--------------------------------------|
| `hangman.py`     | Guess the word letter by letter.     |
| `tictactoe.py`   | Classic Tic-Tac-Toe with smart AI.   |
| `guessnumber.py` | Guess the number chosen by the bot.  |
| `rps.py`         | Rock Paper Scissors terminal battle. |

All games are **computer vs user**, written for the terminal, with interactive prompts and replay functionality.

---

## 🚀 Getting Started

### 📁 Clone the Repository

```bash
git clone https://github.com/SruthiJayaram/terminal-arcade-games.git
cd terminal-arcade-games
```

### 🐍 Requirements

- Python 3.6 or higher
- No external dependencies

### ▶️ How to Play

You have two ways to enjoy the games in this Arcade:

🔹 Option 1: Play via the Arcade Menu
Run the main menu and choose your game from the list:

```bash
python arcade.py -n YourName
```

You'll be welcomed and prompted to pick from:
 ```text
    1 = Rock Paper Scissors
    2 = Guess My Number 
    3 = Hangman 
    4 = Tic-Tac-Toe 
    x = Exit 
``` 

🔹 Option 2: Play a Game Individually
You can also launch any game directly from the terminal:

🧠 Hangman
```bash
python hangman.py -n YourName
```

❌⭕ Tic-Tac-Toe
```bash
python tictactoe.py -n YourName
```

🔢 Guess My Number
```bash
python guessnumber.py -n YourName
```

✊✋✌️ Rock Paper Scissors
```bash
python rps.py -n YourName
```

Replace YourName with your name for a personalized experience.

---

## 🧠 Tech Used

- Python 3
- Random module
- argparse for command-line name input
- Minimax algorithm for smart AI in Tic-Tac-Toe

---

## 🙋‍♀️ About Me

I'm Sruthi, a B.Tech student learning web development and building fun beginner projects like this! 😊 Feel free to check out more at https://github.com/SruthiJayaram

---

## 📄 License

This project is for educational purposes and does not include any production-level deployment or UI design.