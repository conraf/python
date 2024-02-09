import random

def get_valid_word(current_word):
    """
    Returns a valid next word for the chain based on the given current_word.
    """
    if len(current_word) < 2:
        raise ValueError("Invalid current_word")

    last_letter = current_word[-1]
    next_words = [w for w in words if w[0] == last_letter]
    return next_words[random.randint(0, len(next_words)-1)] if next_words else None

def play_game():
    """
    Plays a single game of Word Chain where players take turns entering a valid word that starts with the last letter of the previous word.
    """
    words = ["apple", "banana", "cat", "dog", "elephant"] # Replace with a larger word list or file.
    current_word = random.choice(words)
    print("Current word: {}".format(current_word))

    for _ in range(100): # Limit the number of turns to 100, increase for more turns
        next_word = input("Player's turn, enter a word that starts with the last letter of the current word: ")
        if not valid_next_word(current_word[-1], next_word):
            print("Invalid word! Try again.")
            next_word = input("Player's turn, enter a word that starts with the last letter of the current word: ")

        current_word = next_word
        print("Current word: {}".format(current_word))

    game_over = True
    for _ in range(3): # Give three attempts to input valid words after the last turn
        next_word = input("Enter a word that starts with the last letter of the current word or type 'quit' to exit: ")
        if not (next_word.lower() == "quit" or valid_next_word(current_word[-1], next_word)):
            print("Invalid word! Please try again.")
            game_over = False
            break

    if game_over:
        print("Thanks for playing Word Chain!")

def valid_next_word(last_letter, next_word):
    """
    Checks if the given next_word is valid based on the last letter of the current_word.
    """
    return next_word[0] == last_letter

if __name__ == "__main__":
    play_game()
