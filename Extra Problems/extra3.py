rangeCheck = True
userNums = []

print()
print("Let's average a bunch of numbers!")

while rangeCheck == True:
    userNum = input("Give me a number between 1 and 100: ")
    userNum = int(userNum)

    if userNum > 100:
        break
    elif userNum < 1:
        break
    else:
        userNums.append(userNum)

numsSum = 0
numsLength = len(userNums)

for num in userNums:
    numsSum += num

firstAverage = int(numsSum / numsLength)

print("Err: number provided was outside of the range")
print()
print("The average of all valid integers was", firstAverage)
print()

numsSum2 = 0
nums2Length = len(userNums[1:-1])

for num in userNums[1:-1]:
    numsSum2 += num

secondAverage = int(numsSum2 / nums2Length)

print("If you remove the first and last numbers the average is", secondAverage)

