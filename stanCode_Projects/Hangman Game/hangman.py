"""
Name: Gibbs
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    This function plays hangman game. Try to guess the answer in limited chances.
    """
    answer = random_word()
    dashed = opening(answer)
    guess(answer, dashed)


def opening(answer):
    """
    This function is the opening of hangman game.
    It shows a dashed word and the chances you have to guess the word.
    :param answer: the word to be guessed
    :return: A dashed word. The numbers of the dash is the character numbers of the word to be guessed.
    """
    dashed = ''
    for i in range(len(answer)):
        dashed += '-'
    print('The word looks like: ' + dashed)
    print('You have '+str(N_TURNS)+' guesses left.')
    return dashed


def random_word():
    """
    This function gives a word randomly to players to guess.
    :return: the word to be guessed
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def guess(answer, dashed):
    """
    :param answer: the word to be guessed
    :param dashed: A dashed word. The numbers of the dash is the character numbers of the word to be guessed.
    :return: the result of the game
    """
    b = dashed
    chance = N_TURNS
    while True:
        result = ''
        input_ch = input('Your guess: ')
        if input_ch.isalpha() and len(input_ch) == 1:  # make sure input_ch is in legal format
            input_ch = input_ch.upper()
            b = re_construct(answer, input_ch, result, b)  # check input_ch correct or wrong, and show result
            if b == answer:
                print('You win!! \nThe word was: ' + answer)
                break
            elif input_ch in b:
                print('You are correct! \nThe word looks like: ' + b)
                print('You have ' + str(chance) + ' guesses left.')
            else:
                chance -= 1
                if chance == 0:
                    print('You are completely hung : ( \nThe word was: ' + answer)
                    break
                elif chance > 0:
                    print('There is no '+input_ch+'\'s in the world. \nThe word looks like: ' + b)
                    print('You have ' + str(chance) + ' guesses left.')
        else:
            print('illegal format.')


def re_construct(answer, input_ch, result, b):
    """
    This function checks the input_ch correct or wrong, and shows the result.
    :param answer: the word to be guessed
    :param input_ch: the character input by users
    :param result: a '' string
    :param b: A dashed word. The numbers of the dash is the character numbers of the word to be guessed.
    :return: a new result to continue the hangman game
    """
    for i in range(len(answer)):
        ch = answer[i]
        if ch == input_ch:
            result += input_ch
        else:
            result += b[i]
    return result


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
