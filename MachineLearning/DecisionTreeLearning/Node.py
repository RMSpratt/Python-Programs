"""
    Description: This class is used for creating nodes that make up the decision tree for printing purposes. 
                 Each node represents either a function value as the end classification of examples meeting a list of attributes, or
                 the name of an attribute for further classification.

                 In addition, all of the nodes excluding the root have a link labeled with the node that led to the current node.

                 Methods include getters, setters, and a method for adding child nodes to the current one.
"""
class Node:

    #The list of child nodes for this Node
    children = []

    #The parent node for this Node
    parent = None

    #An index for this Node (for printing purposes)
    index = 0

    #The Node's label value (for printing purposes)
    label = ""

    #The label of the link connecting to this Node (for printing purposes)
    linkLabel = ""

    def __init__(self, label, index):
        self.label = label
        self.index = index
        self.children = []
        self.parent = None
        self.linkLabel = ""



    #Getter functions
    def getChildren(self):
        return self.children

    def getNumChildren(self):
        return len(self.children)

    def getIndex(self):
        return self.index

    def getLabel(self):
        return self.label

    def getLinkLabel(self):
        return self.linkLabel

    def getParentNode(self):
        return self.parent

    def getParentNodeIndex(self):

        if (self.parent != None):
            return self.parent.getIndex()

        return -1



    #Setter functions
    def setLinkLabel(self, linkLabel):
        self.linkLabel = linkLabel

    def setParentNode(self, parent):
        self.parent = parent
        self.parentIndex = parent.getIndex()



    """
        Description: This function adds the passed child Node to this Node's list of children.

        Parameter: child                        The new child node to be added
        No return value
    """
    def addChildNode(self, child):
        self.children.append(child)
