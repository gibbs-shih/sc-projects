"""
Name:　Gibbs
File: rocket.py
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 0  # It decides the size of the rocket.


def main():
	"""
	The rocket contains six parts in sequence: head, belt, upper, lower, belt, head.
	"""
	head(SIZE)
	belt(SIZE)
	upper(SIZE)
	lower(SIZE)
	belt(SIZE)
	head(SIZE)


def head(a):
	"""
	:param a: The size of the rocket.
	This function completes the head of the rocket.
	"""
	for i in range(a):
		for j in range(i, a):
			print(' ', end='')
		for j in range(i+1):
			print('/', end='')
		for j in range(i+1):
			print('\\', end='')
		print('')


def belt(a):
	"""
	:param a: The size of the rocket.
	This function completes the belt of the rocket.
	"""
	print('+', end='')
	for i in range(2*a):
		print('=', end='')
	print('+')


def upper(a):
	"""
	:param a: The size of the rocket.
	This function completes the upper of the rocket.
	"""
	for i in range(a):
		print('|', end='')
		for j in range(i, a-1):
			print('.', end='')
		for j in range(i+1):
			print('/', end='')
			print('\\', end='')
		for j in range(i, a-1):
			print('.', end='')
		print('|')


def lower(a):
	"""
	:param a: The size of the rocket.
	This function completes the lower of the rocket.
	"""
	for i in range(a):
		print('|', end='')
		for j in range(i):
			print('.', end='')
		for j in range(i, a):
			print('\\', end='')
			print('/', end='')
		for j in range(i):
			print('.', end='')
		print('|')


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == "__main__":
	main()