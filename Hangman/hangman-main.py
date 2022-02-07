import random
import string
from words import words
# print(words)


# "Welcome to the hangman game:"

print(
    """Hello! You're about to start a game of hangman!
    The rules are:
    - you can only guess 6 letters total reflecting the hangman's body parts (head, body, legs, and arms)
    - each wrong letter hangs the next piece of the body"
    - if you guess the word correctly, you WIN"""
)


# Pick a random word for user to guess:

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


# The game:

def hangman():
    # Separate the word into letters:
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    # print(word)

    lives = 6

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used:
        # .join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ',
              ' '.join(used_letters))

        # Show what current word is (filling in as guessing goes on):
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        print(used_letters)

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:  # check validity of the character input
            # add a valid letter input into list of used letters
            used_letters.add(user_letter)
            if user_letter in word_letters:  # check if the letter is in the word chosen
                # if yes, remove from the list of letters in the word chosen
                word_letters.remove(user_letter)
            else:
                lives = lives - 1  # take away life if wrong
                print('Letter is not in the word.')
        elif user_letter in used_letters:
            print("You have already guessed that letter, try another one.")
        else:
            print("Invalid character, try again.")
    # Gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!')


hangman()

#user_input = input('Type something:')
#print("You\'ve entered " + user_input)
