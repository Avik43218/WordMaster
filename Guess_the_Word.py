import pickle
import random

def initialise():

    print("""Select a difficulty:
          1. Recruit
          2. Regular
          3. Heroic
          4. Veteran
          """)
    
    choice = input("Enter your choice: ")

    if choice == '1' or choice.lower() == 'recruit':
        tries = 8
    elif choice == '2' or choice.lower() == 'regular':
        tries = 6
    elif choice == '3' or choice.lower() == 'heroic':
        tries = 4
    elif choice == '4' or choice.lower() == 'veteran':
        tries = 3

    return tries

def get_offsets(file_path):

    offset = []
    with open(file_path, 'rb') as f:
        while True:
            pos = f.tell()
            try:
                pickle.load(f)
                offset.append(pos)
            except EOFError:
                break

    return offset

def get_random_word(file_path):

    offsets = get_offsets(file_path)
    if not offsets:
        raise ValueError("No valid pickle objects found. The file may be empty or corrupted!")
    
    random_pos = random.choice(offsets)

    with open(file_path, 'rb') as file:
        file.seek(random_pos)
        word_meaning = pickle.load(file)

        return word_meaning

def reveal_char(word, user_input):

    revealed = []
    indices = []

    for i, char in enumerate(word):
        if char in user_input:
            revealed.append(char)
            indices.append(i)
        else:
            revealed.append('_')
            indices.append(i)

    return revealed, indices

def game_logic():

    tries = initialise()
    random_word_meaning = get_random_word(r"K:\Programs\PythonPrograms\Game\filtered_words.dat")

    attempts = 0
    print(f"Definition: {random_word_meaning[1].capitalize()}\n")

    hidden_word = "_" * len(random_word_meaning[0]) + f"   ({len(random_word_meaning[0])} letters)"
    print(hidden_word)
    print("\n")

    while attempts < tries:

        print(f"You have {tries - attempts} tries left")
        word = input("Enter the word: ")
        print("\n")
        attempts += 1

        partial_word = reveal_char(random_word_meaning[0], word)
        chars = partial_word[0]
        print(''.join(chars))


        if word.lower() == random_word_meaning[0].lower():
            print(f"Congratulations! You guessed the word in {attempts} tries\n")
            break
        else:
            if attempts == (tries):
                print("GAME OVER!")
                print("The correct word was: ", random_word_meaning[0])
                print("\n")
            else:
                print("Wrong guess! Try again!\n")

if __name__ == "__main__":
    game_logic()
