#***************  McbrideD_CSCI1470_HW4.py  ***************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Homework #4
#
# Algorithm:
#   Start
#   Prompt user for weight of competitors
#   Check weight and End if 0 or negative
#   Sort weight into a category
#   Repeat all above steps until loop is broken
#   Sort weights again
#   Print weights by category
#   Calculate and print average weight of competitors
#**********************************************************

competitors = 0

welterweights = []
lightweights = []
featherweights = []
bantamweights = []
tooHigh = []
tooLow = []

boxerWeight = input(
"""Please give the weights of competitors (In Kg)
A negative number or 0 will complete the list
What is the weight of the first competitor? """)
boxerWeight = int(boxerWeight)

while boxerWeight > 0:
    if boxerWeight < 51:
        tooLow.append(boxerWeight)
    elif boxerWeight <= 54:
        bantamweights.append(boxerWeight)
        competitors += 1
    elif boxerWeight <= 57:
        featherweights.append(boxerWeight)
        competitors += 1
    elif boxerWeight <= 60:
        lightweights.append(boxerWeight)
        competitors += 1
    elif boxerWeight <= 64:
        welterweights.append(boxerWeight)
        competitors += 1
    else:
        tooHigh.append(boxerWeight)

    boxerWeight = int(input("What is the weight of the next competitor? "))

if len(tooHigh) > 0:
    print("Disqualified for going over weight:",len(tooHigh))

if len(tooHigh) > 0:
    print("Disqualified for failing to meet minimum weight:",len(tooLow))

if len(bantamweights) > 0:
    if len(bantamweights) == 1:
        featherweights.append(bantamweights.pop(0))
    else:
        print("Bantamweights:", len(bantamweights))

if len(featherweights) > 0:
    if len(featherweights) == 1:
        lightweights.append(featherweights.pop(0))
    else:
        print("Featherweights:", len(featherweights))

if len(lightweights) > 0:
    if len(lightweights) == 1:
        welterweights.append(lightweights.pop(0))
    else:
        print("Lightweights:", len(lightweights))

if len(welterweights) > 0:
    print("Welterweights:", len(welterweights))

bantamSum = 0
featherSum = 0
lightSum = 0
welterSum = 0

for boxer in bantamweights:
    bantamSum += boxer

for boxer in featherweights:
    featherSum += boxer

for boxer in lightweights:
    lightSum += boxer

for boxer in welterweights:
    welterSum += boxer

competitorSum = bantamSum + featherSum + lightSum + welterSum
competitorAverage = int(competitorSum / competitors)

print("The average weight of the competition is ", competitorAverage, "Kg", sep="")
