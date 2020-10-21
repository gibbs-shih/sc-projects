"""
Name: Gibbs
File: similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This function is used to find the most similar part between s1(long DNA sequence) and s2(short DNA sequence).
    """
    long = give_long()
    short = give_short()
    similarity1 = find_similarity(long, short)
    print('The best match is '+similarity1+'.')


def give_long():
    """
    Users give a long DNA sequence to search.
    :return: long DNA sequence
    """
    long = input('Please give me a DNA sequence to search: ')
    long = long.upper()
    return long


def give_short():
    """
    Users give a short DNA sequence to match.
    :return: short DNA sequence
    """
    short = input('What DNA sequence would you like to match? ')
    short = short.upper()
    return short


def find_similarity(long, short):
    """
    This function will find out the most similar part in long DNA sequence when compared to short DNA sequence.
    :param long: long DNA sequence
    :param short: short DNA sequence
    :return: the most similar part between long and short DNA sequence
    """
    similarity1 = 0
    similarity2 = 0
    for i in range(len(long)-len(short)+1):
        a = 0
        part = long[i:i+len(short)]
        for j in range(len(part)):
            if part[j] == short[j]:
                a += 1
        if a == len(short):
            similarity1 = part
            return similarity1
        elif a > similarity2:
            similarity2 = a
            similarity1 = part
    return similarity1




###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
