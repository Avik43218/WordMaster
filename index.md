# WordMaster

**WordMaster** is an interactive web-based word guessing game built using Flask. It challenges players with 10 thrilling rounds of word deduction using logic, hints, and careful guessing.

---

## Table of Contents

- [Features](#features)
- [Gameplay](#gameplay)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [License](#license)

---

## Features

- 10-round gameplay with session tracking
- Difficulty level selection (affects allowed guesses)
- Dynamic letter reveal logic
- Intelligent guess validation and pattern detection
- Styled, responsive UI with color-coded feedback
- Server-side session handling
- Real-time messaging and hint display

---

## Gameplay

1. Start the game and select a difficulty.
2. Use hints to guess the hidden word one guess at a time.
3. Earn points for correct guesses.
4. The word is progressively revealed as guesses are made.
5. Game ends after 10 rounds or all attempts are used.

---

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Jinja2 templating
- **Data**: Word list files (.txt, .dat), session-based storage
- **Deployment**: Render
- **UX**: JavaScript enhancements, dynamic message coloring

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/avik43218/WordMaster.git
   cd WordMaster
   ```
   
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Run the Application**
   ```bash
   python backend.py
   ```
   
4. Open your browser at http://localhost:5000/ to start the game.

---

## How it Works 

- On startup, words are chosen randomly from a curated .dat list.

- Hints guide the player to guess the word within a limited number of attempts.

- The word is progressively revealed based on character matches.

- Invalid guesses or spammy patterns are detected and discouraged.

- Sessions manage game progress and score per user.

---

## License 

This project is licensed under the MIT License.
See [LICENSE](./LICENSE/) for more information.

---

**Created with passion and wordy wisdom — WordMaster.**
