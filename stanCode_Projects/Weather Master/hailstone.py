"""
File: hailstone.py
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This function will simulate the execution of the Hailstone sequence.
    if n is odd, n -> 3n+1,
    if n is even, n -> n/2,
    until n = 1.
    """
    print('This program computes Hailstone sequences.')
    print('')
    a = 0  # 'a' used to count how many steps happen.
    x = int(input('Enter a number: '))
    while True:
        if x == 1:
            print('It took '+str(a)+' steps to reach 1.')
            break
        elif x % 2 == 1:  # x is odd.
            print(str(x)+' is odd, so I make 3n+1: '+str(3*x+1))
            x = 3*x+1
        else:  # x is even.
            print(str(x)+' is even, so I take half: '+str(x//2))
            x = x//2
        a += 1


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
