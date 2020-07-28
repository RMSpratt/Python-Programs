"""
    Author: Reed Spratt
    Date: July 28th 2020

    Description: This program solves the problem to see how many 2-person lifeboats are required to save a given amount of people, where each boat can only hold a 
                 certain specified amount of weight. The function to calculate this amount will determine how many boats minimum would be required based on the total weight
                 of every person and the capacity of a single boat. The amount of boats minimum based on the number of people and the 2-person limit to each boat is also calculated.

                 Since both of these values indicate the minimum number of boats required by a different relevant measurement, the maximum of these two values is taken as the true minimum.

    Running Notes: To run the program, simply call the calculateBoatAmount function with an integer (weight) value as the max weight a boat can hold, and an array of integers denoting each passenger's weight.
    
    Example: 
            boatCapacity = 150     
            passengerWeights = [100,30,50,20,70,80,60,120,150,150]

            maxWeight = 830
            minByPerson = 5                            (5 2-person boats are required to carry 10 people).
            minByWeight = 6                            (math.ceil(830 / 150) = 6 boats minimum are required to carry 830 units of weight).
            minBoatsRequired = 6                       (6 is the greater min requirement to 5).
"""

import math 

"""
    Name: calculateBoatAmount
    Description: This function calculates the minimum number of lifeboats required to save a group of people or passengers.
                 The number of people to save and the combined weight of the passengers is considered. More details in top comment.

    Parameter: boatCapacity - The defined weight capacity each boat can hold
    Parameter: passengerWeights - An array of int values indicating each passenger's weight.
"""
def calculateBoatAmount(boatCapacity, passengerWeights):

    #The maximum weight of all of the passengers
    maxWeight = 0

    #The minimum number of boats going by the amount of passengers
    minByPerson = 0

    #The minimum number of boats going by the total weight of the passengers
    minByWeight = 0

    #The minimum number of boats required for the array of passengers passed
    minBoatsRequired = 0
    
    #Error checking for a negative or 0 boat capacity
    if (boatCapacity <= 0):
        print("ERROR: The boat capacity specified is invalid and must be greater than 0.")
        return

    #Add the weight of every passenger to get the total
    for weight in passengerWeights:

        #Error checking for passengers with weight values greater than the boat capacity
        if (weight > boatCapacity):
            print("ERROR: A passenger's weight cannot exceed the boat capacity for this problem.")
            return

        maxWeight += weight

    #Calculate the minimum number of boats required by the weight of the passengers
    minByWeight = math.ceil(maxWeight / boatCapacity)    

    #Calculate the minimum number of boats required by the number of passengers
    minByPerson = math.ceil(len(passengerWeights) / 2)

    #Take the bigger number of the two minimums 
    minBoatsRequired = max(minByPerson, minByWeight)

    print("The number of boats required is: " + str(minBoatsRequired))


#Invoke the function here using the example syntax in the top comment
calculateBoatAmount(100, [100,30,10,20,50,70,100])