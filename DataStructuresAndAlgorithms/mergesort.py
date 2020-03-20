"""
    Author: Reed Spratt
    Date: March 20th 2020
    
    Description: This program performs recursive mergesort on an input array of elements and sorts them in ascending order.
                 The input array can successfully sort numbers, characters, or string values.

    Efficiency: O(nlogn)
"""



"""
    Name: mergesort
    Description: This method recursively divides an input array and then merges the divisions sorted in ascending order.

    Parameter: inputArray                       The array of elements to sort
    No return value
"""
def mergesort(inputArray):

    #Divide the input array into two halves
    firstHalf = []
    secondHalf = []

    #Get the number of elements in the passed array
    numElements = len(inputArray)

    #Recur while there are more than one elements in the array
    if (numElements > 1):

        #Copy the first half of the array into the first sub-array
        for i in range(0, int(numElements / 2)):
            firstHalf.append(inputArray[i])
        
        #Copy the second half of the array into the second sub-array
        for j in range(int(numElements / 2), numElements):
            secondHalf.append(inputArray[j])

        #Recursively divide and then merge
        mergesort(firstHalf)
        mergesort(secondHalf)
        merge(inputArray, firstHalf, secondHalf)



"""
    Name: merge
    Description: This function merges the two input subarrays into a single array in ascending order.

    Parameter: sortedArray                  The sorted array of elements
    Parameter: firstHalf                    The first half of the input array elements
    Parameter: secondHalf                   The second half of the input array elements
    No return value
"""
def merge(sortedArray, firstHalf, secondHalf):

    #Loop counters for iterating through each array/sub-array
    i = 0
    j = 0
    k = 0

    #Get the number of elements in each sub-array
    numFirstHalf = len(firstHalf)
    numSecondHalf = len(secondHalf)

    #While both subarrays have elements
    while (i < numFirstHalf and j < numSecondHalf):

        #If the element in the first subarray is less than the one in the second subarray, add it to the sorted array
        if (firstHalf[i] < secondHalf[j]):
            sortedArray[k] = firstHalf[i]
            i = i + 1

        #Else, add the element in the second subarray to the sorted array
        else:
            sortedArray[k] = secondHalf[j]
            j = j + 1

        #Increase the sorted array's loop counter
        k = k + 1

    #If the end of the first subarray was reached, add the rest of the elements in the second subarray
    if (i == numFirstHalf):
        while (j < numSecondHalf):
            sortedArray[k] = secondHalf[j]
            j = j + 1
            k = k + 1

    #Else, add the rest of the elements in the first subarray
    else:
        while (i < numFirstHalf):
            sortedArray[k] = firstHalf[i]
            i = i + 1
            k = k + 1



"""
    Name: mainMenu
    Description: Starting function to run the program.

    No parameters
    No return value
"""
def mainMenu():

    #Prompt for the list of numbers or strings to sort
    print("Please enter the list of values as comma-separated values.")
    inputElements = input("> ")
    print("")

    #Split the input string into its list of numbers
    inputElements = inputElements.split(",")

    print("The unsorted list of elements provided is: " + str(inputElements))
    mergesort(inputElements)

    print("The sorted list of elements provided is: " + str(inputElements))

#Run the program
mainMenu()