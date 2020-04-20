import PuzzleBoard
from PuzzleBoard import *

class TreeNode():

    children = []

    state = None
    parent = None

    depth = 0

    def __init__(self, state, parent = None):
        self.children = []
        self.depth = 0
        self.state = state

        #If a parent Node was provided, set it for the current TreeNode
        if (parent != None):
            self.parent = parent
            self.depth = parent.getDepth() + 1



    """
        Name: isRootNode
        Description: This function returns if the current node is the root node in a search tree or not.

        No parameters
        No return value
    """
    def isRootNode(self):

        #If this Node doesn't have a parent Node, it is a root node
        if (self.parent == None):
            return True

        #Else, it is not a root node
        return False

    def getDepth(self):
        return self.depth

    def getParentNode(self):
        return self.parent

    def getState(self):
        return self.state




    """
        Name: getPathFromRoot
        Description: This function generates the list of nodes that led to the current node from the root.

        No parameters
        Return: nodeList 
    """
    def getPathFromRoot(self):

        #The list of nodes to be returned
        nodeList = []

        #An iterator to go through the nodes from root to current
        iterator = self

        #Get all of the nodes leading to the root and add them to the list
        while (iterator.isRootNode() == False):
            nodeList.insert(0, iterator)
            iterator = iterator.getParentNode()

        #Add the root node
        nodeList.insert(0, iterator)

        return nodeList



    """
        Name: printNode
        Description: Utility function to print the current node's state and depth information.

        No parameters
        No return value
    """
    def printNode(self):
        print("Node: dep = " + str(self.depth) + " state: ")
        self.state.printBoard()


    def setDepth(self, depth):
        self.depth = depth

    def setParentNode(self, parent):
        self.parent = parent


    def stateToNode(self, successors):
        nodes = []

        numSuccessors = len(successors)

        childNode = TreeNode(numSuccessors)

        for i in range(numSuccessors):
            newNode = TreeNode(successors[i], self)
            nodes.append(newNode)

            self.children.append(newNode)

        return nodes