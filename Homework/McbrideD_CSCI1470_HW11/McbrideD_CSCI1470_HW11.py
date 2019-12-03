#***************  McbrideD_CSCI1470_HW11.py  ***************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Homework #11
#
# Algorithm:
#   Start
#   
#**********************************************************

import re

contactsFile = open( "findPhoneCC.txt", "r")

phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
emailRegex = re.compile(r".*@.*\.com|.*@.*\.edu|.*@.*\.org|.*@.*\.gov")
chargebackRegex = re.compile(r"\d\d\d\d")

contactsList = []

for line in contactsFile:
    phone = None
    email = None
    chargeback = None
    
    lineparts = line.split("\t")
    for part in lineparts:        
        if emailRegex.search(part) != None:
            phone = str(part)
        elif phoneRegex.search(part) != None and len(part) == 12:
            email = str(part)
        elif chargebackRegex.search(part) != None and len(part) == 4:
            chargeback = str(part)

    lineList = []
    lineList.append(phone)
    lineList.append(email)
    lineList.append(chargeback)

    contactsList.append(lineList)

contactsList[0] = ["Email", "Phone", "Chargeback#"]

newContactsFile = open("refinedContacts.txt", "w+")

for lineList in contactsList:
    email = lineList[0]
    if email == None:
        email = "None"
    phone = lineList[1]
    if phone == None:
        phone = "None"
    chargeback = lineList[2]
    if chargeback == None:
        chargeback = "None"

    newLine = email + "\t" + phone + "\t" + chargeback + "\n"

    newContactsFile.write(newLine)

newContactsFile.close()

