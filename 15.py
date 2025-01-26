# Write a program that calculates the factorial of a given positive integer using a for loop.
num = int(input("Enter a number: "))
factorial = 1   
# The variable factorial is initialized to 1.

for i in range(1, num+1):
    # The range(1, num+1) generates a sequence of numbers starting from 1 and ending at num (inclusive).

    factorial = factorial * i
    # In each iteration, the current value of factorial is multiplied by i (the current number in the loop).
    
print(f"The factorial of {num} is {factorial}")