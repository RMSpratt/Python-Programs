import PuzzleBoard
import PuzzleProblem
import TreeNode

from PuzzleBoard import *
from PuzzleProblem import *
from TreeNode import *




"""
    Name: runMain
    Description: The main function for using A* search to solve the 8-Puzzle Problem. 
"""
def runMain():
    
    #The Search Tree formed through searching
    searchTree = []

    #The Solution found through searching
    solution = []

    #Prompt for the name of the input file  
    print("Please enter the name of the input puzzle file.")
    puzzleFile = input("> ")

    #Initialize the Puzzle to work with from a given file
    newPuzzle = readPuzzleStates(puzzleFile)

    #If the puzzle wasn't initialized, an error occurred in reading the input file. Exit the program.
    if (newPuzzle == None):
        return

    #Else, begin searching
    else:
        print("Beginning Search...")
        solution = search(newPuzzle, searchTree)
        print("A goal state was reached.\n")
        print("Search tree size " + str(len(searchTree)) + " nodes")

        #Display the Search Tree found
        showTree(searchTree)

        #Display the Solution found
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

    #The PuzzleProblem read from a file to be returned
    inputPuzzle = None

    #If the user didn't provide an input file, inform them
    if (puzzleFile == None or puzzleFile == ""):
        print("A puzzle file must be provided.")

    #Else, read the file to initialize the initial and goal states for the Puzzle Problem
    else:
        try:

            #The lines read from the file and the number of lines read
            readLines = []
            lineCount = 0

            #Variable to hold each read line
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
                    inputPuzzle = PuzzleProblem()
                    inputPuzzle.setInitialState(initBoard)
                    inputPuzzle.setGoalState(goalBoard)

                #Else, the file is invalid
                else:
                    print("The passed input file was invalid.")

        except FileNotFoundError:
            print("The file " + puzzleFile + " could not be found and opened.")

        except Exception as ex:
            print("There was an error while reading the file." + str(ex))

    return inputPuzzle



"""
    Name: search
    Description: This function performs A* search using the given PuzzleProblem, and attempts to find a solution to reach the desired goal state.
                 The searchTree is built in this function during search.

    Parameter: problem                  The instance of the 8-Puzzle Problem to perform search on
    Parameter: searchTree               The searchTree to be formed through A* search.
    Return: solution
"""
def search(problem, searchTree):

    #The root of the searchTree as the initial state for the PuzzleProblem
    root = TreeNode(problem.getInitialState())

    #The list of nodes making up the solution to the PuzzleProblem
    solution = []

    #The list of nodes in the fringe to possibly be explored further
    fringe = []

    #Add the root node to the search tree and insert it into the fringe
    searchTree.append(root)
    insertFringe(root, fringe)

    #While the fringe isn't empty, keep searching for a solution
    while (len(fringe) != 0):
        print("Fringe size: " + str(len(fringe)))
        print("Visiting: ")

        #Get the first node in the Fringe, as the most promising TreeNode to explore
        bestNode = fringe.pop(0)
        bestNode.printNode()

        #Get the PuzzleBoard instance associated with the TreeNode
        bestBoard = bestNode.getState()

        #If the PuzzleBoard instance being looked at matches the goal state, get the solution to return
        if (problem.isGoalState(bestBoard)):
            solution = bestNode.getPathFromRoot()
            return solution
        
        #Get the current PuzzleBoard's successors and convert them to TreeNodes
        successors = problem.getSuccessors(bestBoard)
        childNodes = bestNode.stateToNode(successors)

        #Iterate through all of the generated child nodes and add them to the search tree and fringe
        for i in range(len(childNodes)):
            searchTree.append(childNodes[i])
            insertFringe(childNodes[i], fringe)

    return solution



"""
    Name: showSolution
    Description: This function displays the solution found through A* search as the list of nodes from the root to the goal.

    Parameter: solution                 The solution to display
    No return value
"""
def showSolution(solution):
    
    print("Solution to 8-Puzzle Problem.")

    #Print every node in the solution
    for i in range(len(solution)):
        solNode = solution[i]
        solNode.printNode()



"""
    Name: showTree
    Description: This function displays the searchTree formed through A* search.

    Parameter: searchTree               The search tree formed through searching
    No return value
"""
def showTree(searchTree):

    #Variable to maintain the current depth level of nodes being printed
    currDepth = 0

    #The string containing all of the nodes at the current depth level to print
    depthString = ""

    #Variables used to manage distinct alphabetic tags for every node in the search tree
    nodeValue = 65
    nodeTag = chr(nodeValue)

    #The number of alphabetic tags to append to each node, i.e. 1 - A, 2 - AA, 3 - AAA
    numTags = 1

    #The ID of the root parent for a given TreeNode
    rootParent = '-'

    #Iterate through all of the nodes in the searchTree
    for i in range(len(searchTree)):

        #Get the TreeNode to display and its associated Board
        currentNode = searchTree[i]
        currentBoard = currentNode.getState()

        #Get the depth of the current TreeNode and its associated ID
        nodeDepth = currentNode.getDepth()
        nodeID = currentBoard.getID()

        #If the current Node's depth matches the current depth of nodes to print
        if (nodeDepth == currDepth):

            #If this isn't the root node, add the current node's information and the parent node's information
            if (nodeID != 0):
                depthString += (nodeTag + "(" + str(nodeID) + " " + str((nodeID - 1)) + "), ")

            #Else, add the current node's information, and a default parent node tag '-'
            else:
                depthString += (nodeTag + "(" + str(nodeID) + " " + rootParent + "), ")

        #Else, print the depth string with the nodes for the given depth and increase the depth level
        else:
            depthString = depthString[0: len(depthString) - 2]
            print(depthString)
            depthString = nodeTag + "(" + str(nodeID) + " " + str(nodeID - 1) + "), "
            currDepth += 1

        #Increment the ASCII value for the node to print
        nodeValue += 1
        nodeTag = ""

        #If the node value exceeds 'Z', loop back to 'A'
        if (nodeValue > 90):
            nodeValue = 65
            numTags += 1

        #Add the appropriate amount of tags
        for i in range(numTags):
            nodeTag += chr(nodeValue)

    #Print the final depth string of nodes
    depthString = depthString[0: len(depthString) - 2]
    print(depthString + "\n")

#Run the main program for A* search
runMain()