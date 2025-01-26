# Write a program to display the multiplication table of a given integer up to 10.

num = int(input("Enter a number: "))
for i in range(1,11):

    # for i in range(1,11): Starts a loop where the variable i will take values from 1 to 10 (inclusive)
	# range(1,11) generates a sequence of numbers starting from 1 and ending at 10

    print(num, "x", i, "=", num*i)   	
    
    # num * i: Calculates the product of the entered number (num) and the current loop variable (i)