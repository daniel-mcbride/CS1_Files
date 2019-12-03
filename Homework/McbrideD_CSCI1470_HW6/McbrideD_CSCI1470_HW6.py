#***************  McbrideD_CSCI1470_HW6.py  ***************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Homework #6
#
# Algorithm:
#   Start
#   
#**********************************************************

import random

anotherQuiz = True

operators = ["+", "-", "*", "/", "%"]
numQuestions = 10

def createQuizProblem(operator, questionNum):
    firstNum = random.randint(1, 20)
    secondNum = random.randint(1, 20)

    print("Question", " ", questionNum, ": ", firstNum, " ", operator, " ", secondNum, sep="")

    if operator == "+":
        answer = firstNum + secondNum
    elif operator == "-":
        answer = firstNum - secondNum
    elif operator == "*":
        answer = firstNum * secondNum
    elif operator == "/":
        print("**Round division down to the nearest whole number**")
        answer = firstNum // secondNum
    elif operator == "%":
        answer = firstNum % secondNum
    
    return answer


while anotherQuiz:
    numCorrect = 0
    currentQuestion = 1
    
    print("Let's start a new quiz!\n")

    for operator in operators:
        for i in range(2):
            currentAnswer = createQuizProblem(operator, currentQuestion)
            userAnswer = int(input("Answer: "))

            if currentAnswer == userAnswer:
                print("Correct!")
                numCorrect += 1
            else:
                print("Sorry, the correct answer is", currentAnswer)
            
            print()

            currentQuestion += 1
        
    print("You got", numCorrect, "out of", numQuestions, "correct!")
    print()
    newQuiz = input("Would you like to take another quiz? (Y/N) ")
    newQuiz = newQuiz.lower()

    if not newQuiz == "y" or newQuiz == "yes":
        anotherQuiz = False
    else:
        currentQuestion = 1
        numCorrect = 0
        print()
        print()
        
print("That's all for today, I hope you're happy with your results!")
