"""
    Author: Reed Spratt
    Last Modified: March 25th 2020

    Description: This program searches through a list of integers and returns an array with the counts of subsequent elements 
                 that are greater than the one being compared.

    Efficiency: O(n^2)

    Limitations: This program expects an array of integers, and will treat other data-types as being invalid.
"""



"""
    Name: countSmallerSubsequent
    Description: This function iterates through an unsorted list and counts all of the elements after a given element that
                 have a greater value than the current element.

    Parameter: listElements              The list of elements to find the counts of subsequent elements of
    Return: countArray
"""
def countSmallerSubsequent(listElements):

    #Get the number of elements in the passed list
    numElements = len(listElements)

    #Array to hold the count of the subsequent elements greater than the one being compared
    countArray = []

    #Iterate through every element in the list
    for i in range(numElements):

        #Initialize the count of greater subsequent elements to 0
        numGreater = 0

        #Iterate through every subsequent element in the list
        for j in range(i + 1, numElements):

            #If a subsequent element is smaller than the current one, increase the count
            if (listElements[j] < listElements[i]):
                numGreater = numGreater + 1

        #Append the final count to the array of counts
        countArray.append(numGreater)

    #Return the array of counts
    return countArray



"""
    Name: mainMenu
    Description: Starting function to run the program.

    No parameters
    No return value
"""
def mainMenu():

    #Variable to hold the input list of elements as a csv string
    inputElements = ""

    #The list of elements to search through
    listElements = []

    #Prompt for the list of numbers to search through
    print("Please enter the list of integers as comma-separated values.")
    inputElements = input("> ")
    print("")

    #Split the input string into its list of numbers
    listElements = inputElements.split(",")

    try:
      
        #Make sure that every value in the input list is an integer
        for i in range(len(listElements)):
            listElements[i] = int(listElements[i])

    #Catch any exceptions and display them to the user 
    except Exception:
        print("ERROR: One of the elements provided or index provided is invalid.")
        return

    #Get the closest greater number's index
    countSubsequents = countSmallerSubsequent(listElements)

    print("The array of greater subsequent element counts is below:\n")
    print(str(countSubsequents))


#Start the program
mainMenu()