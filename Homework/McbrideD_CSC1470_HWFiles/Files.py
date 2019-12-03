#***************  McbrideD_CSCI1470_HWFiles.py  ***************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Sports Files
#
# Algorithm:
#   Start
#   Open text file
#**********************************************************

statsFile = open( "AstroRoster.txt", "r" )

numPlayers = 0
totalWeight = 0
totalAge = 0
tallestPlayers = ""
seniorYears = 0
seniorPlayers = []

for line in statsFile:

    numPlayers += 1
    
    lineparts = line.split("\t")

    uniformNum = int(lineparts[0])
    name = lineparts[1]
    position = lineparts[2]
    age = int(lineparts[3])
    battingArm = lineparts[4]
    pitchingArm = lineparts[5]
    height = lineparts[6]
    weight = int(lineparts[7])
    DoB = lineparts[8]
    rookieYear = int(lineparts[9])

    print(name, " #", uniformNum, sep="")

    totalWeight += weight
    totalAge += age

    heightParts = height.split(" ")
    feet = heightParts[0][0]
    inches = heightParts[1][0:-1]

    if tallestPlayers != "":
        if tallestPlayers[0][1] < feet:
            tallestPlayers = [[name, feet, inches]]
        elif tallestPlayers[0][1] == feet:
            if tallestPlayers[0][2] < inches:
                tallestPlayers = [[name, feet, inches]]
            elif tallestPlayers[0][2] == inches:
                tallestPlayers.append([name, feet, inches])
    else:
        tallestPlayers = [[name, feet, inches]]

    playerSeniority = 2019 - rookieYear

    if playerSeniority > seniorYears:
        seniorYears = playerSeniority
        seniorPlayers = [name]
    elif playerSeniority == seniorYears:
        seniorPlayers.append(name)

print()

avgWeight = totalWeight // numPlayers
print("The average player wieght is", avgWeight)

avgAge = totalAge // numPlayers
print("The average player age is", avgAge)

if len(tallestPlayers) == 1:
    print("The tallest player is ", tallestPlayers[0][0], " at ", tallestPlayers[0][1], "'", tallestPlayers[0][2], "\"", sep="")
else:
    print("The", len(tallestPlayers), "tallest players are:")
    for player in tallestPlayers:
        print("  ", player[0], " at ", player[1], "'", player[2], "\"", sep="")
if len(seniorPlayers) == 1:
    print("The most senior player is", seniorPlayers[0])
else:
    print("The", len(seniorPlayers), "most senior players are:")
    for player in seniorPlayers:
        print(" ", player)
