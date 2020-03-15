"""
    Author: Reed Spratt
    Date: March 4th 2020

    Description: This program performs searches for the nearest occurrence of a 'searchWord' from a 'startingWord'.
                 The smallest distance between the two words is returned as the number of words in-between.
                 Ex. A dog and cat where the startingWord is 'dog' and the searchWord is 'cat', 1 is returned.

                 The string passed to search through is split into a list of strings based on a space.

    Effiency: O(n) To search through the entire list of words in the passed string where n is the number of words in the input string.
              This doesn't account for the effiency of some of the built-in functions used.

    Limitations: Punctuation isn't dealt with, i.e. matching "cat" and "cat."
"""



"""
    Name: searchForWord
    Description: This function finds and returns the smallest distance between the passed starting word and the desired search word.
                 This function handles cases with multiple occurrences of the starting word and/or the search word.

    Parameter: inputString              The string to search through
    Parameter: startingWord             The word to start searching from
    Parameter: searchWord               The word to search for
    Return: smallestDistance
"""
def searchForWord(inputString, startingWord, searchWord):

    #The index of the last occurrence of the startingWord
    lastStartIndex = -1

    #The index of the last occurrence of the searchWord
    lastSearchIndex = -1

    #Split the input string into a list of its words
    wordList = inputString.split()

    #Initialize the smallest distance to the number of words in the string
    smallestDistance = len(wordList)

    #Iterate through the list and get the index of every occurrence of the startingWord
    for i in range(len(wordList)):

        #If the word matches the startingWord, save its index in a list
        if (wordList[i] == startingWord):
            lastStartIndex = i

            #If the search word has appeared in the string already, and the distance between this occurrence of the starting word and search word
            #is smaller than the current closest distance, update the new smallest distance
            if (lastSearchIndex != -1 and abs(lastStartIndex - lastSearchIndex) - 1 < smallestDistance):
                smallestDistance = abs(lastStartIndex - lastSearchIndex) - 1

        #If the word matches the searchWord, save its index in a list
        if (wordList[i] == searchWord):
            lastSearchIndex = i

            #If the starting word has appeared in the string already, and the distance between this occurrence of the starting word and search word
            #is smaller than the current closest distance, update the new smallest distance
            if (lastStartIndex != -1 and abs(lastStartIndex - lastSearchIndex) - 1 < smallestDistance):
                smallestDistance = abs(lastStartIndex - lastSearchIndex) - 1

    #If the starting word or search word didn't appear in the string, set the smallest distance to -1
    if (lastStartIndex == -1 or lastSearchIndex == -1):
        smallestDistance = -1

    #Return the smallest distance found
    return smallestDistance



"""
    Name: mainMenu
    Description: Starting function to run the program.

    No parameters
    No return value
"""
def mainMenu():

    #Variables to hold the user input
    inputString = ""
    startingWord = ""
    searchWord = ""

    #Prompt for the string to search for
    print("Please enter the string to search through: ")
    inputString = input("> ")
    print("")

    #Prompt for the word to start searching from
    print("Please enter the starting word to search from: ")
    startingWord = input("> ")
    print("")

    #Prompt for the word to search for
    print("Please enter the search word to search from: ")
    searchWord = input("> ")
    print("")

    #Get the smallest distance between the starting word and search word in the input string
    smallestDistance = searchForWord(inputString, startingWord, searchWord)

    #If the input string didn't contain the starting word or the search word, inform the user
    if (smallestDistance == -1):
        print("The starting word \"" + startingWord + "\" and/or the search word \"" + searchWord + "\" were not present in the input string.")

    #Else, display the smallest distance between the starting word and search word
    else:
        print("The smallest number of words between \"" + startingWord + "\" and the search word \"" + searchWord + "\" is " + str(smallestDistance))
  

mainMenu()