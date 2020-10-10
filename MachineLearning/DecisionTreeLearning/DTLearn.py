import Attribute
import Example
import Node
import Scheme
import Sample

from Example import *
from Node import *
from Scheme import *
from Sample import *

class DTLearn:

    #The list of nodes making up the decision tree
    treeNodes = []

    #The number of function values for a particular decision tree learning example
    numFunctionValues = 0

    #The Scheme holding all of the attributes to build the decision tree
    fileScheme = None

    #The Sample holding all of the examples for forming the decision tree
    fileSample = None



    """
        Description: The primary recursive function for forming a decision tree optimized by attribute testing.

        Parameter: g                    The group of examples remaining to be sorted
        Parameter: attrib               The list of attributes remaining to be used to split the remaining examples in the decision tree
        Parameter: sMajor               The majority function value in the parent set of examples
        Return: newNode
    """
    def learnDecisionTree(self, g, attrib, sMajor):

        #The list of counts of examples with a specific function value
        funcValueCounts = [0] * self.numFunctionValues

        #The number of examples in the majority set with a specific function value
        majorityValue = 0

        #The index of the function value as the majority set of examples
        majorityIndex = 0

        #THe tree node to be formed
        newNode = None

        #Base case 1, if there are no examples left, label by the majority function value from the parent
        if (len(g) == 0):
            newNode = Node(sMajor, len(self.treeNodes))
            self.treeNodes.append(newNode)

            return newNode

        #Iterate through each example and get the counts for each distinct function value
        for ex in g:
            funcValue = ex.getFunctionValue()
            funcValueCounts[funcValue] += 1

        #Iterate through each distinct function value and determine the majority
        for i in range(len(funcValueCounts)):

            #If the current function value count exceeds the current majority, update the majority value and index
            if (funcValueCounts[i] > majorityValue):
                majorityValue = funcValueCounts[i]
                majorityIndex = i

        #Base case 2, if all examples in g have the same function value, return a node labeled with that value 
        if (majorityValue == len(g)):
            label = self.fileScheme.getFunctionValue().getValueForIndex(majorityIndex)
            newNode = Node(label, len(self.treeNodes))
            self.treeNodes.append(newNode)

            return newNode

        #Base case 3, if there are no attributes left to test on, but examples remaining with different function values,
        #return a node labeled with the majority function value among the examples
        if (len(attrib) == 0):
            label = self.fileScheme.getFunctionValue().getValueForIndex(majorityIndex)
            newNode = Node(label, len(self.treeNodes))
            self.treeNodes.append(newNode)

            return newNode

        #Get the best attribute to test by
        b = self.fileSample.getAttribute(attrib, g)
        bIndex = self.fileScheme.getIndexOfAttribute(b.getName())

        #Form a new node with the current attribute's name and save it to the list of nodes 
        newNode = Node(b.getName(), len(self.treeNodes))
        self.treeNodes.append(newNode)

        #Get the function value present in the majority of examples
        majorityFuncValue = self.fileScheme.getFunctionValue().getValueForIndex(majorityIndex)

        #Create a modified list of attributes without the best attribute selected
        modifiedList = []
        
        #Add each remaining attribute to the modified list
        for i in attrib:
            modifiedList.append(i)

        #Remove the previously selected best attribute
        modifiedList.remove(b)

        #Iterate through every possible value of the attribute b
        for i in range(b.getNumValues()):

            #Form a subgroup of examples with the specific b value (b = vi)
            subg = self.fileSample.findExamplesWithAttributeValue(g, bIndex, i)

            #Recursively form a subtree with the remaining examples and attributes
            subtr = self.learnDecisionTree(subg, modifiedList, majorityFuncValue)

            #Attach the subtree to the root node, and set the link label that attaches the nodes
            newNode.addChildNode(subtr)
            subtr.setParentNode(newNode)
            subtr.setLinkLabel(b.getValueForIndex(i))

        #Return the tree
        return newNode



    """
        Description: THe function for printing the Decision Tree in its entirety.

        Parameter: The list of nodes to print in the tree
        No return value
    """
    def printDecisionTree(self, nodes):

        #Print the root separately using a separate notation (No parent label or link)
        print(nodes[0].getLabel() + "\n" + str(nodes[0].getIndex()) + "\n")

        #Iterator to go through the remaining nodes to print
        i = 0

        #Iterate through all of the nodes in the list for the tree
        while (i < len(nodes)):

            #Variable to hold the current node to print
            current = nodes[i]

            #If the current node being looked at has child nodes, print them all side by side
            if (current.getNumChildren() > 0):
                parentIndices = ""
                arrowOne = ""
                arrowTwo = ""
                arrowHead = ""
                leafLabel = ""
                leafIndex = ""

                #Get a reference to the current node's children
                currentChildren = []
                
                #Add all of the node's child nodes
                for childNode in current.getChildren():
                    currentChildren.append(childNode)

                #Form a string for each child node
                for j in range(len(currentChildren)):
                    parentIndices += str(currentChildren[j].getParentNodeIndex()) + "\t\t"
                    arrowOne += ("|\t\t")

                    #If the link label name is short, use two tabs
                    if (len(currentChildren[j].getLinkLabel()) < 7):
                        arrowTwo += ("|" + currentChildren[j].getLinkLabel() + "\t\t")
                        
                    #Else, use one tab
                    else:
                        arrowTwo += "|" + currentChildren[j].getLinkLabel() + "\t"

                    arrowHead += "v\t\t"

                    #If the label vname is short, use two tabs
                    if (len(currentChildren[j].getLabel()) < 7):
                        leafLabel += (currentChildren[j].getLabel() + "\t\t")

                    #Else, use one tab
                    else:
                        leafLabel += (currentChildren[j].getLabel() + "\t")

                    #Add the leaf index
                    leafIndex += str(currentChildren[j].getIndex()) + "\t\t"

                #Print all of the tree strings formed
                print(str(parentIndices))
                print(arrowOne)
                print(arrowTwo)
                print(arrowHead)
                print(leafLabel)
                print(str(leafIndex) + "\n")

            i += 1


    
    """
        Description: This function sorts the list of tree nodes found when forming the decision tree.

        No parameters
        No return value
    """
    def sortTreeNodes(self):

        #A variable to hold the list of sorted nodes
        sortedNodes = []

        #Iterate through all of the nodes found in decision tree learning
        for i in range(len(self.treeNodes)):

            #The index to insert the node into the list
            insertIndex = len(sortedNodes)

            #Iterate through the current list of sorted nodes for the proper index to insert the new node
            for j in range(len(sortedNodes)):
                if (self.treeNodes[i].getParentNodeIndex() < sortedNodes[j].getParentNodeIndex()):
                    insertIndex = j
                    break

            #Add the node to the list of sorted nodes
            sortedNodes.insert(insertIndex, self.treeNodes[i])

        #Set the class's list of nodes to the sorted list
        self.treeNodes = sortedNodes



"""
    Description: Main function for running Decision Tree Leaening.

    No parameters
    No return value
"""
def runTreeLearning():

    #Variable to hold the list of attributes read in from the SchemeFile    
    fileAttributes = []

    #Variable to hold the list of examples read in from the DataFile
    fileExamples = []

    #Create a new DTLearn instance for learning the decision tree
    runner = DTLearn()

    print("Please enter the name of the Scheme file to use for learning.")
    schemeFile = input("> ")
    print("")

    #If the user didn't provide an input file, inform them
    if (schemeFile == None or schemeFile == ""):
        print("A scheme file must be provided.")
        return

    print("Please enter the name of the Sample file to use for learning.")
    sampleFile = input("> ")
    print("")

    #If the user didn't provide an input file, inform them
    if (sampleFile == None or sampleFile == ""):
        print("A sample file must be provided.")
        return

    #Load the Scheme with the attributes to use
    runner.fileScheme = Scheme(schemeFile)

    #Load the Sample with the examples to use
    runner.fileSample = Sample(sampleFile, runner.fileScheme.getAllAttributes())

    #Get all of the attributes that were read from the DataFile
    fileAttributes = runner.fileScheme.getNonFunctionAttributes()
    fileExamples = runner.fileSample.getAllExamples()

    #Get the number of possible function values
    runner.numFunctionValues = runner.fileScheme.getFunctionValue().getNumValues()

    #Create the ArrayList of tree nodes
    runner.treeNodes = []

    print("Starting to learn...")

    #Run the Decision Tree learning algorithm
    runner.learnDecisionTree(fileExamples, fileAttributes, None)

    #Sort the list of nodes
    runner.sortTreeNodes()

    #Print the decision tree
    runner.printDecisionTree(runner.treeNodes)


runTreeLearning()