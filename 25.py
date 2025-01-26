# Write a simple “guess the number” game. The program randomly generates a number between 1 and 10, and the user has to guess it.
import random   
number = random.randint(1,10)
print(number)
guess = int(input("Guess the number: "))

if guess == number:
    print("You guessed it right!")
else:
    print(f"Wrong! The number was {number}")