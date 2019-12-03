print("Let's combine some words!!")
print()

string1 = input("What's the first word? ")
substring1 = string1[:2]

string2 = input("What's the second word? ")
substring2 = string2[-2:]

print()

string1 = substring2 + string1[2:]
print(string1)

string2 = string2[:-2] + substring1
print(string2)
