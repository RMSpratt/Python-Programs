import csv

class Record():

    def __init__(self, artist = "undefined", title = "undefined", quantity = 1):
        self.artist = artist
        self.title = title
        self.quantity = quantity

    def decrementQuantity(self):
        self.quantity = self.quantity - 1

    def incrementQuantity(self):
        self.quantity = self.quantity + 1



"""
    Name: createRecord
    Description: This function is used to create a new record to add to the list of records

    Parameter: records         The list of records being modified
    No return value
"""
def createRecord(records):

        #The name of the artist and title of the new record to create
        newArtist = ""
        newTitle = ""

        #Prompt for the record artist
        print("Enter the record artist.")
        newArtist = input()

        #Dictionary of the records for the given artist, accessed by their index in the list of records
        currentRecords = {}

        #Loop iterator
        i = 1

        #Loop through the list of records
        for i in range(len(records)):

            #If the record's artist matches the artist we're looking for, add the record to the dictionary
            if records[i].artist == newArtist:
                currentRecords[i] = records[i].title

        #IF EXISTING ARTIST: If this is an existing artist, display the list of records in the system
        if (len(currentRecords) > 0):
            print("The records by this artist currently in the list are listed below.")
            print("Please enter the index of the album title below if this is an existing record.")

            #Print the list of records by the specified artist, and the index of each in the list
            for index, title in currentRecords.items():
                print(str(index) + " : " + title)

            #This holds the user's index selection
            indexChoice = input()

            #Make sure the user entered a number
            try:

                #This holds the index of the record to add if its an existing record
                addIndex = int(indexChoice)

                #If the user entered a valid index of an existing record, add it to the list
                if (addIndex in currentRecords.keys()):
                    records[addIndex].incrementQuantity()
                    print("The record's quantity was successfully updated.")

                #If the user entered an invalid index, prompt to create a new record
                else:
                    print("Please enter the name of the new album.")
                    newTitle = input()

                    #Create the new record and add it to the list of records
                    newRecord = Record(newArtist, newTitle)
                    records.append(newRecord)

            #If the user didn't enter a number, display an error message
            except ValueError:
                print("Invalid selection. Please try again.")

        #ELSE NEW ARTIST: If this is a new artist entirely, prompt for the name of the record
        else:
            print("There are no records in the list by this artist.")
            print("Please enter the name of the new album.")
            newTitle = input()

            #Create the new record and add it to the list of records
            newRecord = Record(newArtist, newTitle)
            records.append(newRecord)

            print("The new record " + newTitle + " by " + newArtist + " was added to the list of records.")



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

    readFileArray = readFile.split(".")

    #Check if the filename is valid
    if (len(readFileArray) != 2):
        print("Invalid file. Please try again.")
        return

    #Check if the file is a csv file
    if (readFileArray[1] != "csv"):
        print("Invalid file. Please try again.")
        return

    #Attempt to open the file and read all of its rows into the list
    try:
        with open(readFile, "r") as fp:
            recordReader = csv.reader(fp)

            #Skip the header row
            next(recordReader)

            #Grab each row
            for row in recordReader:
                newRecord = Record(row[0], row[1], int(row[2]))
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
    print("Enter the artist name of the record to remove.")
    removeArtist = input()

    #Dictionary of the records for the given artist, accessed by their index in the list of records
    removeRecords = {}

    #Loop iterator
    i = 1

    #Loop through the list of records
    for i in range(len(records)):

        #If the record's artist matches the artist we're looking for, add the record to the dictionary
        if records[i].artist == removeArtist:
            removeRecords[i] = records[i].title

    #If the artist didn't have any records, there are none to remove
    if len(removeRecords) == 0:
        print("There are no records by the artist " + removeArtist + ".")

    #Otherwise, prompt the user for which one to remove
    else:
        print("Enter the index of the record to remove or an invalid number to cancel.")
                
        #Print out every record for the given artist, and its index
        for index, title in removeRecords.items():
            print(str(index) + " : " + title)

        #Get the user's selection
        removeChoice = input()

        #Make sure the user entered a number
        try:
            removeIndex = int(removeChoice)

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

        #If the user didn't enter a number, display an error message
        except ValueError:
            print("Invalid selection. Please try again.")
        


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
    print("Please enter the name of the csv file to write to.")
    recordFile = input()

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
        recordWriter.writerow(["Artist", "Title", "Quantity"])

        #Write each record as a new row
        for rec in records:
            recordWriter.writerow([rec.artist, rec.title, rec.quantity])

    print("The record list has successfully been saved in  " + recordFile + ".")



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

