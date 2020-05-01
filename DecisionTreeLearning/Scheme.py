import Attribute
from Attribute import *

class Scheme:

    #The list of non-function value attributes read from the SchemeFile
    attributes = []

    #The function value attribute
    functionValue = None

    def __init__(self, schemeFile):
        self.attributes = []
        
        #Read all of the attributes from the passed scheme file
        self.readSchemeFile(schemeFile)



    #Getter functions
    def getAllAttributes(self):
        combinedAttributes = []

        #Add all of the non-function attributes
        for attribute in self.attributes:
            combinedAttributes.append(attribute)

        #Add the function attribute
        combinedAttributes.append(self.functionValue)

        return combinedAttributes

    def getFunctionValue(self):
        return self.functionValue

    def getNonFunctionAttributes(self):
        return self.attributes



    """
        Description: This function gets the index of a specified attribute as it was loaded from the SchemeFile.

        Parameter: name
        Return: index or -1
    """
    def getIndexOfAttribute(self, name):

        for i in range(len(self.attributes)):

            if (self.attributes[i].getName() == name):
                return i

        return -1



    """
        Description: This function loads all of the attributes to be used for learning the Decision Tree from a scheme file.

        Parameter: schemeFile
        Return: No return value 
    """
    def readSchemeFile(self, schemeFile):
        
        #Variable to hold each read line from the file
        fileLine = ""

        try:

            #The number of attributes read from the scheme file
            numSchemeAttributes = 0

            #Variables to hold information associated with each attribute
            attributeName = ""
            attributeNumValues = ""
            attributeValues = ""

            #Read the entire scheme file
            with open(schemeFile, "r") as fp:
                
                fileLine = fp.readline()

                numSchemeAttributes = int(fileLine)
                
                fileLine = fp.readline()

                #Read in all of the non-function value attributes
                for i in range(numSchemeAttributes - 1):
                    attributeName = fp.readline()
                    attributeName = attributeName.strip()
                    attributeNumValues = fp.readline()
                    attributeNumValues = attributeNumValues.strip()
                    attributeValues = fp.readline()
                    attributeValues = attributeValues.strip()
                    fp.readline()

                    readAttribute = Attribute(attributeName, int(attributeNumValues), attributeValues)

                    if (readAttribute.getValues() == None):
                        print("One or more of the attributes in the SchemeFile was invalid.")
                        fp.close()
                        exit(1)

                    self.attributes.append(readAttribute)

                #Read in the function value information
                attributeName = fp.readline()
                attributeName = attributeName.strip()
                attributeNumValues = fp.readline()
                attributeNumValues = attributeNumValues.strip()
                attributeValues = fp.readline()
                attributeValues = attributeValues.strip()

                #Create the function value attribute and add it to the list of attributes
                functionAttribute = Attribute(attributeName, int(attributeNumValues), attributeValues)
                self.functionValue = functionAttribute

                fp.close()

        #Inform the user if the file couldn't be found
        except FileNotFoundError:
            print("The scheme file " + schemeFile + " could not be found.")
            exit(1)

        #Inform the user if an error occurred while reading the file
        except IOError:
            print("An error occurred while reading the scheme file " + schemeFile)
            exit(1)

        except:
            print("Another error occurred.")


    """
        Description: This utility function prints out all of the attributes' information read from the SchemeFile.

        No parameters
        No return value
    """
    def printAllAttributes(self):
        
        print("Non-function value attributes: ")
        for attrib in self.attributes:
            attrib.printAttributeInfo()

        print("Function value attribute: ")
        self.functionValue.printAttributeInfo()

        print("")