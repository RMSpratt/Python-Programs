import Attribute
import Example
import Node
import Scheme
import Sample

from Example import *
from Node import *

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
        Description: The primary recursive method for forming a decision tree optimized by attribute testing.

        Parameter: g                    The group of examples remaining to be sorted
        Parameter: attrib               The list of attributes remaining to be used to split the remaining examples in the decision tree
        Parameter: sMajor               The majority function value in the parent set of examples
        Return: newNode
    """
    def learnDecisionTree(self, g, attrib, sMajor):

        #The list of counts of examples with a specific function value
        funcValueCounts = []

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
        modifiedList = attrib
        modifiedList.remove(b)

        #Iterate through every possible value of the attribute b
        for i in range(b.getNumValues()):

            #Form a subgroup of examples with the specific b value (b = vi)
            subg = self.fileSample.findExamplesWithAttributeValue(g, bIndex, i)

            #Recursively form a subtree with the remaining examples and attributes
            subtr = self.learnDecisionTree(subg, modifiedList, majorityFuncValue)

            #Attach the subtree to the root node, and set the link label that attaches the nodes
            newNode.addChild(subtr)
            subtr.setParent(newNode)
            subtr.setLinkLabel(b.getValueForIndex(i))

        #Return the tree
        return newNode
