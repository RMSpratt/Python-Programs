"""
    Author: Reed Spratt
    Date: August 9th 2020

    Description: This program determines if two teams of students can be formed where each student in a passed dictionary maps to a list of their enemies. 
                 The teams formed are only valid if there are no enemies on the same team. For example, if two student entries are: 2: [3], 3: [2], these students
                 cannot be present on the same team. 

                 I decided to solve this problem using recursion with a step-by-step breakdown as follows:

                 1) Get the student with the most enemies, or choose one of them arbitrarily in-case of a tie. 
                 2) Place this student on the first team and call the recursive function.
                 3) Form a list of all of the possible students who can still join the first team, (non-enemies of the first team members).
                 4) Iterate through each possible candidate, adding one to the team each time recursively and repeating step 3 until no remaining candidates exist.
                 5) When there are no more candidates for the first team, form the second team as all remaining students.
                 6) If the two teams are valid, a solution has been found. End.
                 7. Else, remove the most recently added team member and repeat steps 3-5 until a solution is found or there are no more possible combinations.

                The reason why I select the student with the most enemies to be the first member of the first team, is because it can result in less iterations as there will
                be less combinations possible to check.

                Ex. Consider the following map input: {0: [3], 1: [2], 2: [1,4], 3:[0,4,5], 4:[2,3], 5:[3]}

                By starting with student 3, you only need to check if two teams can be formed with 3 and its potential candidates, and everyone else.

                Iteration One: [3, 1] --> No more candidates    Team One = [3, 1], Team Two = [0, 2, 4, 5]
                Team Two is invalid, as 2 and 4 are enemies.

                Iteration Two: [3, 2] --> No more candidates    Team One = [3, 2], Team Two = [0, 1, 4, 5]
                Both teams are valid, so this is a valid solution.


    Running Notes: To run the program, simply pass a dictionary of key-value mappings to the initializeTeam function at the bottom of the program.
                   Examples are present below.
"""


"""
    Name: formTeams
    Description: This function recursively searches a dictionary containing students mapped to their enemies (other students), and determines if 
                 the students can be placed on two teams such that no team has mutual enemies on it. If two teams can be formed successfully, they are 
                 printed with their members and the function returns True. Else, False is returned. For more details, see the program description. (Top)

    Parameter: studentEnemyMaps     The dictionary of students mapped to their list of enemies. Constant through each recursive step.
    Parameter: firstTeam            The current students as members of the first team. This changes between recursive steps as a solution is found.
    Return: True or False
"""
def formTeams(studentEnemyMaps, firstTeam):

    #The second team as the students who can't be on the first team
    secondTeam = []

    #The remaining students who could join the first team
    candidates = []

    #All of the first team's enemies collectively
    firstTeamEnemies = []

    #All of the second team's enemies collectively
    secondTeamEnemies = []

    #Iterate through each member of the first team and get all of their enemies
    for member in firstTeam:
        memberEnemies = studentEnemyMaps[member]

        #Ignore duplicate entries
        for enemy in memberEnemies:
            if ((enemy in firstTeamEnemies) == False):
                firstTeamEnemies.append(enemy)
    
    #Form the list of candidates for the first team as any student not on the first team already, and that isn't an enemy of the first team
    for student in studentEnemyMaps.keys():
        if ((student in firstTeamEnemies) == False and (student in firstTeam) == False):
            candidates.append(student)

    #If there are no more candidates for the first team, form the second team with all remaining students, and determine if these two teams work
    if (len(candidates) == 0):

        #Iterate through each student not on the first team
        for student in firstTeamEnemies:
        
            #If the student to be added isn't an enemy of the current students on the second team, add them to the team
            if ((student in secondTeamEnemies) == False):
                secondTeam.append(student)

                #Get the new team member's enemies
                memberEnemies = studentEnemyMaps[student]

                #Add each new member's enemies to the list of the second team's enemies
                for enemy in memberEnemies:
                    if ((enemy in secondTeamEnemies) == False):
                        secondTeamEnemies.append(enemy)
            
            #Else, if the student is an enemy of the existing second team members, they can't be added. This team doesn't work
            else:
                return False 

        #If ALL of the remaining students not on the first team can join the second team, a solution has been found
        print("A solution for these students is: ")
        print("Team one: " + str(sorted(firstTeam)))
        print("Team two: " + str(sorted(secondTeam)))
        print("")
        return True

    #Else, there are still more candidates, iterate through each and try adding it to the first team
    else:
        for candidate in candidates:
            firstTeam.append(candidate)

            #Recurse with the new first team and get the new remaining candidates
            solutionFound = formTeams(studentEnemyMaps, firstTeam)

            #If a solution has been found, return from this function
            if (solutionFound == True):
                return True

            #Else, remove the most recent candidate from the first team and try a new configuration
            else:
                firstTeam.pop()

    return False

            

"""
    Name: initializeFirstTeam
    Description: This function precedes the recursive function by determining which student has the most enemies out of all of the students present.
                 This student is placed on the first team by default which will be used when recurring to see if a team can be formed with this student.
                 More details on this selection are in the program description. (Top)

    Parameter: students         The dictionary mapping each student to their list of enemies.
    No return value
"""
def initializeFirstTeam(students):

    #Variable to hold the most enemies any one student has
    mostEnemies = 0

    #Variable to hold the student with the most enemies (Arbitrarily chosen if more than one students are tied)
    mostEnemiesStudent = -1

    #Iterate through every student and their list of enemies in the passed dictionary
    for student, enemies in students.items():

        #If the current student has more enemies than any previous student, save them as the student with the most enemies
        if (len(enemies) > mostEnemies):
            mostEnemies = len(enemies)
            mostEnemiesStudent = student

    #Call the recursive function to form the two teams if possible passing the first team as the student with the most enemies
    result = formTeams(students, [mostEnemiesStudent])

    #If the function returned False, there is no possible team formation with the passed dictionary
    if (result == False):
        print("There is no team formation possible for these students.\n")

#Put your sample student mappings here
initializeFirstTeam({0: [3], 1: [2], 2: [1,4], 3:[0,4,5], 4:[2,3], 5:[3]})
initializeFirstTeam({0: [3], 1: [2], 2: [1,3,4], 3:[0,2,4,5], 4:[2,3], 5:[3]})
initializeFirstTeam({0: [3], 1: [3], 2: [3], 3:[0,1,2,4,5], 4:[3], 5:[3]})