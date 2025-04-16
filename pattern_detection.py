import os

def is_sequential(guess):
    for i in range(len(guess) - 1):
        if ord(guess[i+1]) - ord(guess[i]) != 1:
            return False
    return True

def is_keyboard_pattern(guess):
    pattern = "abcdefghijklmnopqrstuvwxyzaeiouqwertyuiopasdfghjklzxcvbnmwasdazerty"
    if guess in pattern or guess[::-1] in pattern:
        return True
    return False

def is_repeated(guess):
    if len(set(guess)) == 1 and len(guess) > 2:
        return True
    return False

def is_suspicious_guess(guess):
    return is_sequential(guess) or is_keyboard_pattern(guess) or is_repeated(guess)

def is_real_word(guess):

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "clean_word_list.txt")

    with open(file_path, 'r') as file:
        valid_words = set(file.read().split())

    if guess in valid_words:
        return True
    return False
