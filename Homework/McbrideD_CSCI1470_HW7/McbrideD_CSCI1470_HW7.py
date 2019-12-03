#***************  McbrideD_CSCI1470_HW7.py  ***************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Homework #7
#
# Algorithm:
#   Start
#   
#**********************************************************

translationDict = {
    "a": 2,
    "b": 2,
    "c": 2,
    "d": 3,
    "e": 3,
    "f": 3,
    "g": 4,
    "h": 4,
    "i": 4,
    "j": 5,
    "k": 5,
    "l": 5,
    "m": 6,
    "n": 6,
    "o": 6,
    "p": 7,
    "q": 7,
    "r": 7,
    "s": 7,
    "t": 8,
    "u": 8,
    "v": 8,
    "w": 9,
    "x": 9,
    "y": 9,
    "z": 9
}

def translatePhoneNum(alphaNum):
    alphaNum = alphaNum.lower()
    translatedNum = ""

    for character in alphaNum:
        if character == "-":
            translatedNum += "-"
        elif character.isdigit():
            translatedNum += character
        else:
            print("not a dash or digit")
            translatedNum += str(translationDict[character])
                
    translatedNum = translatedNum.upper()

    return translatedNum

keepTranslating = True
print("Let's translate some phone numbers!\n")

while keepTranslating:
    encodedPhone = input("What phone number should we translate? (XXX-XXX-XXXX)\n")
    translatedPhone = translatePhoneNum(encodedPhone)

    print("That number translates out to", translatedPhone)
    print()

    continueCheck = input("Would you like to translate another number? (Y/N) ")
    continueCheck = continueCheck.lower()

    if not continueCheck == "y" or continueCheck == "yes":
        keepTranslating = False
