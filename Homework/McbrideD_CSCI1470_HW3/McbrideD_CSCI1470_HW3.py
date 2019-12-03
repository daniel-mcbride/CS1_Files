#***************  McbrideD_CSCI1470_HW3.py  ***************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Homework #3
#
# Algorithm:
#   Start
#   Prompt user for item cost & amount tendered
#   Check that amount tendered is enough money
#   Determine Dollars owed
#   Determine Quarters owed
#   Determine Dimes owed
#   Determine Nickels owed
#   Determine Pennies owed
#   Return change to user
#   Prompt the user for another transaction
#   Repeat previous steps if yes
#   End
#**********************************************************

newTransaction = True

while newTransaction == True:
    itemCost = float(input("What is the price of the item? $"))
    amountTendered = float(input("How much money was supplied? $"))

    if itemCost > 5 or amountTendered > 5:
        print("Sorry, no transactions over $5")
    elif itemCost > amountTendered:
        print("Sorry, that's not enough money for the item")
    elif itemCost == amountTendered:
        print("Thank you for providing exact change!")
    else:
        #Converting change to pennies for change calculations
        changeOwed = 100 * round(amountTendered - itemCost, 2)
        changeString = "Your change is:\n"
        
        #Dollars
        dollars = int(changeOwed / 100)
        changeOwed = changeOwed % 100
        if dollars > 0:
            if dollars > 1:
                changeString += str(dollars) + " Dollars\n"
            else:
                changeString += str(dollars) + " Dollar\n"            
        
        #Quarters
        quarters = int(changeOwed / 25)
        changeOwed = changeOwed % 25
        if quarters > 0:
            if quarters > 1:
                changeString += str(quarters) + " Quarters\n"
            else:
                changeString += str(quarters) + " Quarter\n"    

        #Dimes
        dimes = int(changeOwed / 10)
        changeOwed = changeOwed % 10
        if dimes > 0:
            if dollars > 1:
                changeString += str(dimes) + " Dimes\n"
            else:
                changeString += str(dimes) + " Dime\n"    

        #Nickels
        nickels = int(changeOwed / 5)
        changeOwed = changeOwed % 5
        if nickels > 0:
            if nickels > 1:
                changeString += str(nickels) + " Nickels\n"
            else:
                changeString += str(nickels) + " Nickel\n"    

        #Pennies
        pennies = int(changeOwed)
        if pennies > 0:
            if pennies > 1:
                changeString += str(pennies) + " Pennies\n"
            else:
                changeString += str(pennies) + " Penny\n"    

        print(changeString)

    transactionCheck = input("Would you like to try another transaction? (Y/N) ")
    transactionCheck = transactionCheck.lower()
    
    if transactionCheck == "n" or transactionCheck == "no":
        newTransaction = False
    
