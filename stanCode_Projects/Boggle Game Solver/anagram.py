"""
File: anagram.py
Name: Gibbs
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variables
# Used to store all the words in FILE
dictionary = []


def main():
    """
    This program recursively finds and prints out all the anagram(s) for the word input by user.
    """
    print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)')
    read_dictionary()
    while True:
        anagram = input('Find anagrams for: ')
        if anagram == EXIT:
            break
        find_anagrams(anagram.lower())


def read_dictionary():
    """
    This function puts all the words from FILE('dictionary.txt') in the list(dictionary).
    """
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            dictionary.append(line.strip())


def find_anagrams(s):
    """
    This function finds all the anagram(s) for the word input by user,
    and prints out all the anagram(s) and how many anagram(s) found.
    :param s: str, the word input by user
    """
    print('Searching...')
    s_list = []
    for ch in s:
        s_list.append(ch)
    ans_list = []
    find_anagrams_helper(s_list, '', [], ans_list, [])
    print(f'{len(ans_list)} anagrams: {ans_list}')


def find_anagrams_helper(s_list, current_str, ans, ans_list, number_list):
    """
    This function recursively helps find all the anagram(s) for the word input by user,
    and prints them out.
    :param s_list: list, stores each character of the word input by user in the list
    :param current_str: str, starts with '', used to store one found anagram
    :param ans: list, starts with [], stores each character of one found anagram in the list
    :param ans_list: list, starts with [], used to store all the anagram(s) found in the list
    :param number_list: list, starts with [], stores index of each character of the word,
                        make sure each character used only one time
    """
    if len(ans) == len(s_list):
        if current_str in dictionary and current_str not in ans_list:
            ans_list.append(current_str)
            print(f'Found: {current_str} \nSearching...')
    else:
        for i in range(len(s_list)):
            ch = s_list[i]
            if i not in number_list:
                number_list.append(i)
                ans.append(ch)
                if has_prefix(current_str+ch):
                    find_anagrams_helper(s_list, current_str+ch, ans, ans_list, number_list)
                ans.pop()
                number_list.pop()


def has_prefix(sub_s):
    """
    This function helps decide whether to go on next recursion by searching every words
    in the dictionary, and checking whether they contain prefix stored in sub_s. It avoids unnecessary recursion.
    :param sub_s: str, used to search in the dictionary
    :return: bool, if there is any words with prefix stored in sub_s
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
