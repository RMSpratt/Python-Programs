"""
    Name: executeArtistQuery
    Description: This function executes the passed query after getting the name of the artist to search with.

    Parameter: dbConnection         The connection the the database
    Parameter: dbCursor             The cursor object to execute commands on the database
    Parameter: query                The query to execute
    No return value
"""
def executeArtistQuery(dbConnection, dbCursor, query):

    #Prompt for the name of the artist
    queryArtist = input("Please enter the name of the artist.\n")
    print("")

    #Execute the passed query and get the resulting records
    dbCursor.execute(query, (queryArtist,))
    queryRecords = dbCursor.fetchall()

    #If there were no records in the list for the given artist, inform the user
    if (len(queryRecords) == 0):
        print("There were no records in the list for the artist " + queryArtist + ".")

    #Otherwise, print all of the records
    else:
        print("The records by the artist " + queryArtist + " are listed below.")

        for record in queryRecords:
            print("Title: " + record[0])
            print("Release Year: " + record[1])
            print("Quantity: " + str(record[2]))
            print("")



"""
    Name: executeLabelQuery
    Description: This function executes the passed query after getting the name of the record label to search with.

    Parameter: dbConnection         The connection the the database
    Parameter: dbCursor             The cursor object to execute commands on the database
    Parameter: query                The query to execute
    No return value
"""
def executeLabelQuery(dbConnection, dbCursor, query):

    #Prompt for the name of the record label
    queryLabel = input("Please enter the name of the record label.\n")
    print("")

    #Execute the passed query and get the resulting records
    dbCursor.execute(query, (queryLabel,))
    queryRecords = dbCursor.fetchall()

    #If there were no records in the list for the given manufacturing label, inform the user
    if (len(queryRecords) == 0):
        print("There were no records in the list released by " + queryLabel + ".")

    #Otherwise, print all of the records
    else:
        print("The records released by " + queryLabel + " are listed below.")

        for record in queryRecords:
            print("Artist: " + record[0])
            print("Title: " + record[1])
            print("Release Year: " + str(record[2]))
            print("")



"""
    Name: retrieveDuplicateRecords
    Description: This function gets all of the records with duplicate copies in the list with the passed query.

    Parameter: dbConnection         The connection the the database
    Parameter: dbCursor             The cursor object to execute commands on the database
    Parameter: query                The query to execute
    No return value
"""
def retrieveDuplicateRecords(dbConnection, dbCursor, query):
    
    dbCursor.execute(query)
    queryRecords = dbCursor.fetchall()

    #If there were no records in the list with duplicates, inform the user
    if (len(queryRecords) == 0):
        print("There were no records in the list with duplicate copies.")

    #Otherwise, print all of the records
    else:
        print("The records with duplicate copies are listed below.")

        for record in queryRecords:
            print("Artist: " + record[0])
            print("Title: " + record[1])
            print("Quantity: " + str(record[2]))
            print("")



"""
    Name: retrieveRecordsByYwar
    Description: This function gets all of the records released in a certain year with the passed query.

    Parameter: dbConnection         The connection the the database
    Parameter: dbCursor             The cursor object to execute commands on the database
    Parameter: query                The query to execute
    No return value
"""
def retrieveRecordsByYear(dbConnection, dbCursor, query):
    
    #Make sure the user enters an integer
    queryYear = input("Please enter the release year to search with.\n")
    print("")

    #Execute the passed query and get the resulting records
    dbCursor.execute(query, (queryYear,))
    queryRecords = dbCursor.fetchall()

    #If there were no records in the list for the given manufacturing label, inform the user
    if (len(queryRecords) == 0):
        print("There were no records in the list released in the year " + queryYear + ".")

    #Otherwise, print all of the records
    else:
        print("The records released in the year " + queryYear + " are listed below.")

    for record in queryRecords:
        print("Artist: " + record[0])
        print("Title: " + record[1])
        print("")
