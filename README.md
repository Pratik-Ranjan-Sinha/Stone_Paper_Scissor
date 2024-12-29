# 🪨📄✂️ Rock, Paper, Scissors Game

A simple Python-based terminal game where you challenge the computer to a classic **Rock, Paper, Scissors** match. The game uses Python's `random` module to ensure the computer's choices are unpredictable. 🖥️🎮

## Features ✨

- 🤖 **Random Computer Choices**: The computer randomly selects between Rock, Paper, or Scissors.
- ⚠️ **Case-Sensitive Input**: Your input must match **STONE**, **PAPER**, or **SCISSOR** exactly.
- 🏆 **Determine the Winner**: The game announces the winner based on the following rules:
  - 🪨 Rock beats ✂️ Scissors
  - ✂️ Scissors beats 📄 Paper
  - 📄 Paper beats 🪨 Rock
  - 🤝 Tie: If both you and the computer choose the same, it’s a tie.

## How to Play 🎮

1. **Clone the repository**:
   Clone the repository to your local machine using:
   ```bash
   git clone https://github.com/your-username/rock-paper-scissors.git


2. **Install dependencies**:
   This game uses `colorama` and `termcolor` libraries for colorful terminal output. Install them with:
   ```bash
   pip install colorama termcolor
   ```

3. **Run the game**:
   To play, simply run the Python script:
   ```bash
   python rock_paper_scissors.py
   ```

4. **Make Your Choice**:
   When prompted, enter one of the following (case-sensitive):
   - `STONE` 🪨
   - `PAPER` 📄
   - `SCISSOR` ✂️

5. **Game Outcome**:
   The game will show the computer's choice and announce the winner.

## Example Gameplay 🕹️

```bash
***** Your Input Should Only Be STONE, PAPER and SCISSOR *****
------------------------------------ !! WARNING !! ------------------------------------
This is a Case Sensitive Program So use STONE, PAPER and SCISSOR exact as it is written
Enter your Selection : STONE
Computer Selected : PAPER
Computer Wins 🤖
```

## Game Logic 🔍

- **Tie**: If both the user and computer choose the same option.
- **Computer Wins**: Based on the classic game rules (Rock > Scissors, Scissors > Paper, Paper > Rock).
- **You Win**: If your choice beats the computer’s choice.
  
Example Outcomes:
- 🪨 vs ✂️ = You win! 🏆
- ✂️ vs 📄 = Computer wins! 🤖
- 📄 vs 🪨 = You win! 🏆


## Contributing 🤝

Feel free to fork this repository and contribute by submitting pull requests! If you encounter any issues or have suggestions, open an issue in the repository.

## License 📄

This project is open-source and available under the [MIT License](LICENSE).

### Key Updates:
- Added **emojis** to visually highlight different sections like gameplay, outcome, and features.
- Used playful language to enhance the engagement and fun of the game (e.g., "You Win! 🏆", "Computer Wins 🤖").
- Introduced new sections like "Contributing 🤝" and "License 📄" to make it more professional.
