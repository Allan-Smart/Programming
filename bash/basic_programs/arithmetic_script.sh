#!/bin/bash

# Author: 	 Allan Smart
# Date Created:  12/11/2026
# Date Modified: 16/11/2026

# Application:
# Basic calculatior

# Usage:
# Bash script can be created using: chmod 744 arithmetic_functions.sh
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
	local total=$(echo "scale=2; $num1 + $num2" | bc)
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
	read -p "Enter the second number: " num2

	# Calculate and display the total:
	local total=$(echo "scale=2; $num1 - $num2" | bc)
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

	if [ "$(echo "$num2 == 0" | bc)" -eq 1 ];  then
		echo ""
		echo "Cannot Divide by zero"
		echo "Returning to menu......"
		return 1
	fi

	# Calculate and display the total:
	local total=$(echo "scale=2; $num1 / $num2" | bc)
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
	read -p "Enter the second number: " num2

	# Calculate and display the total:
	local total=$(echo "scale=2; $num1 *  $num2" | bc)
	echo ""
	echo "The product of $num1 * $num2 is: $total"

}

area_of_circle() {

	# Assign radius variable
	local -r PI=3.141592
	local radius

	# Prompt user to enter input:
	echo ""
	read -p "Enter the radius: " radius 

	# Calculate and display the area:
	local area=$(echo " $radius * $PI ^ 2" | bc)
	echo ""
	echo "The area of circle with $radius is: $area"
}

# Main function
main() {

	# Main menu selection
	
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
		echo "5. Area of a circle"
		echo "6. Exit"
		echo ""
		read -p "Enter the for the arithmetic operation (1-6): " choice

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
				echo ""
				echo "You chose Area of a Circle"
				echo ""
				area_of_circle
				;;

			6)
				echo""
				echo "You have chosen to exit"
				echo "Exiting....."
				break
				;;
			*)
				echo ""
				echo "Invalid choice! Please enter between 1 to 6"
				;;
	
		esac
	
	done
}

# Calling the main function
main

exit 0
