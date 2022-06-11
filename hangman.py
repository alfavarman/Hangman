import os
import random
from manual import manual
from time import sleep
from hangman_graphic import graphics


def load_graphic(pic_number):
    print(graphics[pic_number])


def clrscr():
    os.system('clear')


def play(word, lives):
    """Function use word(str) to guess with lives(int) number
    (equals allowed number of mistakes - wrong guesses)

    :param word:(str) word to guess
    :param lives:(int) number limiting mistakes
    """
    os.system('clear')
    print(word)  # for testing purposes to be removed
    word_set = set(word.casefold())
    guess_set = set()
    # max_lives = lives

    while lives > -1:
        load_graphic(lives)
        print('\t\t\t', end='')
        for char in word:
            if char.casefold() not in guess_set:
                print('_', end='')
            else:
                print(char, end='')

        # print()
        if word_set.issubset(guess_set):
            print('Congratulation! You Guessed Word! No Man will be hang today!')
            break
        print('\n\t\tLives: ', end='')
        print('@' * lives)
        letter = input('choose letter: ')
        if not letter.isalpha():
            incorrect_input("Input must be single letter.")
        elif letter.casefold() == 'quit':
            break
        elif len(letter) != 1:
            incorrect_input('Type one latin alphabet letter')
        else:
            if letter in guess_set:
                print(f'The letter: "{letter}" you tried already. Try another one!')
            else:
                guess_set.add(letter)
                if letter not in word_set:
                    lives -= 1
        if lives == 0:
            load_graphic(0)
            print('Sorry Your Friend is Hanged!')
            sleep(3)
            break


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


def good_bye(sec: int = 3):
    """function to terminate program after (default 2) sec after printing goodbye"""
    print('\t\tGood Bye! Thank You')
    sleep(sec)


def print_menu():
    """function to print menu"""
    # bug: invalid input at menu(Hard Medium Easy) moves back to main menu - should stay same menu)
    clrscr()
    while True:
        choice = input('''
        Welcome to Hangman Countries & Capitols
        ***************************************
        1: Play
        2: Manual
        3: Exit
        ''')
        if choice == '1':
            clrscr()
            choice2 = input("""
        1: Hard
        2: Medium
        3: Easy
        
        4: Back
        """)
            if choice2 == '1':
                play(random_word(), 3)
            elif choice2 == '2':
                play(random_word(), 5)
            elif choice2 == '3':
                play(random_word(), 7)
            elif choice2 == '4':
                pass
            elif choice2.casefold() == 'quit':
                good_bye()
                break
            else:
                incorrect_input('select number from menu or type quit')
        elif choice == '2':
            print('\t' + manual)
            input('\t\tpress any key to go back')
        elif choice == '3':
            good_bye()
            break
        elif choice.casefold == 'quit':
            good_bye()
            break
        else:
            incorrect_input('select from menu')


if __name__ == '__main__':
    print_menu()


