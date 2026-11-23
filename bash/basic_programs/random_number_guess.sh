#!/bin/bash


# Author: 	 	Allan Smart
# Date Created:  24/11/2026
# Date Modified: 24/11/2026

# Description:
# Random number guessing game between 1 and 100.

# Usage:
# ./random_number_guess

# Main function
main() {

	# Assign random number variable
	random_number=$(shuf -i 1-100 -n 1)

	# Assign attempts variable
	attempts=0

	# main loop
	while true
	do
		# Prompt user to enter random number
		echo ""
		read -p "Enter a random number between 1 - 100. You have five guesses: " guess

		# Checking guess against random number
		if (( guess == random_number )); then
			echo "Well done!!! You have guessed correctly"
			break
		elif (( guess > random_number )); then
			echo "Incorrect. Try guessing lower"
		else
			echo "Incorrect. Try guessing higher"
		fi

		# Adding one to attempts counter
		(( attempts ++ ))

		# Checking number of attempts
		if (( attempts == 5 )); then
			echo ""
			echo "You  have used up all five guesses"
			echo "Random number is $random_number"
			break
		fi
	done

	# Printing exit statement
	echo ""
	echo "Exiting....."

	# Cleanly exiting program
	exit 0
}

# Call main function
main

