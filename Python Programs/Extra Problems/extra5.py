# !!INCOMPLETE!!
#  word function
#  count consonants
#  print indexes of all vowels

def wordAnalysis(word):
    vowelList = ["a", "e", "i", "o", "u", "y"]
    consonantList = ["b","c","d","f","g","h","k","l","m","n","p","q","r","s","t","v","w","x","z"]

    index = 0

    vowelIndicies = []
    consonantCount = 0

    for letter in word:
        if letter in vowelList:
            vowelIndicies.append(index)
        elif letter in consonantList:
            consonantCount += 1
        index += 1

    #printStr = ""

    for vowelIndex in vowelIndicies:
        print(vowelIndex)

userWord = input("Gimme a word ")

wordAnalysis(userWord)
