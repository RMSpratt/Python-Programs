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



    #Getter methods
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
        return self.parent.getIndex()



    #Setter methods
    def setLinkLabel(self, linkLabel):
        self.linkLabel = linkLabel

    def setParentNode(self, parent):
        self.parent = parent
        self.parentIndex = parent.getIndex()



    """
        Description: This method adds the passed child Node to this Node's list of children.

        Parameter: child                        The new child node to be added
        No return value
    """
    def addChildNode(self, child):
        self.children.append(child)
