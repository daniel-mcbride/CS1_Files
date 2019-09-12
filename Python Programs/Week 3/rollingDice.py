import random
answer = input("Do you want to roll dice? ")
answer = answer.lower()

while answer == "yes" or answer == "y":
    randomNum = random.randint(1, 6)
    print("The number you rolled is:", randomNum)
    answer = input("Do you want to roll dice? ")
