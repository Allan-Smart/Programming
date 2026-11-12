#!/bin/bash

# Author: 	 Allan Smart
# Date Created:  12/11/2026
# Date Modified: 12/11/2026

# Application:
# Basic calculatior

# Usage:
# ./arithmetic_functions

# ----------------- Arithmetic Functions:  ----------------- 

addition() {

	# Assign addition variables
	local num1 num2

	# Prompt user for inputs:
	echo ""
	read -p "Enter the first number: " num1
	echo ""
	read -p "Enter the second number: " num2

	# Calculate and display the total:
	local total=$(( num1 + num2 ))
	echo ""
	echo "The sum of $num1 + $num2 is: $total"
}

subtraction () {

	# Assign subtraction  variables
	local num1 num2

	# Prompt user for inputs:
	echo ""
	read -p "Enter the first number: " num1
	echo ""
	read -P "Enter the second number: " num2

	# Calculate and display the total:
	local total=$(( num1 + num2 ))
	echo ""
	echo "The difference of $num1 - $num2 is: $total"

}

division() {

	# Assign division variables
	local num1 num2

	# Prompt user for inputs:
	echo ""
	read -p "Enter the first number: " num1
	echo ""
	read -p "Enter the second number: " num2

	if [ $num2 -eq 0 ];  then
		echo "Cannot Divide by zero"
		echo "Exiting......"
		return 1
	fi

	# Calculate and display the total:
	local total=$(( num1 / num2 ))
	echo ""
	echo "The quotient of $num1 / $num2 is: $total"

}

multiplication() {

	# Assign multiplication variables
	local num1 num2

	# Prompt user for inputs:
	echo ""
	read -p "Enter the first number: " num1
	echo ""
	read -p "Enter the second numer " num2

	# Calculate and display the total:
	local total=$(( num1 *  num2 ))
	echo ""
	echo "The product of $num1 * $num2 is: $total"

}


# Main menu selection
echo ""

while true
do
	# Assign choice varialbe
	echo "" 
	echo "Bash Script Calculator:"
	echo ""
	echo "1. Addition"
	echo "2. Subtraction"
	echo "3. Division"
	echo "4. Multiplication"
	echo "5. Exit"
	echo ""
	read -p "Enter the for the arithmetic operation (1-5): " choice

	case "$choice" in
		1) 
			echo ""
			echo "You chose Addition"
			echo ""
			addition
			;;

		2)
			echo ""
			echo "You chose Subtraction"
			echo ""
			subtraction
			;;

		3)
			echo ""
			echo "You chose Division"
			echo ""
			division
			;;

		4)
			echo""
			echo "You chose Multiplication"
			echo ""
			multiplication
			;;
		5)
			echo""
			echo "You have chosen to exit"
			echo "Exiting....."
			break
			;;
		*)
			echo ""
			echo "Invalid choice! Please enter between 1 to 5"
			;;
	
	esac
	
done

exit 0
