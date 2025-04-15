# WordMaster: A Flask-Based Word Guessing Game

Welcome to **WordMaster**, a dynamic, web-based word guessing game built using **Flask**, **HTML/CSS**, and **Python** — featuring multiple difficulty levels, scoring, hints, and a clean interactive UI.

Test your vocabulary, intuition, and spelling as you try to uncover the hidden word based on a hint. But be careful — you have limited attempts per round!

---

## 🎯 Features

- **Interactive Word Guessing** with live feedback
- **10 Rounds per Game**, increasing difficulty
- **Difficulty Levels**:
  - Recruit (6 tries)
  - Regular (5 tries)
  - Heroic (3 tries)
  - Veteran (2 tries)
- **Hint System** to help users guess intelligently
- **Letter Reveal Mechanism**: reveals parts of the word based on previous guesses
- **Score Tracking** across rounds
- **Responsive UI** styled with custom CSS (rem units)
- **Session Management** using Flask
- **Secure Input Validation** to prevent cheating
- Cleanly structured codebase with separate modules and templates

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/WordMaster.git
cd WordMaster
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the app
```bash
python app.py
```
Then visit: http://127.0.0.1:5000 in your browser.

---

## Folder Structure

WordMaster/
├── app.py
├── backend.py
├── filtered_words.dat
├── requirements.txt
├── Procfile
├── /templates
│   ├── start.html
│   ├── setup.html
│   └── game.html
├── /static
│   └── CSS & assets

---

## Game Logic

- Players get one word per round.

- They are shown a hint and a masked version of the word.

- Guessing the full word correctly grants 10 points.

- Incorrect guesses reduce the number of available attempts.

- After 10 rounds, the game ends and the final score is shown.

---

## Security and Input Validation

- All inputs are sanitized and validated to prevent spam guesses like the full alphabet.

- Sessions are managed using Flask’s secure session system.

- Secrets like the SECRET_KEY are loaded through environment variables.

---

## Deployment Ready

This app is fully compatible with platforms like Render, Railway, and Heroku.

Be sure to:

Include a requirements.txt with Flask and gunicorn

Use a Procfile with:

web: gunicorn app:app

---

## Live Demo

Coming soon on Render!

---

## License

This project is open-source under the [MIT License]()

---

## Acknowledgements

- Flask Documentation
- Natural Language Toolkit for word data & definitions
- GitHub for hosting
- AI assistants for code review and guidance

---

**Built with passion by Avik43218**
Level up your vocabulary - one guess at a time!
Keep Learning :D
