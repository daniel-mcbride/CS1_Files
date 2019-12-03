numSum = 0
count = 1

currentNum = int(input("What is the first grade to add? "))
print("Enter a negative number to STOP")

while currentNum >= 0:
    numSum += currentNum
    count += 1
    currentNum = int(input("Please enter another grade: "))

average = numSum / (count - 1)

print(average)
