import os
import random
from manual import manual
from time import sleep


def play(word, lives):
    """Function use word(str) to guess with lives(int) number
    (equals allowed number of mistakes - wrong guesses)

    :param word:(str) word to guess
    :param lives:(int) number limiting mistakes
    """

    print('Word: ', end='')
    for char in word:
        print('_', end='')

    print('\nLives:', end='')
    print('@' * lives)


def random_word():
    """ function create list of lines from file and select,
     random line from file and return it.

    Arguments: # all to be implemented in future
        file: source of file if not in the same directory
        word_length: (int) length of characters
    :return: word(str)
        """
    with open('countries-and-capitals.txt', 'r') as words:
        words_list = words.readlines()
        word = random.choice(words_list)
    return word


def incorrect_input():
    print('Invalid Input. Select number from Menu')


def print_menu():
    """function to print menu"""

    while True:
        choice = int(input('''
        Welcome to Hangman Countries & Capitols
        ***************************************
        1: Play
        2: Manual
        3: Exit
        :
        '''))

        if choice == 1:
            choice2 = int(input("""
            1: Hard
            2: Medium
            3: Easy
            
            4: Back
            """))
            if choice2 == 1:
                play(random_word(), 3)
                break # to remove once def play is completed
            elif choice2 == 2:
                play(random_word(), 5)
                break # to remove once def play is completed
            elif choice2 == 3:
                play(random_word(), 7)
                break # to remove once def play is completed
            elif choice2 == 4:
                os.system('clear')
            else:
                incorrect_input()
        elif choice == 2:
            print(manual)
            input('press any key to go back')
        elif choice == 3:
            print('Bye Bye!')
            sleep(3)
            exit()
        else:
            incorrect_input()


print_menu()



