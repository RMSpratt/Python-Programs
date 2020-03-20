"""
    Author: Reed Spratt
    Date: March 20th 2020
    
    Description: This program performs non-recursive binary search for a specific value in an input list of elements.
                 The list provided by the user is pre-sorted using Python's built-in sort() function.

    Efficiency: O(logn) (Not including Python's sort() method)

    Limitations: This program expects the input string of csv to not have whitespace separating each element.
"""



"""
    Name: binarySearch
    Description: This function performs non-recursive binary search on the input list of elements for a specified value.
                 A boolean is returned indicating if the element was found or not.
    Parameter: inputArray                       The array of elements to search through
    Parameter: searchValue                      The value in the array to search for
    Return: True or False
"""
def binarySearch(inputArray, searchValue):

    #If the length of the passed array is 0, return immediately
    if (len(inputArray) == 0):
        return False

    #Variables to hold the left and right indices for searching
    leftIndex = 0
    rightIndex = len(inputArray) - 1

    #Keep searching while the left index is less than or equal to the right index
    while (leftIndex <= rightIndex):

        #Grab the middle index of the left and right indices
        middleIndex = int((leftIndex + rightIndex) / 2) 

        #If the search element has a smaller value than the middle value, decrement the right index
        if (searchValue < inputArray[middleIndex]):
            rightIndex = middleIndex - 1

        #Else if the search element has a larger value than the middle value, increment the left index
        elif (searchValue > inputArray[middleIndex]):
            leftIndex = middleIndex + 1

        #Else, the search element was found
        else:
            return True

    #If the search element wasn't found in the entire input array, return false
    return False
        


"""
    Name: mainMenu
    Description: Starting function to run the program.

    No parameters
    No return value
"""
def mainMenu():

    #Prompt for the list of numbers or strings to sort
    print("Please enter the list of values as comma-separated values with no spaces between.")
    inputElements = input("> ")
    print("")

    #Split the input string into its list of numbers
    inputElements = inputElements.split(",")

    #Sort the input list
    inputElements.sort()

    #Prompt for the value to search for in the list
    print("Please enter the value to search for in the list.")
    searchValue = input("> ")
    print("")

    #Search for the specified value in the list
    foundValue = binarySearch(inputElements, searchValue)

    #If the specified value was found, inform the user
    if (foundValue):
        print("The value " + searchValue + " was found in the input list.")

    #Else, inform the user that the value was not found
    else:
        print("The value " + searchValue + " was not found in the input list.")

#Run program
mainMenu()