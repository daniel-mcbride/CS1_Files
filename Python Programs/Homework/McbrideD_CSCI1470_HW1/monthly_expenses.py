#**********************  monthly_expenses.py  *********************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Homework #1
#
# Algorithm:
#   Prompt user for name
#   Prompt user for salary
#   Prompt user for expenses
#   Calculate remaining balance
#   Display user name
#   Display user salary
#   Display remaining balance
#      ...
#**********************************************************

#set all input variables for expenses
name = input("What is your name? ")
salary = input("How much do you make a month? ")
rent = input("What do you pay for rent? ")
grocery = input("How much do you spend on groceries? ")
mobile = input("What is your phone bill? ")
misc = input("How much do you spend on anything not mentioned? ")

#convert all numerical values to integers
salary = int(salary)
rent = int(rent)
grocery = int(grocery)
mobile = int(mobile)
misc = int(misc)

# calculate
expenses = rent + grocery + mobile + misc
balance = salary - expenses

print()
print("Thanks for sharing ", name, "!", sep="")
print("Your monthly income is $", salary, sep="")
print("Your monthly expenses add up to $", expenses, sep="")
print("That leaves you with $", balance, " left for the month", sep="")
