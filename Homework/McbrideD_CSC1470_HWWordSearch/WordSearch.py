#***************  McbrideD_CSCI1470_HWWordSearch.py  ***************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Word Search Puzzle
#
# Algorithm:
#   Start
#   
#**********************************************************

import re

def searchGrid(grid, word):
    flippedWord = word[::-1]
    
    wordSearchRegex = re.compile(word)
    flippedWordSearchRegex = re.compile(flippedWord)

    matches = []

    rowNum = 1
    
    for row in grid:
        if wordSearchRegex.search(row) != None:
            match = wordSearchRegex.search(row)
            matches.append([rowNum, match.start(), match.end()])

        if flippedWordSearchRegex.search(row) != None:
            match = flippedWordSearchRegex.search(row)
            matches.append([rowNum, match.end(), match.start()])

        rowNum += 1

    if len(matches) == 0:
        print("ERROR:", word, "does not appear in this puzzle")
    else:
        if len(matches) == 1:
            print("\"", word, "\" appears in row ", matches[0][0], " from column ", matches[0][1], " to column ", matches[0][2], sep="")
        else:
            print("\"", word, "\"", " appears in ", len(matches), " locations", sep="")
            for match in matches:
                print("Row ", match[0], ": ", "from column ", match[1], " to column ", match[2],  sep="")    

grid = [
    "dkios",
    "kutac",
    "zuyfk",
    "ncatf",
    "yudog"
    ]

for line in grid:
    for char in line:
        print(" ", char, sep="", end="")
    print()

word = input("What word would you like to find in this puzzle? ")

searchGrid(grid, word)
