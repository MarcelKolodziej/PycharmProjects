"""

Simple hangman implementation with lives.


M.K

"""

import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or '' in word:  # if word contain '-' or '' keep roll on list
        word = random.choice(words)

        return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> ' a b cd'
        print('You have', lives, 'You have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', '  '.join(word_list))

        # imput
        user_letter = input("Guess a letter:").upper()  # small "a" is a diffrent then capital "A"
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # take out one life
                print('\nYour letter,' , user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('\nInvalid character. Please try Again')

    # get here when len(world_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was -->', word)

    else:
        print('Congratz!! You guessed well -->', word)


if __name__ == '__main__':
    hangman()
