import random


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

play('grecja', 7)