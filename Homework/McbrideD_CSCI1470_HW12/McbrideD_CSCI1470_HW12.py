#***************  McbrideD_CSCI1470_HW12.py  ***************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Homework #12
#
# Algorithm:
#   Start
#   
#**********************************************************

message = "This here's obviously more annoying sadly"

def secretMessage(encodedMessage):
    decodedMessage = ""

    words = encodedMessage.split(" ")

    for word in words:
        decodedMessage += word[0]

    return decodedMessage

print(secretMessage(message))

date = "04/19/19"

def dateConverter(numericalDate):
    monthList = ["January", "Febuary", "March", "April", "May", "June", "July",
                 "August", "September", "October", "November", "December"]
    stringDate = ""
    dateParts = numericalDate.split("/")
    
    monthNum = int(dateParts[0])
    month = monthList[monthNum - 1]
    stringDate += month + " "
    
    day = dateParts[1]
    stringDate += day + ", "
    
    year = "20" + dateParts[2]
    stringDate += year

    return stringDate

print(dateConverter(date))
