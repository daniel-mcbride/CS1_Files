import random

randNums = []
repeatNums = []

for index in range(10):
    newNum = random.randint(1, 10)

    if newNum in randNums:
        repeatNums.append(newNum)

    randNums.append(newNum)    

randSum = 0

print("randNums = [", end="")
for randNum in randNums:
    print(randNum, end=" ")
print("]")

index = 0
for num in randNums:
    randSum += num

    if num in repeatNums:
        print(index, end=" ")

    index += 1

print()
print("The sum is", randSum)
