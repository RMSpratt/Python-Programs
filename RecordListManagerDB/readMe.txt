Author: Reed Spratt
Last Date Modified: March 2nd 2020

___________________________________________________
DESCRIPTION
___________________________________________________

This is a simple program for editing and querying an SQL database table containing information about various records.

I originally developed this program in the summer of 2019 to create an inventory of my Dad's record collection, but gradually
added functionality for querying the collection as well. 

The list of records attached with this program is only a subset of the records in my Dad's collection.


___________________________________________________
DEPENDENCIES
___________________________________________________

You must have MySQL installed on your device to use this program, and the mysql connector library for Python. 
The csv and getpass libraries are also used in this project.


___________________________________________________
RUNNING INSTRUCTIONS
___________________________________________________

This program can be run with the command 'python recordMenuDB.py' and will immediately prompt for information to connect to an SQL database.
Note: A version of this program exists that doesn't require a database in the folder 'RecordListManager'.

After establishing a connection, you have the options to either: 

1) Create a new empty Records Table to be populated as you'd like.
2) Create a new Records Table populated with a csv file.
3) Use an existing Records Table for manipulation. 

After successfully choosing and setting up a table using one of these options, you can use the edit or query menu commands to manipulate the Records table.
