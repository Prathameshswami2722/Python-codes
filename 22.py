# Write a program that counts the number of vowels in a string.

s = input("Enter a string: ")
vowels = "aeiou"
count = 0
for i in s:
    if i in vowels:  #For each character i, the program checks if it exists in the string vowels
        count += 1
print(f"The number of vowels in the string is: {count}")