"""
    Name: PuzzleBoard
    Description: This class represents specific PuzzleBoard configurations produced while solving the 8-Puzzle Problem.
                 The configuration of numbers in the board is defined by the 'layout' string.
"""
class PuzzleBoard:

    #The current configuration of the PuzzleBoard including all eight pieces
    layout = []

    #The last move that led to this PuzzleBoard configuration
    lastMove = ""

    #The Manhattan heuristic value of this configuration, as its distance from the goal state or configuration
    heuristicValue = 0

    #ID used for identification purposes when printing the 8-Puzzle solution
    id = -1

    #Constructor for PuzzleBoard objects
    def __init__(self, configuration, parentID):
        self.heuristicValue = 0
        self.id = parentID
        self.layout = []
        self.initializeLayout(configuration)



    """
        Name: calculateHeuristicValue
        Description: This function is used to calculate the estimated cost from the current node to the goal node.
                     This is also referred to as the board's heuristic value.

        Parameter: goalState
        No return value
    """
    def calculateHeuristicValue(self, goalState):

        #Counter variable
        count = 0

        #Iterate through each board index
        for i in range(3):
            for j in range(3):

                #Ignore the hole character
                if (goalState[count] != '0'):

                    #Get the position of the current tile's index in the goal state
                    tilePosition = self.layout.index(goalState[count])

                    #Get the x and y coordinates of the current tile
                    xCoordinate = tilePosition % 3
                    yCoordinate = int(tilePosition / 3)

                    #Increment the current board's heuristic value by manhattan heuristics
                    self.heuristicValue += abs(xCoordinate - j)
                    self.heuristicValue += abs(yCoordinate - i)

                count = count + 1



    """
        Name: getBoardLayout
        Description: Getter function for the board's layout.
    """
    def getBoardLayout(self):
        return self.layout



    """
        Name: getHeuristicValue
        Description: Getter function for the board's heuristic value.
    """
    def getHeuristicValue(self):
        return self.heuristicValue



    """
        Name: getID
        Description: Getter function for the board's id.
    """
    def getID(self):
        return self.id



    """
        Name: initializeLayout
        Description: This function initializes the board's layout to the passed configuration string.
    """
    def initializeLayout(self, configuration):

        count = 0

        while count < 9:
            self.layout.append(configuration[count])
            count = count + 1



    """
        Name: makeMove
        Description: This function configures the Board Layout for every possible move given the current hole placement.
                     If the move can be made, True is returned. Else, False is returned.

        Parameter: movement                 The move to attempt to make
        Return: True or False
    """
    def makeMove(self, movement):

        #Variable to hold the current index of the hole character
        holeIndex = self.layout.index('0')

        #Variables to get the hole's X and Y coordinates
        holeXCoordinate = holeIndex % 3
        holeYCoordinate = int(holeIndex / 3)

        #If the move is a valid left shift
        if (movement == 'L' and holeXCoordinate > 0):

            #Get the new index for the hole character
            swapIndex = holeIndex - 1

            #Swap the hole's from its current index to its new index
            tempSwap = self.layout[swapIndex]
            self.layout[swapIndex] = self.layout[holeIndex]
            self.layout[holeIndex] = tempSwap

            #Record the last move for this board
            self.lastMove = '<'

        #Else if the move is a valid right shift
        elif (movement == 'R' and holeXCoordinate < 2):

            #Get the new index for the hole character
            swapIndex = holeIndex + 1

            #Swap the hole's from its current index to its new index
            tempSwap = self.layout[swapIndex]
            self.layout[swapIndex] = self.layout[holeIndex]
            self.layout[holeIndex] = tempSwap

            #Record the last move for this board
            self.lastMove = '>'

        #Else if the move is a valid upward shift
        elif (movement == 'U' and holeYCoordinate > 0):

            #Get the new index for the hole character
            swapIndex = holeIndex - 3

            #Swap the hole's from its current index to its new index
            tempSwap = self.layout[swapIndex]
            self.layout[swapIndex] = self.layout[holeIndex]
            self.layout[holeIndex] = tempSwap

            #Record the last move for this board
            self.lastMove = '^'

        #Else if the move is a valid downward shift
        elif (movement == 'D' and holeYCoordinate < 2):

            #Get the new index for the hole character
            swapIndex = holeIndex + 3

            #Swap the hole's from its current index to its new index
            tempSwap = self.layout[swapIndex]
            self.layout[swapIndex] = self.layout[holeIndex]
            self.layout[holeIndex] = tempSwap

            #Record the last move for this board
            self.lastMove = 'v'

        #Else, the move is invalid
        else:
            return False

        #Set this board's ID
        self.id = self.id + 1

        #Return that the move was valid
        return True



    """
        Name: printBoard
        Description: This function prints the current board's configuration.
    """
    def printBoard(self):

        #Counter variable
        count = 0

        #Print the last move
        print("Last move: " + self.lastMove)

        #Print each tile in the board's configuration
        for i in range(3):
            for j in range(3):
                print(self.layout[count], end=" ")
                count = count + 1

            print("")
        print("")