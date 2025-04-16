from Guess_the_Word import get_random_word
from flask import Flask, request, render_template, session
import pattern_detection
import os

app = Flask(__name__, template_folder="templates")
app.secret_key = os.getenv("SECRET_KEY")

@app.route('/')
def loading():

    return render_template("loading.html")

@app.route('/start')
def start():

    return render_template("start_game.html")

@app.route('/setup', methods=['POST'])
def setup():

    return render_template("setup.html")


@app.route('/execute', methods=['POST', 'GET'])
def execute():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "valid_words.dat")
    
    if "score" not in session:
        session["score"] = 0

    if request.method == "POST" and "choice" in request.form:
        
        difficulty = request.form.get("choice")
        session["attempts"] = int(difficulty)
        session["max_attempts"] = session["attempts"]
        session["round"] = 0
        session["max_rounds"] = 9

    guess = ""
    msg = ""
    hidden_word = ""
        
    if session["round"] >= session["max_rounds"] and session["attempts"] == 0:

        msg = "You've completed all 10 rounds!"

        return render_template("game_over.html", score=session.get("score",0))

    else:

        if request.method == "GET" or "word" not in session:

            word, hint = list(get_random_word(file_path))
            length = len(word)
            hidden_word = "_" * length

            session["round"] += 1
            round = session["round"]
            session["attempts"] = session["max_attempts"]

            session["word"] = word.lower()
            session["hint"] = hint.lower()
            session["length"] = length
            session["hidden_word"] = hidden_word
            session["guessed_letters"] = []

        else:

            word = session.get("word")
            hint = session.get("hint")
            length = len(session.get("word"))
            guess = request.form.get("guess","").lower()

            # Input Validation

            if len(guess) != len(word) or not guess.isalpha():
                msg = "Invalid input! Please try again!"
                return render_template("game.html", hint=hint, message=msg, guess=guess, hidden_word=session["hidden_word"], length=length, word=word, round=session["round"], attempts=session["attempts"])

            elif pattern_detection.is_suspicious_guess(guess):
                msg = "Hmm... That seems like a keyboard pattern - Nice Try"
                return render_template("game.html", hint=hint, message=msg, guess=guess, hidden_word=session["hidden_word"], length=length, word=word, round=session["round"], attempts=session["attempts"])
            
            # Validation End

            guessed_letters = session.get("guessed_letters", [])

            for char in guess:
                if char not in guessed_letters:
                    guessed_letters.append(char)
            session["guessed_letters"] = guessed_letters

            def reveal_char(word, guessed_letters):
                return [c if c in guessed_letters else '_' for c in word]

            revealed_chars = reveal_char(word, guessed_letters)
                    
            session["hidden_word"] = "".join(revealed_chars)
            hidden_word = session["hidden_word"]

            round = session["round"]

            if guess == word:

                msg = "Congratulations! You guessed the word :)"

                session["score"] += 10
                session["attempts"] -= 1

                session.pop("word",None)
                session.pop("hint",None)
                session.pop("length",None)
                session.pop("hidden_word",None)
                session.pop("guessed_letters",None)


            else:

                if pattern_detection.is_real_word(guess) == False:
                    msg = "Nope, that ain't a word!"
                    session["attempts"] -= 1

                else:
                    
                    msg = "Wrong guess! Try again"
                    session["attempts"] -= 1

                if session["attempts"] <= 0:
                    msg = "Out of attempts! The word was: " + word
                    session["attempts"] = 0
                    session.pop("word",None)
                    session.pop("hint",None)
                    session.pop("length",None)
                    session.pop("hidden_word",None)
                    session.pop("guessed_letters",None)


        return render_template("game.html", hint=hint, message=msg, guess=guess, hidden_word=hidden_word, length=length, word=word, round=round, attempts=session["attempts"])

if __name__ == "__main__":
    app.run(debug=False)
