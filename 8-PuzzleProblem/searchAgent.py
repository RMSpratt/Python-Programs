import PuzzleBoard
import PuzzleProblem
import TreeNode

from PuzzleBoard import *

from PuzzleProblem import *

from TreeNode import *

def runMain():
    
    searchTree = []
    solution = []

    # print("Please enter the name of the input puzzle file.")
    # puzzleFile = input("> ")

    #Initialize the Puzzle to work with from a given file
    newPuzzle = readPuzzleStates("initGoal.txt")

    if (newPuzzle == None):
        return

    else:
        print("Beginning Search...")

        solution = search(newPuzzle, searchTree)
        print("A goal state was reached.\n")
        print("Search tree size " + str(len(searchTree)) + " nodes")

        showTree(searchTree)
        showSolution(solution)



"""
    Name: insertFringe
    Description: This method inserts the given Node to the list or Fringe in-order with the rest based on heuristic value.

    Parameter: node                     The new node to be inserted into the fringe
    Parameter: nodeList                 The list of nodes or fringe
"""
def insertFringe(node, nodeList):

    #Variable to hold the new Board object to insert into the fringe
    newBoard = node.getState()

    #The current node's function f(n) value
    nodeFValue = node.getDepth() + newBoard.getHeuristicValue()

    #The index to insert the node into the fringe
    insertIndex = 0

    #Iterate through each node in the list
    for listNode in nodeList:

        #Get the board for the current node and its f(n) value
        listBoard = listNode.getState()
        listFValue = listNode.getDepth() + listBoard.getHeuristicValue()

        #If the current list node's function value is smaller than the new node to insert, break out of the list
        if (nodeFValue < listFValue):
            break
        
        #Increment the list's index
        insertIndex = insertIndex + 1

    #Insert the new node into the list at the proper index
    nodeList.insert(insertIndex, node)
        


"""
    Name: readPuzzleStates
    Description: This function reads the initial puzzle and goal puzzle states from the passed input file.

    Parameter: puzzleFile               The file to read the puzzle states from
    No return value
"""    
def readPuzzleStates(puzzleFile):

    filePuzzle = None

    if (puzzleFile == None or puzzleFile == ""):
        print("A puzzle file must be provided.")

    else:
        try:
            readLines = []
            lineCount = 0

            puzzleLine = ""

            with open(puzzleFile, "r") as fp:

                #Read the first file line
                puzzleLine = fp.readline()

                #Read the file until 10 lines have been read
                while (puzzleLine != None and lineCount < 10):

                    #Remove any spaces and newlines in the input lines
                    puzzleLine = puzzleLine.replace(" ", "")
                    puzzleLine = puzzleLine.strip()

                    #Insert the read file line into the list of read lines and increment the count
                    readLines.append(puzzleLine)
                    lineCount = lineCount + 1
                    
                    #Read the next file line
                    puzzleLine = fp.readline()

                #Close the file reader
                fp.close()

                #If the file had the minimum number of lines required in the file, continue
                if (lineCount > 8):
                    initPuzzle = readLines[1] + readLines[2] + readLines[3]
                    goalPuzzle = readLines[6] + readLines[7] + readLines[8]

                    #Create boards representing the initial and goal puzzle states
                    initBoard = PuzzleBoard(initPuzzle, 0)
                    goalBoard = PuzzleBoard(goalPuzzle, -1)

                    #Get the Manhattan heuristic value of the initial and goal states
                    initBoard.calculateHeuristicValue(goalBoard.getBoardLayout())
                    goalBoard.calculateHeuristicValue(goalBoard.getBoardLayout())

                    #Set the new Puzzle Problem's initial and goal states
                    filePuzzle = PuzzleProblem()
                    filePuzzle.setInitialState(initBoard)
                    filePuzzle.setGoalState(goalBoard)

                #Else, the file is invalid
                else:
                    print("The passed input file was invalid.")

        except FileNotFoundError:
            print("The file " + puzzleFile + " could not be found and opened.")

        except Exception as ex:
            print("There was an error while reading the file." + str(ex))

    return filePuzzle


def search(problem, searchTree):

    root = TreeNode(problem.getInitialState())

    solution = []

    fringe = []

    searchTree.append(root)
    insertFringe(root, fringe)

    while (len(fringe) != 0):
        print("Fringe size: " + str(len(fringe)))
        print("Visiting: ")

        tempNode = fringe.pop(0)
        tempNode.printNode()

        tempBoard = tempNode.getState()

        if (problem.isGoalState(tempBoard)):
            solution = tempNode.getPathFromRoot()
            return solution
        

        successors = problem.getSuccessors(tempBoard)
        childNodes = tempNode.stateToNode(successors)

        for i in range(len(childNodes)):
            searchTree.append(childNodes[i])
            insertFringe(childNodes[i], fringe)

    return solution



def showSolution(solution):
    
    print("Solution to 8-Puzzle Problem.")

    for i in range(len(solution)):
        solNode = solution[i]
        solNode.printNode()


def showTree(searchTree):

    currDepth = 0

    depthString = ""
    nodeValue = 65
    nodeTag = chr(nodeValue)

    numTags = 1

    rootParent = '-'

    for i in range(len(searchTree)):

        treeNode = searchTree[i]
        treeBoard = treeNode.getState()

        nodeDepth = treeNode.getDepth()
        nodeID = treeBoard.getID()

        if (nodeDepth == currDepth):

            if (nodeID != 0):
                depthString += (nodeTag + "(" + str(nodeID) + " " + str((nodeID - 1)) + "), ")

            else:
                depthString += (nodeTag + "(" + str(nodeID) + " " + rootParent + "), ")

        else:
            depthString = depthString[0: len(depthString) - 2]
            print(depthString)
            depthString = nodeTag + "(" + str(nodeID) + " " + str(nodeID - 1) + "), "
            currDepth += 1

        #Increment the ASCII value for the node to print
        nodeValue += 1
        nodeTag = ""

        if (nodeValue > 90):
            nodeValue = 65
            numTags += 1

        for i in range(numTags):
            nodeTag += chr(nodeValue)

    #Print the final depth string of nodes
    depthString = depthString[0: len(depthString) - 2]
    print(depthString + "\n")

runMain()