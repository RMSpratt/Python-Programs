"""
    Author: Reed Spratt
    Date: March 22nd 2020
    
    Description: This program computes an expression in Reverse Polish Notation.

    Limitations: This program treats all operands as integers, so float-values will be rounded.
"""



"""
    Name: solveReversePolishExpression
    Description: This function solves a given expression in Reverse Polish Notation using a stack for storing intermediate numbers.
                 The result of the expression is returned, and all numbers are treated as integer values.

    Parameter: The expression as a list of operands and operators.
    Return: float
"""
def solveReversePolishExpression(expression):

    #List to store the valid operators for evaluating the expression
    validOperators = ['+', '-', '*', '/', '%']

    #List as a stack to store operands
    numberStack = []

    #Variable to store an intermediate result of two operands and an operator
    tempResult = 0

    #Iterate through every term in the expression
    for i in expression:

        #If the list element is an operator, pop the two most recent numbers in the stack
        if (i in validOperators and len(numberStack) >= 2):
            firstNum = numberStack.pop()
            secondNum = numberStack.pop()

            #Add the two numbers
            if (i == '+'):
                tempResult = secondNum + firstNum

            #Subtract the two numbers
            elif (i == '-'): 
                tempResult = secondNum - firstNum

            #Multiply the two numbers
            elif (i == '*'):
                tempResult = secondNum * firstNum

            #Divide the two numbers
            elif (i == '/'):
                tempResult = secondNum / firstNum

            #Modulo the two numbers
            else:
                tempResult = secondNum % firstNum

            #Add the result to the operand stack
            numberStack.append(int(tempResult))

        #Else if the passed number is an operand, save it in the stack
        elif (i.isdigit() == True):
            numberStack.append(int(i))

        #Else, the expression term is invalid
        else:
            print("The passed expression is invalid.")
            return

    #If there isn't a result in the numberStack, the passed expression was empty or invalid
    if (len(numberStack) == 0):
        return 0
    
    #Else, return the final result
    else:
        return numberStack.pop()



"""
    Name: parseExpression
    Description: This utility function removes any whitespace or single quotations from the elements in a list.

    Parameter: expression               The expression as a list of operands and operators.
    No return value
"""
def parseExpression(expression):

    for i in range(len(expression)):
        expression[i] = expression[i].strip()
        expression[i] = expression[i].replace('\'', '')



"""
    Name: mainMenu
    Description: Starting function to run the program.

    No parameters
    No return value
"""
def mainMenu():

    #Variable to store the result of computing the given expression
    finalResult = 0

    #Prompt for and collect the expression to compute
    print("Please enter the expression in Reverse Polish Notation to solve using CSVs. Ex. \'6, 2, -\'")
    inputExpression = input("> ")
    print("")

    #Split the expression into operands and operators, and remove any whitespace or single-quotes
    inputExpression = inputExpression.split(",")
    parseExpression(inputExpression)

    #Get the result of the expression
    finalResult = solveReversePolishExpression(inputExpression)

    #If the function returned a value, display it to the user
    if (finalResult != None):
        print("The final result is: " + str(finalResult))

#Run the main program
mainMenu()