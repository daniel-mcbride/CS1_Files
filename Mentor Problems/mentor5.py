def double_char(singleString):
    doubleString = ""
    
    for char in singleString:
        doubleString += char + char

    return doubleString

testString = "bubbles"

print(double_char(testString))
