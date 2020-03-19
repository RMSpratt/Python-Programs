"""
    Name: findLeastCoins
    Description: This function determines the least amount of coins needed to make change for the provided
                 amount of change. This function will check for an invalid target amount.

    Parameter: targetChange                     The target amount of change to reach
    Return: numberCoins
"""
def findLeastCoins(targetChange):

    #The least number of coins that can be used to reach the target amount
    numberCoins = 0

    #Variable to hold the remaining amount of change to reach after every coin denomination is used
    remainingAmount = targetChange

    #If the amount to reach is negative, it's invalid
    if (remainingAmount < 0):
        print("The passed target amount to reach is invalid.")

    #If the amount to reach is greater than 24c, determine the number of quarters to use
    if (remainingAmount > 24):
        numberCoins += int(remainingAmount / 25)
        remainingAmount = remainingAmount % 25

    #If the amount to reach is greater than 9c, determine the number of dimes to use
    if (remainingAmount > 9):
        numberCoins += int(remainingAmount / 10)
        remainingAmount = remainingAmount % 10

    #If the amount to reach is greater than 4c, determine the number of nickels to use
    if (remainingAmount > 4):
        numberCoins += int(remainingAmount / 5)
        remainingAmount = remainingAmount % 5

    #If the amount to reach is greater than 0, determine the number of pennies to use
    if (remainingAmount > 0):
        numberCoins += remainingAmount

    return numberCoins



"""
    Name: mainMenu
    Description: Starting function to run the program.

    No parameters
    No return value
"""
def mainMenu():

    try:
        print("Please enter the number of cents to reach.")
        numCents = int(input("> "))
        print("")

    except:
        print("The number of cents provided is invalid.")
        return

    #If the number of change provided to reach is valid, find the least amount of coins to reach it
    minCoins = findLeastCoins(numCents)
    print("The minimum number of coins to reach " + str(numCents) + " is: " + str(minCoins))    


mainMenu()