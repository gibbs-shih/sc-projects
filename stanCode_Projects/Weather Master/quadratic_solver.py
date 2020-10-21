"""
File: quadratic_solver.py
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This function will compute the roots of equation: ax^2+bx+c=0.
	"""
	print('stanCode Quadratic Solver!')
	compute_the_roots_of_equation()


def compute_the_roots_of_equation():
	"""
	Use the three given numbers(a,b,and c), and discriminant(b^2-4ac) to get the roots of equation.
	discriminant>0, two roots.
	discriminant=0, one root.
	discriminant<0, no real roots.
	"""
	a = int(input('Enter a : '))
	if a != 0:
		b = int(input('Enter b : '))
		c = int(input('Enter c : '))
		discriminant = b**2-4*a*c
		if discriminant > 0:
			y = math.sqrt(discriminant)
			x1 = (-b+y)/(2*a)
			x2 = (-b-y)/(2*a)
			print('Two roots: ' + str(x1) + ' , ' + str(x2))
		elif discriminant == 0:
			x = -b/(2*a)
			print('One root: ' + str(x))
		else:
			print('No real roots.')
	else:
		print("'a' can not be zero!")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
