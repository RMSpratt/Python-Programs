"""
    Author: Reed Spratt
    Last Modified: March 16th 2020

    Description: This program searches for the nearest occurrence of a number in a list that is greater than the one at the passed index.

    Efficiency: O(1) best-case and O(n) worst-case.
"""



"""
    Name: findClosestGreaterNumber
    Description: This function finds the closest greater number to the one at the passed index. The input list is unsorted.
                 This function searches forwards from the specified element first, and then searches backwards from the specified element.
                 If a greater number isn't found, None is returned instead.

    Parameter: listElements                 The list of elements to search through
    Parameter: startIndex                   The starting index to search from
    Return: greaterIndex or None
"""
def findClosestGreaterNumber(listElements, startIndex):

    #Variable to hold the closest greater number's index
    greaterIndex = -1

    #If the list passed was empty or the start index to search from is invalid, return from the function
    if (len(listElements) == 0 or startIndex > len(listElements) or startIndex < 0):
        return None

    #Get the starting number to find a greater value of
    startNumber = listElements[startIndex]

    #Initialize a loop counter to the passed index
    i = startIndex

    #Iterate forwards through the list for the closest greater number
    while (i < len(listElements)):

        #If a greater value is found, save its index
        if (listElements[i] > startNumber):
            greaterIndex = i
            break

        #Keep searching
        i = i + 1

    #Initialize a loop counter to the passed index
    j = startIndex

    #Iterate backwards through the list for the closest greater number
    while (j > 0):

        #If a greater value is found and its closer to the starting index, save its index
        if (listElements[j] > startNumber and abs(startIndex - j) < abs(startIndex - greaterIndex)):
            greaterIndex = j
            break

        #Keep searching
        j = j - 1

    #If the list didn't contain a number greater than the one passed, return None
    if (greaterIndex == -1):
        return None

    #Return the closest index of the greater number
    return greaterIndex
    


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
    print("Please enter the list of numbers as comma-separated values.")
    inputElements = input("> ")
    print("")

    #Split the input string into its list of numbers
    listElements = inputElements.split(",")

    try:
      
        #Make sure that every value in the input list is an integer
        for i in range(len(listElements)):
            listElements[i] = int(listElements[i])

        #Prompt for and validate the starting index to search from
        print("Please enter the starting index to search from.")
        startIndex = int(input("> "))
        print("")

    #Catch any exceptions and display them to the user 
    except Exception:
        print("ERROR: One of the elements provided or index provided is invalid.")
        return

    #Get the closest greater number's index
    greaterIndex = findClosestGreaterNumber(listElements, startIndex)

    #If a closest greater index was found, display it
    if (greaterIndex != None):
        print("The closest greater number to \"" + str(listElements[startIndex]) + "\" was found at index " + str(greaterIndex) + ".")

    #Else, a closest greater index wasn't found, inform the user
    else:
        print("The list didn't have a greater number than the one specified within it.")



#Start the program
mainMenu()