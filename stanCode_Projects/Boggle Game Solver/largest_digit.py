"""
File: largest_digit.py
Name: Gibbs
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	This function recursively finds the biggest digit and prints it out.
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the number used to find the largest digit
	:return: the largest digit in the number
	"""
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, largest_digit):
	"""
	This function helps find the largest digit in the number.
	:param n: the number used to find the largest digit
	:param largest_digit: stores the largest digit in the number, the default value is 0.
	:return: the largest digit in the number
	"""
	if n == 0:
		return largest_digit
	else:
		if n < 0:
			n = n * (-1)
		digit = n % 10
		if digit > largest_digit:
			largest_digit = digit
		n = n//10
		return find_largest_digit_helper(n, largest_digit)


if __name__ == '__main__':
	main()
