import math

import Attribute
import Example

from Attribute import *
from Example import *

class Sample:

    #The list of attributes present in every example
    schemeAttributes = []

    #The set of examples that make up this sample
    exampleSet = []

    def __init__(self, dataFile, schemeAttributes):
        self.schemeAttributes = schemeAttributes
        self.exampleSet = []

        #Read the DataFile to load the set of examples
        self.readDataFile(dataFile, self.schemeAttributes)



    """
        Description: This function returns a count of the examples with a specific function value.

        Parameter: examples                 The list of examples to search through
        Parameter: value                    The function value being searched here
    """
    def countExamplesWithFunctionValue(self, examples, value):

        #The count of examples in the passed set with the specified function value
        count = 0

        #Iterate through all of the examples in the passed set
        for ex in examples:

            #If the function value of an example matches the desired value, increment the count
            if (ex.getFunctionValue() == value):
                count += 1

        return count



    """
        Description: This function returns a list of examples that have a specified attribute value.

        Parameter: searchExample            The list of examples to search through
        Paramter: attribIndex               The index of the specified attribute to check
        Parameter: value                    The desired value of the attribute to look for
    """
    def findExamplesWithAttributeValue(self, searchExamples, attribIndex, value):

        #The list of examples that had a matching attribute value 
        matchingExamples = []

        #Iterate through the list of examples
        for ex in searchExamples:

            #If the example has the specified attribute value, add it to the list to return
            if ex.getSpecificValue(attribIndex) == value:
                matchingExamples.append(ex)
    
        return matchingExamples



    #Getter function for all of the examples read from the DataFile
    def getAllExamples(self):
        return self.exampleSet



    """
        Description: This function gets the best attribute for testing the remaining examples on in the decision tree.
                     The best attribute is selected by the amount of information gained by testing with it.

        Parameter: attrib                   The list of attributes remaining to test with
        Parameter: g                        The group of examples remaining to test with
        Return: bestAttrib           
    """
    def getAttribute(self, attrib, g):

        #The best attribute to be selected next in the decision tree
        bestAttrib = None

        #The maximum amount of information gainable by splitting the remaining examples with a specific attribute
        maxGain = -1

        #Get the number of possible function values
        k = self.schemeAttributes[len(self.schemeAttributes) - 1].getNumValues()

        #Get the amount of information required to solve the query q before testing with an attribute
        info = self.infoFmGp(g, k)

        #Iterate through every remaining attribute
        for b in attrib:

            #Get the remaining amount of information to answer the query q after testing with the given attribute
            remainder = self.getRmd(b, g, k)

            #Get the amount of information gained after testing with a specific attribute
            gain = info - remainder
            gain = round(gain, 4)

            #Checks for rounding errors
            if (gain < 0):
                gain = 0

            print("Test " + b.getName() + ": info=" + str(info) + " rmd=" + str(remainder) + " gain=" + str(gain))

            #If the amount of information gained is greater than the current maximum amount
            if (gain > maxGain):
                maxGain = gain
                bestAttrib = b

        print("Select attribute " + bestAttrib.getName() + "\n")

        #Return the best attribute
        return bestAttrib



    """
        Description: This function gets the remaining amount of information required to answer a query q after splitting
                     the input group by some attribute b.

        Parameter: b                        The attribute to split the input group of examples by
        Parameter: g                        The input group of examples 
        Parameter: k                        The number of possible function values
        Return: remainder
    """
    def getRmd(self, b, g, k):
        
        #Get the index corresponding with the current attribute
        attribIndex = self.schemeAttributes.index(b)

        #The remaining amount of information required to answer the query after splitting based on attribute b
        remainder = 0

        #Get the number of examples in the subgroup
        size = len(g)

        #The list of examples with a specific value of b (gi)
        subgroup = []

        #The number of examples in the subgroup (gi)
        subcount = 0

        #The number of psosible values the attribute can have
        possibleBValues = b.getNumValues()

        #Iterate through every possible value of the current attribute
        for i in range(possibleBValues):

            #Form a subgroup of examples that have a specific value of b (Group gi)
            subgroup = self.findExamplesWithAttributeValue(g, attribIndex, i)

            #Count the number of examples that fall in the subgroup (gi)
            subcount = len(subgroup)

            #Get the probability of an example from the parent group falling into this subgroup
            probability = subcount / size

            #Get the amount of information obtained from this subgroup
            info = self.infoFmGp(subgroup, k)

            #Get the remaining information required after this subgroup split
            remainder += probability * info
            remainder = round(remainder, 4)

        return remainder



    """
        Description: This function calculates one of two values classified as Task A and Task B respectively.
                     Task A calculates I(P(v1), ..., P(vk))
                     Task B calculates I(P(v1 | b = bi), ..., P(vk | b = bi))

                     Parameter: g           The group of examples to calculate the information value from
                     Parameter: k           The number of possible function values
                     Return: info
    """
    def infoFmGp(self, g, k):
        
        #Variable to hold the size of the input group of examples
        size = len(g)

        #Variable to hold the amount of information required to return
        info = 0

        #The list of counts of examples in each subgroup that the input group of examples is divided into
        exampleCount = []

        #Iterate through each possible function value and count the number of examples in each group
        for i in range(k):
            exampleCount.append(self.countExamplesWithFunctionValue(g, i))

        #Iterate through each possible function value and calculate the probability of an example in g getting into
        #the subgroup gi based on the count
        for j in range(k):
            probability = 0

            #If the size of the subgroup is greater than 0, get the probability of an example ending up in that group
            if (size > 0):
                probability = exampleCount[j] / size

            #Add the amount of information required to solve query q using the new subgroup
            if (probability > 0):
                info = info - probability * (math.log(probability, 2))
                info = round(info, 4)
        
        #Return the amount of information required to solve query q
        return info



    """
        Description: Utility function to print all of the examples registered in this sample.

        No parameters
        No return value
    """
    def printAllExamples(self):
        print("The examples read from DataFile are below.")

        #Print the information for every example
        for ex in self.exampleSet:
            ex.printExampleInfo()

        print("")



    """
        Description: The function reads the passed DataFile to load the list of examples for learning the DecisionTree.

        Parameter: dataFile                 The filepath or file name to open
        Parameter: schemeAttributes         The list of attributes registered from the schemeFile
        No return value 
    """
    def readDataFile(self, dataFile, schemeAttributes):
       
        #The number associated with each example
        exampleNum = 1

        try:

            #Read the sample file in its entirety
            with open(dataFile, "r") as sampleReader:
                headerLine = sampleReader.readline()

                #If the header line's variables are out of order or missing, exit the program
                if (self.verifyHeaderLine(headerLine) == False):
                    print("One or more of the header variables in the data file are out of order or missing.")
                    sampleReader.close()
                    exit(1)

                #Read the first example line in the DataFile
                fileLine = sampleReader.readline()

                #Read every Example from the DataFile
                while (fileLine != None and fileLine != ""):
                    fileLine = fileLine.strip()
                    fileLine = fileLine.replace("\t\t", " ")
                    fileLine = fileLine.replace("\t", " ")
                    fileLine = fileLine.replace(" +", " ")

                    #Create a new Example using the file line
                    dataExample = Example(exampleNum, fileLine, schemeAttributes)

                    #If the example read was invalid, stop reading the file and exit the program
                    if (dataExample.getAttributeValues() == None):
                        sampleReader.close()
                        exit(1)

                    #Else, add the example to the example set
                    else:
                        self.exampleSet.append(dataExample)

                    #Increment the count of the number of examples
                    exampleNum += 1

                    #Read the next example in the file
                    fileLine = sampleReader.readline()

        #If the file couldn't be found, inform the user
        except FileNotFoundError:
            print("The data file " + dataFile + " could not be found")

        #If an error occurred while reading the file, inform the user
        except IOError:
            print("An error occurred while reading the data file " + dataFile)



    """
        Description: This function verifies the header line of variable assignments in the DataFile.
                     The validity of the line is returned as a boolean value.

        Parameter: headerLine               The header line to verify
        Return: True or False
    """
    def verifyHeaderLine(self, headerLine):

        #Variable to hold the list of attributes in the header string
        headerAttributes = []

        #Format the header string
        headerLine = headerLine.strip()
        headerLine = headerLine.replace("\t", " ")
        headerLine = headerLine.replace(" +", " ")

        #Get all of the attributes in the header string
        headerAttributes = headerLine.split(" ")

        #If the number of header attributes doesn't equal the number of attributes in the scheme file, it's invalid
        if (len(headerAttributes) != len(self.schemeAttributes)):
            print(len(headerAttributes))
            print(len(self.schemeAttributes))
            return False

        #Iterate through the list of attributes in the header string and make sure they match the ones read by the scheme file
        for i in range(len(headerAttributes)):

            #If an attribute doesn't match, the header string is invalid
            if (self.schemeAttributes[i].getName() != headerAttributes[i]):
                return False

        #Else, the header string is valid
        return True
