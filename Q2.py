##Question 2:
##Write a Python program that converts a Binary number into its equivalent Decimal number.
##The program should start reading the binary number from the user. Then the decimal equivalent number must be calculated.
#Finally, the program must display the equivalent decimal number on the screen.
##Tips: solve input errors.

l = list(n)
l.reverse()
for i in l:
    if (i != '1') and (i != '0'):
        print("error, enter a binary number!")
        exit()

d = 0
for j in range(len(l)):
    d = d + int(l[j]) * 2 ** j

print("equivalent decimal number = ", d)