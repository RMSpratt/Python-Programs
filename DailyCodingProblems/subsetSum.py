"""
    Author: Reed Spratt
    Date: March 4th 2020

    Description: This program performs recursive branch and bound to search for a desired sum using a list of positive integers. 
                 All solutions are displayed from within the function, along with any dead-ends reached, with the reason behind the dead-end. 
                 When an element is not added to the subset, -1 is added to the solution subset to represent this.

    Dead-ends: There are three types of dead-ends that indicate undesirable branches, described in detail below:

               Underflow: This dead-end condition indicates that the current subsetSum + the sum of the remaining elements is less than the desired sum.
               Overflow: This dead-end condition indicates that the current subsetSum exceeds the desired sum.
               End of tree: This dead-end condition indicates that the end of the list has been reached without getting the desired sum.
"""



"""
    Name: searchForSusbetsSolutions
    Desctription: This function searches for the desiredSum specified with the passed list of elements using a recursive 
                  branch and bound searching strategy. Undesirable branches before reaching the end of the list are checked and 
                  described in this program's header. This function only prints solutions, and all solutions are returned.

    Parameter: list                 The list of elements to search with
    Parameter: desiredSum           The sum to be reached using some subset of list elements
    Parameter: currentSum           The current sum as the elements in the subset thus far
    Parameter: remainingSum         The remaining maximum possible sum of the remaining elements in the list
    Parameter: currentElement       The current element index being considered in the list
    Parameter: solution             The subset of elements being considered for the desired sum
"""
def searchForSubsetsSolutions(list, desiredSum, currentSum, remainingSum, currentElement, solution):
    
    #If the current sum is equal to the desired sum, print the solution
    if (currentSum == desiredSum):
        print("Found a solution for the sum: " + str(desiredSum))
        print("Solution element list: ")

        #Print each element in the solution
        for el in solution:

            if (el != -1):
                print(str(el), end= " ")

        print("\n")

    #Else if we haven't reached the end of the list, haven't gone past the desiredSum, and can still reach the desiredSum
    #with the remaining elements, continue recurring
    elif (currentElement < len(list) and currentSum < desiredSum and (currentSum + remainingSum) >= desiredSum):

        #Calculate the new remaining sum with the remaining elements
        remainingSum = remainingSum - list[currentElement]

        #Recur once by not adding one the current element to the solution
        solution.append(-1)
        searchForSubsetsSolutions(list, desiredSum, currentSum, remainingSum, currentElement + 1, solution)

        #Pop the most recent element if we reach a dead-end or solution
        solution.pop()

        #Recur once by adding the current element to the solution
        solution.append(list[currentElement])
        searchForSubsetsSolutions(list, desiredSum, currentSum + list[currentElement], remainingSum, currentElement + 1, solution)

        #Pop the most recent element if we reach a dead-end or solution
        solution.pop()



"""
    Name: searchForSusbetsTrace
    Desctription: This function searches for the desiredSum specified with the passed list of elements using a recursive 
                  branch and bound searching strategy. Undesirable branches before reaching the end of the list are checked and 
                  described in this program's header. This function performs a full trace as it searches, and all solutions are returned.

    Parameter: list                 The list of elements to search with
    Parameter: desiredSum           The sum to be reached using some subset of list elements
    Parameter: currentSum           The current sum as the elements in the subset thus far
    Parameter: remainingSum         The remaining maximum possible sum of the remaining elements in the list
    Parameter: currentElement       The current element index being considered in the list
    Parameter: solution             The subset of elements being considered for the desired sum
"""
def searchForSubsetsTrace(list, desiredSum, currentSum, remainingSum, currentElement, solution):
    
    #If the current sum is equal to the desired sum, print the solution
    if (currentSum == desiredSum):
        print("Found a solution for the sum: " + str(desiredSum))
        print("Solution element list: ")

        #Print each element in the solution subset
        for el in solution:

            #Ignore any elements set to -1 (Indicate an element was not added)
            if (el != -1):
                print(str(el), end= " ")

        print("\n")

    #Else if we've reached the end of the tree without getting the desired sum, we've reached a dead-end
    elif (currentElement >= len(list)):
        print("Reached a dead-end. Sum Reached: " + str(currentSum) + " (End of tree)\n")

    #Else if the current sum is greater than the desired sum, we've gone too far
    elif (currentSum > desiredSum):
        print("Reached a dead-end. Sum Reached: " + str(currentSum) + " (Overflow)\n")

    #Else if the current sum + the remaining elements' sum is less than the desired sum, the desired sum can't be reached
    elif (currentSum + remainingSum < desiredSum):
        print("Reached a dead-end. Sum Reached: " + str(currentSum) + " Remaining Sum: " + str(remainingSum) + " (Underflow)\n")

    #Else, keep recurring and searching
    else:

        #Calculate the new remaining sum with the remaining elements
        remainingSum = remainingSum - list[currentElement]

        #Recur once by not adding one the current element to the solution
        print("Don't add element: " + str(list[currentElement]))
        solution.append(-1)
        searchForSubsetsTrace(list, desiredSum, currentSum, remainingSum, currentElement + 1, solution)

        #Pop the most recent element if we reach a dead-end or solution
        print("Backtrack.")
        solution.pop()

        #Recur once by adding the current element to the solution
        print("Add element: " + str(list[currentElement]))
        solution.append(list[currentElement])
        searchForSubsetsTrace(list, desiredSum, currentSum + list[currentElement], remainingSum, currentElement + 1, solution)

        #Pop the most recent element if we reach a dead-end or solution
        print("Backtrack.")
        solution.pop()



"""
    Name: mainMenu
    Description: Main function to prompt for a sum to reach and the list of elements to search through.

    No parameters
    No return value
"""
def mainMenu():

    #Array to hold all of the user-entered elements
    inputElements = []

    #The current element read by the user
    inputElement = 0

    #The desired sum to reach
    inputSum = 0

    #The total sum of the elements 
    totalSum = 0

    #Prompt for the list of elements
    print("Please enter a list of positive integers one by one.\nEnter -1 to stop inputting elements.")

    #Collect elements until a negative number is entered
    while (inputElement >= 0):

        #Validate each element given by the user
        try:
            inputElement = int(input("> "))

            #If the entered element is valid, add it to the list of elements and increase the total sum of the list
            if (inputElement > 0):
                inputElements.append(inputElement)
                totalSum += inputElement

        #Inform the user of any skipped invalid elements
        except:
            print("The element " + str(inputElement) + " is invalid and was not added to the list.")

    print("")

    #Prompt for the desired sum to try and reach using the list
    try:
        inputSum = int(input("Please enter a desired positive integer sum.\n> "))
        print("")

    #If the sum entered was invalid, inform the user and exit the program
    except:
        print("The sum inputted was invalid and could not be used.")
        return

    #Search the list to see if the desired sum can be reached while tracing all movements
    print("Searching with trace.")
    searchForSubsetsTrace(inputElements, inputSum, 0, totalSum, 0, [])
    print("")

    #Search the list to see if the desired sum can be reached and only print solutions
    print("Searching without trace.")
    searchForSubsetsSolutions(inputElements, inputSum, 0, totalSum, 0, [])

mainMenu()