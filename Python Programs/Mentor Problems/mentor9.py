#INCOMPLETE

userString = input("Type something! Try to include all the common english letters!\n")

commonList = ["e","t","a","i","n"]

while len(commonList) > 0):
    for char in userString:
        if char in commonList:
            commonList.remove(char)
        
    userString = input("That's not all of them. Type some more to get them all!")
