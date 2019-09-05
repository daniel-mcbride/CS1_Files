#Generation program

print("Represent the day of the week as 0-6")
print("0 is Sunday, 1 is Monday etc.")
print()
dayOfWeek = input("What day of the week is it? ")
dayOfWeek = int(dayOfWeek)

dayDict = {
    0 : "Sunday",
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday"
}

print()

if dayOfWeek < 0 or dayOfWeek > 6:
    print("Sorry, number is out of range.")
else:
    print("It is ", dayDict[dayOfWeek], "!", sep="")
