#***************  McbrideD_CSCI1470_HW10.py  ***************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Homework #10
#
# Algorithm:
#   Start
#   
#**********************************************************

def checkLength(password):
    if len(password) >= 8:
        return True
    else:
        return False

def checkUppercase(password):
    for character in password:
        if character.isupper():
            return True
    return False

def checkLowercase(password):
    for character in password:
        if character.islower():
            return True
    return False

def checkDigit(password):
    for character in password:
        if character.isdigit():
            return True
    return False

print("Let's get your password set up!\n")
password = input("New Password: ")

invalidPassword = True

while invalidPassword:
    validLength = checkLength(password)
    validUpper = checkUppercase(password)
    validLower = checkLowercase(password)
    validDigit = checkDigit(password)

    if validLength and validUpper and validLower and validDigit:
        invalidPassword = False
    else:
        print("Sorry, your password was invalid")
        if not validLength:
            print("The password did not meet the 8 character minimum length")
        if not validUpper:
            print("The password did not contain an uppercase letter")
        if not validLower:
            print("The password did not contain a lowercase letter")
        if not validDigit:
            print("The password did not contain a numerical character")
        print()
        password = input("Please enter a new password: ")

verifyPassword = False

while not verifyPassword:
    print()
    passwordCheck = input("Please reenter your password: ")

    if passwordCheck == password:
        verifyPassword = True
    else:
        print("Verification failed")

print("Verification Succeded! Your new password is now in place!")
