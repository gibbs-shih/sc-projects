"""
Name: Gibbs
File: caesar.py
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This function can help to decipher any ciphered strings put in.
    """
    secret = int(input('Secret number: '))  # decides new shifted order of the alphabetic sequence
    ciphered_string = input("What's the ciphered string? ")
    ciphered_string = ciphered_string.upper()
    ans = deciphered_string(ciphered_string, secret)
    print('The deciphered string is: '+ans)


def alphabet(secret):
    """
    This function gets the new shifted alphabet sequence according to the rule.
    :param secret: the number to shift the alphabet sequence
    :return: a new shifted alphabet sequence
    """
    new_alphabet = ''
    secret = secret % 26  # make sure the shift number in the range from 0 ~ 26
    new_alphabet += ALPHABET[26-secret:26]
    new_alphabet += ALPHABET[:26-secret]
    return new_alphabet


def deciphered_string(ciphered_string, secret):
    """
    This function helps to get the deciphered string.
    :param secret: The number decides new shifted order of the alphabetic sequence.
    :param ciphered_string: the ciphered string required to be deciphered
    :return: the deciphered string
    """
    new_alphabet = alphabet(secret)
    ans = ''
    for i in ciphered_string:
        if i in new_alphabet:
            j = new_alphabet.find(i)
            ans += ALPHABET[j]
        else:
            ans += i
    return ans



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
