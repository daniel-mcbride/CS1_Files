import random

correctNum = random.randint(1, 100)

print("Let's play a guessing game!")
print("You have 6 tries to guess the number between 1-100!")

success = False
attempt = 1

while attempt < 7:
    guess = int(input("What's your guess? "))

    if guess == correctNum:
        print("Congratulations!", correctNum, "is correct!")
        success = True
        break
    elif guess > 0 and guess < 101:
        attempt += 1
        
        if guess > correctNum:
            print("Sorry, the number is lower than", guess)
        else:
            print("Sorry, the number is higher than", guess)
    else:
        print("invalid guess. Don't worry it won't count against you")
if not success:
    print("GAME OVER. You have run out of guesses")
    print("The correct number was", correctNum)
