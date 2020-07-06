"""
    Author: Reed Spratt
    Date: July 6th 2020

    Description: This program takes either a file containing a chess board configuration, or a series of chess pieces entered from the command line. 
    The position of the king chess piece is used and compared with the rest of the chess pieces (assumed to be on the opposing team), to determine if the king is
    in chedck or not. All positions are recorded using x,y coordinate pairings. Valid coordinates lie between 1 and 8 for both x and y values. 

    Running Notes: If using the command-line entry method, example input would be as follows:

    Please enter each opposing piece's type and position coordinates.\nEnter 'X' when you have provided all the pieces.\n
    Type: Q
    X: 3
    Y: 5   

    Type: B
    X: 4
    Y: 4

    Type: X
    --------------------------------------------------------------------------------------------------------------------------------

    If instead providing a file, a set of 64 characters is expected, with 8 characters per line. An example file can be found in this directory.

    Additional Notes: 
    - The only valid piece types for opposing chess pieces are 'B' (Bishop), 'N' (Knight), 'P' (Pawn), 'Q' (Queen), and 'R' (Rook).
    
    - Some validation checking is done for things such as invalid coordinates or chess piece types, but since this was meant as a simple DCP solution, 
      not everything is checked for. Ex. Opposing Pieces can have the same position as eachother, more than one opposing queen can exist on the board, etc.

    - I may come back to this program to add more error handling, but may not, as it was only meant as a small coding challenge solution
"""

import math



"""
    Description: This function performs the logic checking to see if the king is in check. Rules are used for each
                 type of opposing chess piece. If the king is in check, True is returned. Else, False is returned.

    Parameter: kingPosition     The x and y coordinate pair as the king piece's position on the chess board
    Parameter: opposingPieces   The array of opposing chess pieces
    Return: True or False
"""
def checkForCheck(kingPosition, opposingPieces):

    #Iterate through every opposing piece
    for piece, position in opposingPieces.items():

        #Check for bishop pieces
        if piece[0] == 'B':

            #If the bishop is on a diagonal that intersects with the king, the king is in check
            if abs(kingPosition[0] - position[0]) == abs(kingPosition[1] - position[1]):
                print("Check by a bishop at position: " + str(position))
                return True

        #Check for knight pieces
        elif piece[0] == 'N':

            #If the knight's x-value is 3 away from the king, and its y-value is 1 away from the king, the king is in check
            if abs(kingPosition[0] - position[0]) == 3 and abs(kingPosition[1] - position[1]) == 1:
                print("Check by a knight at position: " + str(position))
                return True

        #Check for pawn pieces
        elif piece[0] == 'P':

            #If the pawn is one position away from the king on a diagonal, the king is in check
            if abs(kingPosition[0] - position[0] == 1) and kingPosition[1] - position[1] == -1:
                print("Check by a pawn at position: " + str(position))
                return True

        #Check for the queen piece
        elif piece[0] == 'Q':

            #If the queen shares an x or y value with the king, the king is in check
            if kingPosition[0] == position[0] or kingPosition[1] == position[1]:
                print("Check by a queen at position: " + str(position))
                return True

            #If the queen is on a shared diagonal with the king, the king is in check
            if abs(kingPosition[0] - position[0]) == abs(kingPosition[1] - position[1]):
                print("Check by a queen at position: " + str(position))
                return True

        #Check for rook pieces
        elif piece[0] == 'R':

            #If a rook shares an x or y value with the king, the king is in check
            if kingPosition[0] == position[0] or kingPosition[1] == position[1]:
                print("Check by a rook at position: " + str(position))
                return True

    #If none of the pieces match the check conditions, the king is safe
    print("The king piece is not in check.")
    return False



"""
    Description: Main menu function for collecting user input for the king chess piece's position, and the opposing chess pieces to be used
                 to validate if the king is in check or not.

    No paramaters
    No return value
"""
def mainMenu():

    #The array of valid chess pieces that can be provided excluding the king
    validPieces = ['B', 'N', 'P', 'Q', 'R']

    #The array of the king chess piece's x and y coordinates
    kingPiece = []

    #The dictionary of opposing chess pieces that maps their type to their coordinates
    whitePieces = {}

    #Variable to hold each new opposing chess piece
    newPiece = ""

    #The number of opposing chess pieces registered so far
    numPieces = 0

    print("Welcome to the Check Checker for Chess program.\nFor running instructions, please view the comments at the top of this program file.\n")
    print("Please select one of the options below: ")
    print("1: Provide a chessboard file to read.")
    print("2: Provide each piece's input positions")
    userInput = input()

    #OPTION ONE: File input method
    if userInput == '1':

        #Boolean to determine if the user provided a valid file
        validFile = False

        #Keep prompting for a valid chess file until the user provides one
        while validFile == False:
            print("Please enter the name of the file to read or 'X' to quit: ")
            chessFile = input()

            #Inform the user if they didn't provide a chess file
            if chessFile == None or chessFile == "":
                print("A chess file must be provided.")

            elif chessFile.upper() == 'X':
                print("Goodbye!")
                return
                
            #Else, open the file if it exists and read the chess board configuration
            else:
                try: 
                    fp = open(chessFile, 'r')

                    #Variable to keep track of how many characters from the chess file have been read
                    numRead = 0

                    #Read up to 64 characters, since a chess board has 8x8 squares
                    while numRead < 64:
                        readChar = fp.read(1)
        
                        #If the end of the file is reached before reading in 64 characters, break out of the loop
                        if not readChar:
                            break

                        #Skip newline characters in the file
                        if readChar == '\n':
                            continue

                        #If the character read is a valid white chess pieces, add it to the list
                        elif readChar in validPieces:
                            pieceName = readChar + str(numPieces)

                            #Calculate the piece's x and y coordinates
                            pieceXCoord = numRead % 8
                            pieceYCoord = math.ceil(numRead / 8)
                            print("Adding a new piece")
                            whitePieces[pieceName] = [pieceXCoord, pieceYCoord]

                        #Else if the piece read is the king piece, save its coordinates
                        elif readChar == 'K':
                            kingXCoord = numRead % 8
                            kingYCoord = math.ceil(numRead / 8)
                            kingPiece = [kingXCoord, kingYCoord]

                        #Increment the number of read characters or positions
                        numRead += 1

                    #Close the input file after reading everything
                    fp.close()

                    #Set validFile to True, to stop looping asking for a file
                    validFile = True

                    #Call the function to check if the king piece is in check
                    checkForCheck(kingPiece, whitePieces)

                except Exception as ex:
                    print("An error occurred while reading the chess file.\nException: " + str(ex) + "\n")

    #OPTION TWO: Command line input method
    elif userInput == '2': 
        print("Please enter the black king chess piece's position coordinates on the chess board:\n")

        #Collect the king chess piece's x and y coordinates.
        try:
            kingXCoord = int(input("X: "))
            kingYCoord = int(input("Y: "))
            kingPiece = [kingXCoord, kingYCoord]
            print("")

        except: 
            print("The king piece coordinates entered are invalid. Vaid range is 1-8 for x and y.\n")
            return
        
        print("Please enter each opposing piece's type and position coordinates.\nEnter 'X' when you have provided all the pieces.\n")

        #Keep collecting pieces until the user enters X as the type
        while newPiece != 'X':

            try:
                newPiece = input("Type: ")

                #If the piece type entered is X, stop prompting for pieces
                if newPiece != 'X':
                    pieceXCoord = int(input("X Coord: "))
                    pieceYCoord = int(input("Y Coord: "))

                    #If the new piece's type isn't in the list of acceptable types, it is invalid
                    if newPiece in validPieces == False:
                        print("The piece type entered is not valid. Valid pieces are: " + str(validPieces))

                    #Else if the new piece isn't in the valid range of the chessboard, it is invalid
                    elif pieceXCoord in range(1,8) == False or pieceYCoord in range(1,8) == False:
                        print("The piece coordinates are not valid. Valid coordinates are between 1-8.")

                    #Else if the new piece is on the same square as the king chess piece, it is invalid
                    elif pieceXCoord == kingXCoord and pieceYCoord == kingYCoord:
                        print("The piece cannot have the same coordinates as the king chess piece.")  

                    #Else, the piece is valid and can be saved
                    else:
                        pieceName = newPiece + str(numPieces)
                        whitePieces[pieceName] = [pieceXCoord, pieceYCoord]
                        numPieces += 1
                        print("The piece entered was invalid and not added to the list of pieces.")

                #Call the function to check if the king piece is in check
                checkForCheck(kingPiece, whitePieces)

            #Exception handler for input errors i.e. improper numerical values, etc.
            except Exception as ex:
                print("The piece entered was invalid and not added to the list of pieces.\nException: " + str(ex))
        


#Run the program by calling the mainMenu function
mainMenu()