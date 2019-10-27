import csv

class Record():

    def __init__(self, artist, title, label, releaseYear, quantity = 1, additionalInfo = ""):
        self.artist = artist
        self.title = title
        self.label = label
        self.releaseYear = releaseYear
        self.quantity = quantity
        self.additionalInfo = additionalInfo

    def decrementQuantity(self):
        self.quantity = self.quantity - 1

    def incrementQuantity(self):
        self.quantity = self.quantity + 1

    def setAdditionalInfo(self, additionalInfo):
        self.additionalInfo = additionalInfo

    def setRecordLabel(self, label):
        self.label = label

    def setReleaseYear(self, releaseYear):

        #If the passed release year is 0, set it to be blank (default)
        if (releaseYear == "0"):
            self.releaseYear = ""

        #Otherwise, set it to the passed release year
        else:
            self.releaseYear = releaseYear



"""
    Name: createRecord
    Description: This function is used to create a new record to add to the list of records

    Parameter: records         The list of records being modified
    No return value
"""
def createRecord(records):

        #Prompt for the record artist
        newArtist = input("Please enter the record artist.\n")
        print("")

        #Get all of the records in the list for the current artist
        currentRecords = getRecordsByArtist(records, newArtist)        

        #IF EXISTING ARTIST: If this is an existing artist, display the list of records in the system
        if (len(currentRecords) > 0):
            print("The records by this artist currently in the list are listed below.")
            print("Please enter the index of the album title below if this is an existing record.")

            #Print the list of records by the specified artist, and the index of each in the list
            for index, title in currentRecords.items():
                print(str(index) + " : " + title)

            try:
                #This holds the user's index selection
                addIndex = int(input())
                print("")

                #If the user entered an index of an existing record, add it to the list
                if (addIndex in currentRecords.keys()):
                    records[addIndex].incrementQuantity()
                    print("The record's quantity was successfully updated.")

                #Otherwise, if this is a new record, prompt to create a new entry
                else:

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

                        #Create the new record and add it to the list of records
                        newRecord = Record(newArtist, newTitle, newLabel, newYear)
                        records.append(newRecord)

                        print("The new record " + newTitle + " by " + newArtist + " was added to the list of records.")

                    #If the user didn't enter a valid release year, display an error message
                    except ValueError:
                        print("Invalid release year. The record could not be created.")

            #If the user didn't enter an integer for the record's index
            except ValueError:
                print("The index entered was invalid.")

        #ELSE NEW ARTIST: If this is a new artist entirely, prompt for the name of the record
        else:
            print("There are no records in the list by this artist.")
            print("")
            
            #Prompt for the name of the album
            newTitle = input("Please enter the name of the new album.\n")
            print("")

            #Prompt for the album's manufacturing label
            newLabel = input("Please enter the label that published the record, or 'unknown'.\n")
            print("")
            
            #Prompt for the album's release year
            try:

                #Make sure the user enters an integer
                newYear = int(input("Please enter the album's release year or 0 if you don't know the year.\n"))
                print("")

                #Create the new record and add it to the list of records
                newRecord = Record(newArtist, newTitle, newLabel, newYear)
                records.append(newRecord)

                print("The new record " + newTitle + " by " + newArtist + " was added to the list of records.")

            #If the user didn't enter a valid release year, display an error message
            except ValueError:
                print("Invalid release year. The record could not be created.")



"""
    Name: editRecord
    Description: This function prompts the user for a new value to set for the desired property.

    Parameter: records          The list of records
    Parameter: property         The desired property to modify
    No return value
"""
def editRecord(records, property):

    #Prompt for the name of the artist
    editArtist = input("Please enter the name of the artist.\n")
    print("")

    #Retrieve the list of records for the given artist
    currentRecords = getRecordsByArtist(records, editArtist)

    #If there were no records for the artist, return
    if (len(currentRecords) == 0):
        print("There are no records in the list by " + editArtist)
        return

    #Otherwise, list them and prompt for the record selection
    else:
        print("The records by this artist currently in the list are listed below.")
        print("Please enter the index of the album title below to modify it.")

        #Print the list of records by the specified artist, and the index of each in the list
        for index, title in currentRecords.items():
            print(str(index) + " : " + title)

        try:
            #Get the user's index and verify it's an integer
            addIndex = int(input())
            print("")

            #If the user entered a valid index of an existing record, prompt to modify the desired property
            if (addIndex in currentRecords.keys()):

                #If the desired property to change is the manufacturing label
                if (property == "Label"):
                    newLabel = input("Please enter the record's manufacturing label.\n")
                    print("")

                    #Set the record's manufacturing label to the new one
                    records[addIndex].setRecordLabel(newLabel)

                    print("The record's new manufacturing label was set.")

                #If the desired property to change is the release year
                elif (property == "Year"):
                    print("Please enter the record's release year, or 0 if you don't know the year.")
                    print("")
                    
                    try:
                        #Make sure the user enters an integer
                        newYear = int(input())
                        print("")

                        #Set the record's release year to the new one
                        records[addIndex].setReleaseYear(newYear)

                        print("The record's new release year was set.")

                    #If the user didn't enter a valid release year, display an error message
                    except ValueError:
                        print("Invalid release year. The record could not be created.")

                #If the desired property to change is the additional information
                elif (property == "Additional"):
                    newAdditionalInfo = input("Please enter the record's additional information.\n")
                    print("")

                    #Set the record's additional information
                    records[addIndex].setAdditionalInfo(newAdditionalInfo)

                    print("The record's additional information was set.")

                #Any other properties are invalid
                else:
                    print("Invalid property to modify. Please try again.")

            #If the user's index choice wasn't a valid selection
            else:
                print("Invalid index selection. Please try again.")

        #If the user didn't enter an integer for the index
        except ValueError:
            print("Index entered must be an integer. Please try again.")



"""
    Name: getRecordsByArtist
    Description: Thie function retrieves the list of records for the specified artist

    Parameter: records          The list of records
    Parameter: artist           The artist to retrieve the records for
    Return: currentRecords      The list of records for the given artist
"""
def getRecordsByArtist(records, artist):

    #Dictionary of the records for the given artist, accessed by their index in the list of records
    currentRecords = {}

    #Loop iterator
    i = 1

    #Loop through the list of records
    for i in range(len(records)):

        #If the record's artist matches the artist we're looking for, add the record to the dictionary
        if records[i].artist == artist:
            currentRecords[i] = records[i].title

    #Return the list of records
    return currentRecords



"""
    Name: loadRecordList
    Description: This function reads in a list of records from the specified file.

    Parameter: records          The list of records
    No return value
"""
def loadRecordList(records):
    print("Please enter the name of the file to load the list of records from.")

    #Get the file to read records in from
    readFile = input()
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

    #Clear the record list if it has data from a previous load
    records.clear()

    #Attempt to open the file and read all of its rows into the list
    try:
        with open(readFile, "r") as fp:
            recordReader = csv.reader(fp)

            #Skip the header row
            next(recordReader)

            #Grab each row
            for row in recordReader:
                newRecord = Record(row[0], row[1], row[2], row[3], int(row[4]), row[5])
                records.append(newRecord)

    #If the file couldn't be found, display an error message
    except FileNotFoundError:
        print("The file " + readFile + " could not be found. Please try again.")

    except TypeError:
        print("The file had invalid data and could not be used. Please try again.")



"""
    Name: removeRecord
    Description: This function removes a record from the given list of records, if it exists in the list.

    Parameter: records          The list of records
    No return value
"""
def removeRecord(records):
    
    #Prompt for the artist name
    removeArtist = input("Enter the artist name of the record to remove.\n")
    print("")

    #Dictionary of the records for the given artist, accessed by their index in the list of records
    removeRecords = getRecordsByArtist(records, removeArtist)

    #If the artist didn't have any records, there are none to remove
    if len(removeRecords) == 0:
        print("There are no records by the artist " + removeArtist + ".")

    #Otherwise, prompt the user for which one to remove
    else:
        print("Enter the index of the record to remove or an invalid number to cancel.")
                
        #Print out every record for the given artist, and its index
        for index, title in removeRecords.items():
            print(str(index) + " : " + title)

        try:
            #Get the user's index and verify it's an integer
            removeIndex = int(input())
            print("")

            #If the user entered a valid index to remove, check its quantity
            if (removeIndex in removeRecords.keys()):

                #If the record has multiple copies, decrement its count
                if (records[removeIndex].quantity > 1):
                    records[removeIndex].decrementQuantity()
                    print("The record's quantity was lowered by one.")

                #Else, remove the record entirely
                else:
                    records.pop(removeIndex)
                    print("The record was removed from the list of records.")

            #If the user entered an invalid index, display an error message
            else:
                print("Invalid selection. Please try again.")
        
        except ValueError:
            print("Index entered must be an integer. Please try again.")
        


"""
    Name: saveRecordList
    Description: This function writes the passed list of records to a user-specified csv file.

    Parameter: records          The list of records
    No return value
"""
def saveRecordList(records):
    
    #If the record list passed is empty, return
    if (len(records) == 0):
        print("The passed record list is empty.")
        return

    #Prompt for the file to write to
    recordFile = input("Please enter the name of the csv file to write to.\n")
    print("")

    #Verify the file name is valid
    fileNameArray = recordFile.split(".")

    if (len(fileNameArray) != 2):
        print("The filename to save to is invalid. Please try again.")
        return

    #Verify the file type is a csv file
    fileExtension = fileNameArray[1]

    if (fileExtension != "csv"):
        print("The filename to save to is invalid. Please try again.")
        return

    #Sort the file list before writing
    sortRecordList(records)

    #Open the file and write the record list to it
    with open(recordFile, mode="w") as fp:
        recordWriter = csv.writer(fp, delimiter=',')
        recordWriter.writerow(["Artist", "Title", "Manufacturing Label", "Release Year", "Quantity", "Additional Information"])

        #Write each record as a new row
        for rec in records:
            recordWriter.writerow([rec.artist, rec.title, rec.label, rec.releaseYear, rec.quantity, rec.additionalInfo])

    print("The record list has successfully been saved in " + recordFile + ".")



"""
    Name: sortRecordList
    Description: This function sorts the passed list of records if it isn't empty.

    Parameter: records          The list of records to sort
    No return value
"""
def sortRecordList(records):

    #If the record list is empty, it can't be sorted
    if (len(records) == 0):
        print("The record list to sort is empty.")
        return

    #Sort the list based on artist first, and album title second
    records.sort(key=lambda rec: (rec.artist, rec.title))