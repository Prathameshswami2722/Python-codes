# Write a Python function that takes a string and returns its length without using the built-in len() function.
str = input("Enter a string: ") #to input string by user 
length = 0    #this will be used to count the character in the string from 0 
for i in str:
    length += 1  #The for loop iterates over each character in the string, For every iteration, length is incremented by 1.
print(f"Length of the string: {length}")