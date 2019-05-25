import csv
import RecordEditFunctions
import RecordQueryFunctions
from RecordEditFunctions import createRecord
from RecordEditFunctions import loadRecordList
from RecordEditFunctions import removeRecord
from RecordEditFunctions import saveRecordList
from RecordEditFunctions import sortRecordList
from RecordQueryFunctions import listRecordsByArtist
from RecordQueryFunctions import listRecordsWithDuplicates
from RecordQueryFunctions import printTotalRecordCount
from RecordQueryFunctions import printUniqueRecordCount



"""
    Name: runListEditMenu
    Description: This function runs the record list editing submenu to modify and manage the passed list of records.

    No parameters
    No return value
"""
def runListEditMenu(records):

    #The user's choice for the edit submenu
    editChoice = ""

    #Run the edit list menu until the user exits
    while (editChoice != "4"):
        print("Edit Menu: Select one of the options below.")
        print("1: Add a record to the list.")
        print("2: Remove a record from the list.")
        print("3: Save record list.")
        print("4: Return to main menu")

        #Get the user's menu choice
        editChoice = input()

        #MENU OPTION ONE: Add record to list
        if editChoice == "1":
            createRecord(records)

        #MENU OPTION TWO: Remove record from list
        elif editChoice == "2":
            removeRecord(records)

        #MENU OPTION THREE: Save the current record list to a file
        elif editChoice == "3":
            saveRecordList(records)

        #MENU OPTION FOUR: Return to the main menu
        elif editChoice == "4":
            print("Returning to main menu.")

        #Invalid menu options are ignored
        else:
            print("Invalid selection. Please try again.")

        #Print a newline between menu options
        print("")



"""
    Name: runListQueryMenu
    Description: This function runs the record list query submenu to get information about a list of records.

    No parameters
    No return value
"""
def runListQueryMenu(records):

    queryChoice = ""

    #Continue to prompt the user until exit
    while (queryChoice != "5"):
        print("Query Menu: Select one of the queries below.")
        print("1: List the records for a given artist.")
        print("2: List all of the records with duplicates.")
        print("3: List the total number of records in the list.")
        print("4: List the number of unique records in the list.")
        print("5: Return to main menu.")

        #Get the user's query choice
        queryChoice = input()

        #MENU CHOICE ONE: List the records for a given artist
        if (queryChoice == "1"):
            listRecordsByArtist(records)

        #MENU CHOICE TWO: List the records with duplicate copies
        elif (queryChoice == "2"):
            listRecordsWithDuplicates(records)

        #MENU CHOICE THREE: Print the total count of records in the list
        elif (queryChoice == "3"):
            printTotalRecordCount(records)

        #MENU CHOICE FOUR: Print the total count of unique records in the list
        elif (queryChoice == "4"):
            printUniqueRecordCount(records)
            
        #MENU CHOICE FIVE: Return to the main menu
        elif (queryChoice == "5"):
            print("Returning to the main menu.")

        #Invalid choices are ignored
        else:
            print("Invalid selection. Please try again.")

        #Print a newline between menu selections
        print("")



""" 
    Name: runMainMenu
    Description: This function runs the main menu until the user decides to exit.

    No parameters
    No return value
"""
def runMainMenu(records):

    #The user's menu selection
    mainChoice = ""

    #Continue to prompt the user until they exit
    while (mainChoice != "4"):
        print("Main Menu: Select one of the options below.")
        print("1: Launch record list editing menu.")
        print("2: Launch record list query menu.")
        print("3: Change record lists.")
        print("4: Exit")

        #Get the user's menu choice
        mainChoice = input()

        #MENU CHOICE ONE: Launch Edit submenu
        if (mainChoice == "1"):
            print("Entering the list edit submenu.\n")
            runListEditMenu(records)

        #MENU CHOICE TWO: Launch Query submenu after sorting the record list
        elif (mainChoice == "2"):
            print("Entering the list query submenu.\n")
            sortRecordList(records)
            runListQueryMenu(records)

        #MENU CHOICE THREE: Change Record lists
        elif (mainChoice == "3"):
            print("Would you like to save the current record list first? Y (Yes) or any other key (No)?")
            saveChoice = input()

            #If the user wants to save the list, launch the saveRecordList function
            if (saveChoice == 'Y' or saveChoice == 'y'):
                saveRecordList(records)

            print("Would you like to start a new record list (1) or open an existing one? (2)")
            listChoice = input()

            #If the user wants a new list, clear the list
            if (listChoice == '1'):
                records.clear()

            #If the user wants an existing list, prompt for the file with it
            elif (listChoice == '2'):
                loadRecordList(records)

            #Invalid choices are ignored
            else:
                print("Invalid selection. Please try again.")

        #MENU CHOICE FOUR: Exit the program
        elif (mainChoice == "4"):
            print("Goodbye!")

        #Invalid choices are ignored
        else: 
            print("Invalid selection. Please try again.")

        #Print a newline between menu selections
        print("")



"""
    Name: runStartupMenu
    Description: This function is launched on program execution and prompts the user with a simple menu to manage a record list.

    No parameters
    No return value
"""
def runStartupMenu():

    #The list of records to be manipulated
    records = []

    #The user startup menu choice
    startupChoice = ""

    #Boolean to check if the user has decided how to initalize the record list
    listInitialized = False

    #Run the startup menu until the user chooses a valid option
    while (listInitialized == False):

        #Startup menu prompt
        print("Welcome to the record management system.")
        print("Please select one of the below options.")
        print("1: Create a new record list.")
        print("2: Load a record list from a file.")

        #Get the user's menu choice
        startupChoice = input()

        #MENU CHOICE ONE: Start a new list
        if (startupChoice == "1"):
            print("New record list selected.\n")
            listInitialized = True

        #MENU CHOICE TWO: Use an existing list
        elif (startupChoice == "2"):
            loadRecordList(records)

            if (len(records) != 0):
                listInitialized = True

        #Invalid choices are ignored
        else:
            print("Invalid selection. Please try again.\n")

    #Run the main menu once the user has started a list
    runMainMenu(records)



#Run the startup menu to begin the program
runStartupMenu()
            





