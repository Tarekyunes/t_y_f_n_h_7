# Question 1:
# B- Write a Python program that calculates the factorial of a given number entered by user.

n = int(input("Enter a number: "))
if n < 0:
    print("error, enter a positive number")
else:
    factorialnumber = 1
    for i in range(1, n+1):
        factorialnumber *= i
    print(n, "!", sep="", end=""), print("=", factorialnumber)
