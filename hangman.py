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
    print(word) # for testing purposes to be removed
    word_set = set(word)
    #word_set.remove('\n')
    print(word_set)
    guess_set = set()
    print('Word: ', end='')
    for char in word:
        if char not in guess_set:
            print('_', end='')
        else:
            print(char, end='')

    print('\nLives: ', end='')
    print('@' * lives)

    while lives >= 0:
        letter = input('choose letter: ')
        if not letter.isalpha():
            incorrect_input("Input must be single letter.")
        elif len(letter) != 1:
            incorrect_input('Type one latin alphabet letter')
        else:
            if letter in guess_set:
                print(f'The letter: "{letter}" you tried already. Try another one!')
            else:
                guess_set.add(letter)
                if letter in word:
                    for char in word:
                        if char not in guess_set:
                            print('_', end='')
                        else:
                            print(char, end='')
                    print('\nLives: ', end='')
                    print('@' * lives)
                    guess_set.add(letter)
                else:
                    lives -= 1
                    print('\nLives: ', end='')
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
        word = word.strip('\n')
    return word


def incorrect_input(message):
    print('Invalid Input.')
    print(message)


def print_menu():
    """function to print menu"""

    while True:
        choice = int(input('''
        Welcome to Hangman Countries & Capitols
        ***************************************
        1: Play
        2: Manual
        3: Exit
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
                #break # to remove once def play is completed
            elif choice2 == 2:
                play(random_word(), 5)
                #break # to remove once def play is completed
            elif choice2 == 3:
                play(random_word(), 7)
                #break # to remove once def play is completed
            elif choice2 == 4:
                os.system('clear')
            else:
                incorrect_input()
        elif choice == 2:
            print(manual)
            input('\tpress any key to go back')
        elif choice == 3:
            print('Bye Bye!')
            sleep(3)
            exit()
        else:
            incorrect_input()


print_menu()



