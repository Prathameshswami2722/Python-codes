# Write a function that takes a string s and an integer n, and returns the string repeated n times.
def repeat_string(s, n):
    return (s+ " ")* n    

# repeat_string(s, n):
# s is a string (the input string).
# n is an integer (the number of times to repeat the string).
# Then, multiplying the result by n repeats this concatenated string n times. For instance, "hello " * 3 becomes "hello hello hello ".


s = input("Enter a string: ")
n = int(input("Enter a number: "))   

# int(input("Enter a number: ")): Prompts the user to enter a number
# The input is converted to an integer using int() and assigned to n.

print(repeat_string(s,n))
