"""
File: boggle.py
Name: Gibbs
----------------------------------------
This program is a classic boggle game. Users put in 4 rows(each row contains 4 characters),
and the program will find the words from the 4x4 grid.
All of the words exist in the dictionary, and the length for each words equals to or is longer than 4.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variables
# Used to store all the words in FILE
dictionary = []


def main():
	"""
	Users put in 4 rows(each row contains 4 characters),and the program will find the words from the 4x4 grid.
	"""
	read_dictionary()
	rows = input_rows()
	if rows != 'no':
		points_list = []
		ans_list = []
		for row in range(4):
			for column in range(4):
				points_list.append([row, column])
				ans = rows[row][column]
				find_words(rows, points_list, ans, ans_list)
				points_list.pop()
		print(f'There are {len(ans_list)} words in total.')


def input_rows():
	"""
	Users put in 4 rows(each row contains 4 characters with blank space)
	:return: list, contains 4 rows
	"""
	rows = []
	for i in range(4):
		row = input(f'{i+1} row of letters: ').lower().split()
		if len(row) == 0:
			print('Illegal input')
			return 'no'
		for ch in row:
			if len(ch) != 1 or not ch.isalpha() or len(row) != 4:
				print('Illegal input')
				return 'no'
		rows.append(row)
	return rows


def find_words(rows, points_list, ans, ans_list):
	"""
	This function finds all the qualified words from the 4x4 grid.
	:param rows: list, contains 4 rows
	:param points_list: list, stores used (row, column)
	:param ans: str, used to search in the dictionary
	:param ans_list: list, stores all the qualified words
	"""
	if len(ans) >= 4:
		if ans in dictionary:
			if ans not in ans_list:
				ans_list.append(ans)
				print(f'Found "{ans}"')
	if has_prefix(ans):
		for row in range(-1, 2, 1):
			for column in range(-1, 2, 1):
				if row == 0 and column == 0:
					pass
				else:
					points_row = points_list[len(points_list)-1][0] + row
					points_column = points_list[len(points_list)-1][1] + column
					if 0 <= points_row <= 3 and 0 <= points_column <= 3:
						if [points_row, points_column] not in points_list:
							points_list.append([points_row, points_column])
							ans += rows[points_row][points_column]
							find_words(rows, points_list, ans, ans_list)
							points_list.pop()
							ans = ans[:len(ans)-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, 'r') as f:
		for line in f:
			dictionary.append(line.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
