import PuzzleBoard
from PuzzleBoard import *



"""
    Name: TreeNode
    Description: This function represents an instance of a Node in the search tree formed
                 during A* search.
"""
class TreeNode():

    #The current TreeNode's child nodes
    children = []

    #The state of the current TreeNode as its associated PuzzleBoard
    state = None

    #The parent TreeNode to the current one, if one exists
    parent = None

    #The depth of the current TreeNode
    depth = 0

    #Constructor for TreeNode objects
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



    """
        Name: getDepth
        Description: Getter function for the current TreeNode's depth.
    """
    def getDepth(self):
        return self.depth



    """
        Name: getParentNode
        Description: Getter function for the current TreeNode's parent node, if one exists.
    """
    def getParentNode(self):
        return self.parent



    """
        Name: getState
        Description: Getter function for the current TreeNode's state or PuzzleBoard.
    """
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



    """
        Name: setDepth
        Description: Setter function for the current TreeNode's depth.
    """
    def setDepth(self, depth):
        self.depth = depth



    """
        Name: setParentNode
        Description: Setter function for the current TreeNode's parent node.
    """
    def setParentNode(self, parent):
        self.parent = parent



    """
        Name: stateToNode
        Description: This function converts the passed successor PuzzleBoards to TreeNodes.
                     The successor nodes are also added to this TreeNode's list of children.

        Parameter: successors               The list of successor PuzzleBoards to a passed PuzzleBoard.
    """
    def stateToNode(self, successors):

        #The list of TreeNodes to return
        nodes = []

        #The number of successors passed
        numSuccessors = len(successors)

        #Iterate through the list of successor nodes, and add each to the list to return and to this TreeNode's children
        for i in range(numSuccessors):
            newNode = TreeNode(successors[i], self)
            nodes.append(newNode)
            self.children.append(newNode)

        return nodes