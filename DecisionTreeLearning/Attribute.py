"""
    Description: This class represents the attributes used for classifying the input set of examples in the decision tree. 
                 Each attribute has a unique name, along with a list of possible values it can take on. The number of values is also maintained.

                 Functions are primarily getters, including a function to get the index of a specific value for an attribute.
"""
class Attribute:

    #The name of the attribute
    name = ""

    #The number of values the attribute can have
    numValues = 0

    #The list of possible values the attribute can have
    possibleValues = []

    def __init__(self, name, numValues, valueString):
        self.name = name
        self.numValues = numValues
        self.possibleValues = []

        #Parse the possible values this attribute can take on
        self.parseAttributeValues(valueString)



    #Getter functions
    def getName(self):
        return self.name

    def getNumValues(self):
        return self.numValues

    def getValueForIndex(self, index):
        return self.possibleValues[index]

    def getValues(self):
        return self.possibleValues



    """
        Description: This function gets the index of the passed value in this Attribute's list of values, if it exists.
                    If the value is invalid for the attribute, -1 is returned instead.
    
        Parameter: value                     The value string to search for
        Return: index or -1
    """
    def getIndexOfValue(self, value):

        #If the passed value is in the list of possible values for this attribute, 
        if (value in self.possibleValues):
            return self.possibleValues.index(value)

        return -1



    """
        Description: This function parses the input string into a list of possible values for this attribute.
     
        Parameter: valueString              The string containing the values for this attribute
        No return value
    """
    def parseAttributeValues(self, valueString):
        
        #Variable to hold the possible attribute values in the passed string as a list
        passedValues = valueString.split()

        #If the number of passed values doesn't match the amount specified in the file, the attribute is invalid
        if (len(passedValues) != self.numValues):
            print("ERROR: The number of passed values doesn't match the amount required for this attribute.")
            self.possibleValues = None
            return

        #Add all of the possible values for the attribute
        for newValue in passedValues:
            self.possibleValues.append(newValue)

        

    """
        Description: This utility function prints out this attribute's information. (Mostly for debugging purposes.)
     
         No parameters
        No return value
    """
    def printAttributeInfo(self):
        print("Attribute name: " + self.name)
        print("Attribute number of values: " + str(self.numValues))
        print("Attribute values: " + str(self.possibleValues))