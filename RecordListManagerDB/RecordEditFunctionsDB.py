import csv
import mysql.connector



"""
    Name: addRecord
    Description: This function adds a new record to the database table, or updates an existing record's quantity
                 if it already exists in the table.

    Parameter: dbConnection         The connection the the database
    Parameter: dbCursor             The cursor object to execute commands on the database
    No return value
    
"""
def addRecord(dbConnection, dbCursor):
    
    #Prompt for the record artist
    newArtist = input("Please enter the record artist.\n")
    print("")

    #Get all of the records in the table for the current artist
    userQuery = "SELECT record_id, record_Name FROM Record WHERE artist_Name = %s"
    dbCursor.execute(userQuery, (newArtist,))

    #The records retrieved from the database table
    currentRecords = dbCursor.fetchall()

    #If there were records for the given artist, list them
    if (len(currentRecords) > 0):
        print("The records by this artist in the list are listed below.")
        print("Please enter the index of the album title below if this is an existing record. Otherwise, 0")

        #Print all of the records
        for i in currentRecords:
            print(i)

        try: 

            #This holds the user's index selection
            addIndex = int(input())
            print("")

            #Loop through all of the rows for the artist
            for j in currentRecords:

                #Check if the user entered a valid index of a row
                if addIndex in j:

                    #Update the row's quantity value to be one greater
                    userQuery = "UPDATE Record SET quantity = quantity + 1 WHERE record_id = %s"
                    dbCursor.execute(userQuery, (addIndex,))
                    dbConnection.commit()
                    print("The record's quantity was successfully updated.")
                    return

            #If the user entered an invalid index, this is a new record
                    
            #Get the album title
            newTitle = input("Please enter the name of the new album.\n")
            print("")

            #Get the manufacturing label
            newLabel = input("Please enter the label that published the record, or 'Unknown'.\n")
            print("")

            try:
                #Make sure the user enters an integer
                newYear = int(input("Please enter the album's release year, or 0 if you don't know the year.\n"))
                print("")

                #Add the record to the database table with the passed information
                userQuery = "INSERT INTO Record (artist_Name, record_Name, record_Label, release_Year, quantity, additional_Info) VALUES (%s, %s, %s, %s, %s, %s)"
                dbCursor.execute(userQuery, (newArtist, newTitle, newLabel, newYear, 1, ""))
                dbConnection.commit()

                #Inform the user on success
                print("The new record " + newTitle + " by " + newArtist + " was added to the list of records.")

            #If the user didn't enter a valid release year, display an error message
            except ValueError:
                print("Invalid release year. The record could not be created.")

            #If there was an error adding the record to the list, inform the user
            except:
                print("There was an error adding the record to the database table. Please try again.")

        #If the user entered a bad index value (non-integer)
        except ValueError:
            print("The index entered was invalid.")

    #Otherwise if the artist had no existing records, prompt the user to create a new record entry
    else: 
        print("There are no records in the list by this artist.")

        #Get the album title
        newTitle = input("Please enter the name of the new album.\n")
        print("")

        #Get the manufacturing label
        newLabel = input("Please enter the label that published the record, or 'Unknown'.\n")
        print("")

        try:
            #Make sure the user enters an integer
            newYear = int(input("Please enter the album's release year, or 0 if you don't know the year.\n"))
            print("")

            #Add the record to the database table with the passed information
            userQuery = "INSERT INTO Record (artist_Name, record_Name, record_Label, release_Year, quantity, additional_Info) VALUES (%s, %s, %s, %s, %s, %s)"
            dbCursor.execute(userQuery, (newArtist, newTitle, newLabel, newYear, 1, ""))
            dbConnection.commit()

            #Inform the user on success
            print("The new record " + newTitle + " by " + newArtist + " was added to the list of records.")

        #If the user didn't enter a valid release year, display an error message
        except ValueError:
            print("Invalid release year. The record could not be created.")

        #If there was an error adding the record to the list, inform the user
        except:
            print("There was an error adding the record to the database table. Please try again.")



"""
    Name: createDatabaseConnection
    Description: This function creates and returns a connection to a mysql database.

    Parameter: dbHost         The database's localhost
    Parameter: dbUser         The database username login
    Parameter: dbPass         The database password
    Parameter: dbName         The name of the database

    Return: The created database connection userDb or None
"""
def createDatabaseConnection(dbHost, dbUser, dbPass, dbName):

    #Try to establish the database connection
    try:  
        userDB = mysql.connector.connect(
            host = dbHost,
            user = dbUser,
            password = dbPass,
            database = dbName
        )

        #Return the database connection if successful
        print("The database was successfully connected to. \n")

        return userDB

    #If something went wrong, inform the user
    except:
        print("The database connection could not be created. Please try again.")
        return None
    


"""
    Name: editRecord
    Description: This function guides the user to modify a record's manufacturing label or release year.

    Parameter: dbConnection         The connection the the database
    Parameter: dbCursor             The cursor object to execute commands on the database
    No return value 
"""
def editRecord(dbConnection, dbCursor, property):

    #Prompt for the name of the artist
    editArtist = input("Please enter the name of the artist.\n")
    print("")

    #Get all of the records in the table for the current artist
    userQuery = "SELECT record_id, record_Name FROM Record WHERE artist_Name = %s"
    dbCursor.execute(userQuery, (editArtist,))

    #The records retrieved from the database table
    currentRecords = dbCursor.fetchall()

    #If there were no records for the artist, return
    if (len(currentRecords) == 0):
        print("There are no records in the list by " + editArtist)
        return

    #Otherwise, list them and prompt for the record selection
    else:
        print("The records by this artist currently in the list are listed below.")
        print("Please enter the index of the album title below to modify it.")

        #Print all of the records
        for i in currentRecords:
            print(i)

        try: 

            #This holds the user's index selection
            editIndex = int(input())
            print("")

            #Loop through all of the rows for the artist
            for j in currentRecords:

                #Check if the user entered a valid index of a row
                if editIndex in j:

                    #If the desired property to change is the manufacturing label
                    if (property == "Label"):
                        newLabel = input("Please enter the record's manufacturing label.\n")
                        print("")

                        #Set the record's manufacturing label to the new one
                        userQuery = "UPDATE Record SET record_Label = %s WHERE record_id = %s"
                        dbCursor.execute(userQuery, (newLabel, editIndex))
                        dbConnection.commit()
                        print("The record's new manufacturing label was set.")
                        return

                    #If the desired property to change is the release year
                    elif (property == "Year"):
                        print("Please enter the record's release year, or 0 if you don't know the year.")
                    
                        try:
                            #Make sure the user enters an integer
                            newYear = int(input())
                            print("")

                            #Set the record's manufacturing label to the new one
                            userQuery = "UPDATE Record SET release_Year = %s WHERE record_id = %s"
                            dbCursor.execute(userQuery, (newYear, editIndex))
                            dbConnection.commit()
                            print("The record's new release year was set.")
                            return

                        #If the user didn't enter a valid release year, display an error message
                        except ValueError:
                            print("Invalid release year. The record could not be created.")
                            return

                    #Any other properties are invalid
                    else:
                        print("Invalid property to modify. Please try again.")
                        return

            #If the user's index choice wasn't a valid selection
            print("Invalid index selection. Please try again.")

        #If the user didn't enter an integer for the index
        except ValueError:
            print("Index entered must be an integer. Please try again.")



"""
    Name: loadCSVRecordList
    Description: This function loads a record list from a file and populates a database's Record table 
                 with the results of the file

    Parameter: dbConnection         The connection the the database
    Parameter: dbCursor             The cursor object to execute commands on the database

    No return value
"""
def loadCSVRecordList(dbConnection, dbCursor):

    print("Please enter the name of the file to load the list of records from.")

    #Get the file to read records in from
    readFile = input("> ")
    print("")

    readFileArray = readFile.split(".")

    #Check if the filename is valid
    if (len(readFileArray) != 2):
        print("Invalid file. Please try again.")
        return

    #Check if the file is a csv file
    if (readFileArray[1] != "csv"):
        print("Invalid file. Please try again.")
        return

    #Drop the RECORD table in the database if it exists, and create a new table to replace it
    dbCursor.execute("DROP TABLE IF EXISTS RECORD")
    dbCursor.execute('''CREATE TABLE RECORD (record_id INT AUTO_INCREMENT, artist_Name VARCHAR(100) NOT NULL, record_Name VARCHAR(100) NOT NULL, 
                    record_Label VARCHAR(100), release_Year VARCHAR(5), quantity INT NOT NULL, additional_Info VARCHAR(100), PRIMARY KEY(record_id))
                    ''')

    #Commit the changes
    dbConnection.commit()

    #Attempt to open the file and read all of its rows into the database table
    try:
        with open(readFile, "r") as fp:
            recordReader = csv.reader(fp)

            #Skip the header row
            next(recordReader)

            #Grab each row from the file, and create a row in the 'Record' table
            for row in recordReader:
                userQuery = "INSERT INTO Record (artist_Name, record_Name, record_Label, release_Year, quantity, additional_Info) VALUES (%s, %s, %s, %s, %s, %s)"
                dbCursor.execute(userQuery, (row[0], row[1], row[2], row[3], int(row[4]), row[5]))
                dbConnection.commit()

            print("The database table has successfully been populated from the file " + readFile + ".")
                
    #If the file couldn't be found, display an error message
    except FileNotFoundError:
        print("The file " + readFile + " could not be found. Please try again.")

    #If the file had an invalid data value
    except ValueError:
        print("The file had invalid data and could not be used. Please try again.")

    #If any issues occur populating the database table
    except:
        print("There was an issue populating the database table from the csv file. Please try again.")



"""
    Name: removeRecord
    Description: This function will prompt the user to remove a record from the list.

    Parameter: dbConnection         The connection the the database
    Parameter: dbCursor             The cursor object to execute commands on the database
    No return value 
"""
def removeRecord(dbConnection, dbCursor):

    #Prompt for the artist name
    removeArtist = input("Enter the artist name of the record to remove.\n")
    print("")

    #Get all of the records in the table for the current artist
    userQuery = "SELECT record_id, record_Name FROM Record WHERE artist_Name = %s"
    dbCursor.execute(userQuery, (removeArtist,))

    #The records retrieved from the database table
    currentRecords = dbCursor.fetchall()

    #If there were no records for the artist, return
    if (len(currentRecords) == 0):
        print("There are no records in the list by " + removeArtist)
        return

    #Otherwise, list them and prompt for the record selection
    else:
        print("The records by this artist currently in the list are listed below.")
        print("Please enter the index of the album title below to remove it.")

        #Print all of the records
        for i in currentRecords:
            print(i)

        try:

            #This holds the user's index selection
            removeIndex = int(input())
            print("")

            #Loop through all of the rows for the artist
            for j in currentRecords:

                #Check if the user entered a valid index of a row
                if removeIndex in j:

                    userQuery = "DELETE FROM Record WHERE record_ID = %s"
                    dbCursor.execute(userQuery, (removeIndex,))
                    dbConnection.commit()

                    print("The record has been successfully removed from the list.")
                    return

            #If the user's index choice wasn't a valid selection
            print("Invalid index selection. Please try again.")
            
        #If the user's index choice wasn't an integer
        except ValueError:
            print("Index entered must be an integer. Please try again.")

            

"""
    Name: saveRecordListCSV
    Description: This function saves a record list from the database to a csv file.

    Parameter: dbConnection         The connection the the database
    Parameter: dbCursor             The cursor object to execute commands on the database

    No return value
"""
def saveRecordListCSV(dbConnection, dbCursor):

    #Prompt for the file to write to
    recordFile = input("Please enter the name of the csv file to write to.\n")
    print("")

    fileNameArray = recordFile.split(".")

    #Verify the file name is valid
    if (len(fileNameArray) != 2):
        print("The filename to save to is invalid. Please try again.")
        return

    fileExtension = fileNameArray[1]

    #Verify the file type is a csv file
    if (fileExtension != "csv"):
        print("The filename to save to is invalid. Please try again.")
        return

    #Grab the full record list from the database's Records table
    dbCursor.execute("SELECT * FROM Record ORDER BY artist_Name, record_Name")
    recordList = dbCursor.fetchall()

    #Open the file and write the record list to it
    with open(recordFile, mode="w") as fp:
        recordWriter = csv.writer(fp, delimiter=',')
        recordWriter.writerow(["Artist", "Title", "Manufacturing Label", "Release Year", "Quantity", "Additional Information"])

        #Write all of the rows in the database table to the file
        for record in recordList:
            recordWriter.writerow([record[1], record[2], record[3], record[4], str(record[5]), record[6]])

        print("The record list has successfully been saved in " + recordFile + ".")
