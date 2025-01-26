# Print the first n numbers of the Fibonacci sequence using a for loop.

n = int(input("Enter a number: "))
a = 0  #The variables a and b are initialized to 0 and 1, respectively
b = 1
for i in range(n):
    print(a)
    a, b = b, a+b #This is a tuple assignment that simultaneously updates the values of a and b: