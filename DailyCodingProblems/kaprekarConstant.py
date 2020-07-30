"""
    Author: Reed Spratt
    Date: July 30th 2020

    Description: This program determines the number of steps required to convert a four-digit number into Kaprekar's Constant (6174). This number can be formed from any 
                four-digit number excluding those that are solely made of the same digit (These are defined in the invalidNumbers array). In each step leading to getting the number,
                the greatest and smallest numbers are formed using the passed one. Ex. 1234 would produce 4321 and 1234. The difference of these numbers is taken as the result, which is used
                in the next iteration until 6174 is obtained.
    

    Running Notes: To run the program, simply call the findKaprekarConstant function using a passed four-digit number.

    Example: 2024

    Biggest: 4220
    Smallest: 0224
    Current: 3996 (4220 - 0224)

    Biggest: 9963
    Smallest: 3699
    Current: 6264 (9963 - 3699)

    Biggest: 6642
    Smallest: 2466
    Current: 4176 (6642 - 2466)

    Biggest: 7641
    Smallest: 1467
    Current: 6174 (7641 - 1467)
"""



import math 

#Define all numbers with equal digits to be invalid
invalidNumbers = [0000,1111,2222,3333,4444,5555,6666,7777,8888,9999]



"""
    Name: findKaprekarConstant
    Description: This function returns the number of steps required to convert a four-digit number into Kaprekar's Constant.
                 More details are in the program header comment.

    Parameter: currentNum               The current number being used to reach Kaprekar's Constant (6174)
    Return: numIterations
"""
def findKaprekarConstant(currentNum):

    #The number of iterations required to find Kaprekar's Constant
    numIterations = 0

    #If the passed number isn't four digits long, it's invalid and can't be used
    if (currentNum < 1000 or currentNum > 9999 or currentNum in invalidNumbers):
        print("ERROR: Invalid starting number")
        return 0

    #Continue to loop while the current number isn't 6174
    while (currentNum != 6174):

        #The biggest and smallest numbers that can be formed with the current number
        biggestNum = 0
        smallestNum = 0

        #An array of the current number's digits
        currentDigits = []

        #Break the number into its digits
        for i in range(4):
            currentDigits.append(currentNum % 10)
            currentNum = int(currentNum / 10)

        #Create an ascending list of the number's digits
        ascendingList = sorted(currentDigits)

        #Create a descending list of the number's digits
        descendingList = sorted(currentDigits, reverse=True)

        #Form the biggest and smallest numbers using the arrays of digits
        for i in range(4):
            biggestNum += descendingList[i] * pow(10, 3 - i)
            smallestNum += ascendingList[i] * pow(10, 3 - i)

        print("Biggest: " + str(biggestNum))
        print("Smallest: " + str(smallestNum))

        #Increase the number of iterations before reaching the constant
        numIterations += 1

        #Form the new current number  
        currentNum = biggestNum - smallestNum
        print("Current: " + str(currentNum) + "\n")



#Call the function here with a valid number
#findKaprekarConstant(2002)