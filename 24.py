# Write a program to reverse the digits of a given integer (e.g., 123 -> 321).

num=int(input("Enter a number: "))
rev=0     #A variable rev (short for “reverse”) is initialized to 0 This variable will hold the reversed number.
while num>0:    #A while loop runs as long as num is greater than 0.

    rem=num%10  #The remainder operator (%) is used to extract the last digit of num.

    rev=rev*10+rem  #	•	The current digit (rem) is appended to the reversed number (rev) The multiplication
    #by 10 shifts the digits of rev one place to the left, making space for the new digit.

    num=num//10  #The integer division operator (//) removes the last digit from num.
print(rev)