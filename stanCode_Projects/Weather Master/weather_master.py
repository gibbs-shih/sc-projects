"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


QUIT = -100  # To quit the program.


def main():
	"""
	This program will compute the average, highest, lowest, cold days among the inputs.
	"""
	print("stanCode \"Weather Master 4.0!\"")
	give_temperature_get_result()


def give_temperature_get_result():
	a = int(input('Next temperature: (or '+str(QUIT)+' to quit)? '))
	if a == QUIT:
		print('No temperatures were entered.')
	else:
		highest_temperature = a
		lowest_temperature = a
		how_many_days = 1
		total = a
		cold_days = 0
		if a < 16:
			cold_days = 1
		while True:
			a = int(input('Next temperature: (or ' + str(QUIT) + ' to quit)? '))
			if a == QUIT:
				break
			if a > highest_temperature:  # This will find the highest temperature.
				highest_temperature = a
			if a < lowest_temperature:  # This will find the lowest temperature.
				lowest_temperature = a
			if a != QUIT:  # This will compute the average temperature by total/ how many days.
				how_many_days += 1
				total += a
			if a < 16:  # This will count how many cold days.
				cold_days += 1
		print('Highest temperature = '+str(highest_temperature))
		print('Lowest temperature = '+str(lowest_temperature))
		print('Average = '+str(total/how_many_days))
		print(str(cold_days)+' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
