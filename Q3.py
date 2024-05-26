# Question 3:
# Type python quiz program that takes a text or json or csv file as input for (20 (Questions, Answers)). It asks
# the questions and finally computes and prints user results and store user name and result in separate file csv or json file.

import json
questions = {}
degree = 0
num = 1
infile = open("QUIZ.json", "r")
questions = json.load(infile)
infile.close()
name = input("Enter your name: ")
for i in questions.keys():
    print(num, end=""), print(")", i)
    answer = input("the answer is: ")
    if answer == questions[i]:
        degree += 1
        print("correct")
    else:
        print("wrong")
    num += 1
result = {name: degree}
outfile = open("result.json", 'w')
json.dump(result, outfile)
outfile.close()

