# Question 1:
# C- L=[‘Network’ , ’Bio’ , ’Programming’, ‘Physics’ , ‘Music’]
# In this exercise, you will implement a Python program that reads the items of the previous list and identifies
# the items that starts with ‘B’ letter, then print it on screen.
# Tips: using loop, ‘len ()’ , startswith() methods.


L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']
for i in range(len(L)):
    if L[i].startswith('B'):
        print(L[i])