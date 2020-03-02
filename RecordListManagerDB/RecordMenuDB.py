import csv
import getpass

import RecordEditFunctionsDB
from RecordEditFunctionsDB import addRecord
from RecordEditFunctionsDB import createDatabaseConnection
from RecordEditFunctionsDB import editRecord
from RecordEditFunctionsDB import loadCSVRecordList
from RecordEditFunctionsDB import removeRecord
from RecordEditFunctionsDB import saveRecordListCSV

import RecordQueryFunctionsDB
from RecordQueryFunctionsDB import *



"""
    Name: runMainMenu
    Description: This function runs the main menu until the user decides to exit.

    Parameter: dbConnection         The connection the the database
    Parameter: dbCursor             The cursor object to execute commands on the database
    No return value    
"""
def runMainMenu(dbConnection, dbCursor):
    
    #The user's menu selection
    mainChoice = ""

    #Continue to prompt the user until they exit
    while (mainChoice != "4"):
        print("Main Menu: Select one of the options below.")
        print("1: Launch record list editing menu.")
        print("2: Launch record list query menu.")
        print("3: Switch to another database.")
        print("4: Exit")

        #Get the user's menu choice
        mainChoice = input()
        print("")

        #MENU CHOICE ONE: Launch Edit submenu
        if (mainChoice == '1'):
            print("Entering the list edit menu.")
            runRecordEditMenu(dbConnection, dbCursor)

        #MENU CHOICE TWO: Launch Query submenu
        elif (mainChoice == '2'):
            print("Entering the list query menu.")
            runRecordQueryMenu(dbConnection, dbCursor)

        #MENU CHOICE THREE: Prompt to switch to another database
        elif(mainChoice == '3'):
            print("Not implemented yet.")

        #MENU CHOICE FOUR: Exit the program
        elif (mainChoice == '4'):
            print("Goodbye!")
            dbCursor.close()
            dbConnection.close()
            return

        #Invalid options are ignored
        else:
            print("Invalid selection. Please try again.")



"""
    Name: runRecordEditMenu
    Description: This function runs the record list editing submenu to modify and manage the list of records in the database.

    Parameter: dbConnection         The connection the the database
    Parameter: dbCursor             The cursor object to execute commands on the database
    No return value
"""
def runRecordEditMenu(dbConnection, dbCursor):
    
    #The user's choice for the edit submenu
    editChoice = ""

    #Run the edit list menu until the user exits
    while (editChoice != "6"):
        print("Edit Menu: Select one of the options below.")
        print("1: Add a record to the list.")
        print("2: Remove a record from the list.")
        print("3: Change a record's manufacturing label.")
        print("4: Change a record's release year.")
        print("5: Save record list to a csv file.")
        print("6: Return to main menu")

        #Get the user's selection
        editChoice = input()
        print("")

        #MENU OPTION ONE: Add a record to the list
        if (editChoice == '1'):
            addRecord(dbConnection, dbCursor)

        #MENU OPTION TWO: Remove a record from the list
        elif (editChoice == '2'):
            removeRecord(dbConnection, dbCursor)

        #MENU OPTION THREE: Update a record's manufacturing label
        elif (editChoice == '3'):
            editRecord(dbConnection, dbCursor, "Label")

        #MENU OPTION FOUR: Update a record's release year
        elif (editChoice == '4'):
            editRecord(dbConnection, dbCursor, "Year")

        #MENU OPTION FIVE: Save the record list to a csv file
        elif (editChoice == '5'):
            saveRecordListCSV(dbConnection, dbCursor)

        #MENU OPTION SIX: Return to the main menu
        elif (editChoice == '6'):
            print("Returning to the main menu.")

        #Invalid options are ignored
        else:
            print("Invalid selection. Please try again.")

        #Print a newline between selections
        print("")



"""
    Name: runRecordQueryMenu
    Description: This function runs the record list query submenu to get information about a list of records.

    Parameter: dbConnection         The connection the the database
    Parameter: dbCursor             The cursor object to execute commands on the database
    No return value
"""
def runRecordQueryMenu(dbConnection, dbCursor):
    
    queryChoice = ""

    #Continue to prompt the user until exit
    while (queryChoice != "10"):
        print("Query Menu: Select one of the queries below, or exit.")
        print("1: List the records for a given artist ordered alphabetically.")
        print("2: List the records for a given artist ordered chronologically.")
        print("3: List the artist with the highest number of records in the list.")
        print("4: List all of the records released by a certain record label.")
        print("5: List the records released in a certain year.")
        print("6: List all of the records with duplicates.")
        print("7: List the total number of records in the list.")
        print("8: List the number of unique records in the list.")
        print("9: List the number of unique artists in the list.")
        print("10: Return to main menu.")

        #Get the user's query choice
        queryChoice = input()
        print("")

        #MENU OPTION ONE: List records by artist alphabetically
        if (queryChoice == '1'):

            #Set the query and call the 'executeArtistQuery' function with it
            userQuery = "SELECT record_Name, release_Year, quantity FROM Record WHERE artist_Name = %s ORDER BY record_Name"
            executeArtistQuery(dbConnection, dbCursor, userQuery)

        #MENU OPTION TWO: List records by artist chronologically
        elif (queryChoice == '2'):
            
            #Set the query and call the 'executeArtistQuery' function with it
            userQuery = "SELECT record_Name, release_Year, quantity FROM Record WHERE artist_Name = %s ORDER BY release_Year, record_Name"
            executeArtistQuery(dbConnection, dbCursor, userQuery)

        #MENU OPTION THREE: Get the artist with the highest number of records in the list
        elif (queryChoice == '3'):

            #Set the query and get the artist with the highest record count
            userQuery = "SELECT artist_Name, COUNT(*) FROM Record GROUP BY artist_Name ORDER BY COUNT(*) DESC"
            dbCursor.execute(userQuery)
            queryResult = dbCursor.fetchone()

            print("The artist with the greatest number of records in the list is " + queryResult[0] + " with " + str(queryResult[1]) + " records.")

        #MENU OPTION FOUR: List the records released by a certain record label
        elif (queryChoice == '4'):

            #Set the query and get the records released by the given manufacturing label
            userQuery = "SELECT artist_Name, record_Name, release_Year FROM Record WHERE record_Label = %s ORDER BY artist_Name, record_Name"
            executeLabelQuery(dbConnection, dbCursor, userQuery)

        #MENU OPTION FIVE: List the records released in a certain year
        elif (queryChoice == '5'):
            
            #Set the query and get the records released in the given year
            userQuery = "SELECT artist_Name, record_Name FROM Record WHERE release_Year = %s ORDER BY artist_Name, record_Name"
            retrieveRecordsByYear(dbConnection, dbCursor, userQuery)

        #MENU OPTION SIX: List the records with duplicate copies
        elif (queryChoice == '6'):
            
            #Set the query and get the records with duplicate copies
            userQuery = "SELECT artist_Name, record_Name, quantity FROM Record WHERE quantity > 1 ORDER BY artist_Name, record_Name"
            retrieveDuplicateRecords(dbConnection, dbCursor, userQuery)

        #MENU OPTION SEVEN: Get the total number of records in the record list
        elif (queryChoice == '7'):
            dbCursor.execute("SELECT SUM(quantity) FROM Record")
            totalCount = dbCursor.fetchone()

            print("There are " + str(totalCount[0]) + " records in the list total.")

        #MENU OPTION EIGHT: Get the number of unique records in the record list
        elif (queryChoice == '8'):
            dbCursor.execute("SELECT COUNT(record_ID) FROM Record")
            uniqueCount = dbCursor.fetchone()

            print("There are " + str(uniqueCount[0]) + " unique records in the record list.")

        #MENU OPTION NINE: Get the number of unique artists in the record list
        elif (queryChoice == '9'):
            dbCursor.execute("SELECT COUNT(DISTINCT artist_Name) FROM Record")
            artistCount = dbCursor.fetchone()

            print("There are " + str(artistCount[0]) + " distinct artists in the record list.")

        #MENU OPTION TEN: Return to the main menu
        elif (queryChoice == '10'):
            print("Returning to main menu.")

        else:
            print("Invalid selection. Please try again.")

        print("")



"""
    Name: runStartupMenu
    Description: This function is launched on program execution and prompts the user with a simple menu to manage a record list.

    No parameters
    No return value
"""
def runStartupMenu():

    #The user startup menu choice
    startupChoice = ""

    #Boolean to check if the user has decided how to initalize the record list
    listInitialized = False

    #Variable to hold the connection to the database
    dbConnection = None

    #Program startup prompt
    print("Welcome to the Record List Manager with Database Storage Functionality.")
    print("You must connect to a database before using this program, so please enter the following information.\n")

    #Collect all of the SQL Database information to establish a connection
    print("Please enter your mysql host name.")
    dbHost = input()
    print("")

    print("Please enter your mysql user name.")
    dbUser = input()
    print("")

    print("Please enter your mysql password.")
    dbPass = getpass.getpass(prompt="Pass: ")
    print("")

    print("Please enter the name of the database you are using.")
    dbName = input()
    print("")

    #Try to connect to the database with the given information
    dbConnection = createDatabaseConnection(dbHost, dbUser, dbPass, dbName)

    #If the database connection was made, continue executing
    if (dbConnection):
    
        #Create the database cursor for modifying the database
        dbCursor = dbConnection.cursor(buffered=True)

        #Run the startup menu until the user chooses a valid option
        while (listInitialized == False):

            #Startup menu prompt
            print("Welcome to the record management system.")
            print("Please select one of the below options.")
            print("1: Create a new records list. (Any existing 'RECORD' table is overwritten).")
            print("2: Use the existing record list in the database.")
            print("3: Load a record list from a csv file into the database. (Any existing 'RECORD' table is overwritten).")
            print("4: Exit the program.")

            #Get the user's menu choice
            startupChoice = input()
            print("")

            #OPTION ONE: Create a new record list in the database
            if (startupChoice == '1'):

                #Drop the RECORD table in the database if it exists, and create a new table to replace it
                dbCursor.execute("DROP TABLE IF EXISTS RECORD")
                dbCursor.execute('''CREATE TABLE RECORD (record_id INT AUTO_INCREMENT, artist_Name VARCHAR(100) NOT NULL, record_Name VARCHAR(100) NOT NULL, 
                                record_Label VARCHAR(100), release_Year VARCHAR(5), quantity INT NOT NULL, additional_Info VARCHAR(100), PRIMARY KEY(record_id))
                                ''')

                #Commit the changes
                dbConnection.commit()

                #Proceed to the main menu
                listInitialized = True

            #OPTION TWO: Use an existing record list in the database
            elif (startupChoice == '2'):

                #Verify the database has a RECORD table
                try:
                    dbCursor.execute("SELECT * FROM RECORD")
                    listInitialized = True
            
                #If it doesn't, this database can't be used for an existing list
                except:
                    print("The database " + dbName + " does not have an existing RECORD table, and can not be used for an existing list.")
                    print("Please try again.\n")

            #OPTION THREE: Use an existing record list from a csv file
            elif(startupChoice == '3'):
                loadCSVRecordList(dbConnection, dbCursor)

                #Proceed to the main menu
                listInitialized = True

            #OPTION FOUR: Exit the main menu
            elif(startupChoice == '4'):
                print("Goodbye!")
                dbCursor.close()
                dbConnection.close()
                return

        #Once the list has been initialized, (new or existing), start the main menu
        runMainMenu(dbConnection, dbCursor)

#Run the startup menu to begin the program
runStartupMenu()
