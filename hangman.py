import random
from menu_file import Menu


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


def print_menu(list_menu: list):
    """function to print menu
    from file

    Arguments:
        file:name of file with menu
        :param list_menu: """

    for index, (choice1, choice2) in enumerate(list_menu):
        print(f'{index +1 }: {choice1}')
    print('0: Exit')
    choice = input(int())

    if choice ==

print_menu(Menu)

# play(random_word(), 5)

