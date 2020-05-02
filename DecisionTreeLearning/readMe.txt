Author: Reed Spratt
Last Date Modified: May 2nd 2020

___________________________________________________
DESCRIPTION
___________________________________________________

This program forms a decision tree for making decisions on new examples with a set of criteria. An initial static training set of examples are used 
to form the decision tree, and generalize decisions for future examples. A set of attributes are used to build the decision tree and classify the input examples.

For more detailed explanations of each major data structure/class and individual functions, see them in the source files.

This program makes use of two input files:
scheme.txt: This file contains all of the attributes to be used for decision tree formation including their names, number of values, and possible values.
sample.txt: This file contains all of the examples to be classified using the decision tree built from the attributes in the scheme file.

This program is a rewritten version of the original completed in Java for a course at the University of Guelph. 
Credits to Dr. Xiang for distributing the assignment initially, but all of the code present in this program was written by me. 

An additional file giving a brief explanation of how Decision Tree formation in this manner works will be included in this repository at a later date.

___________________________________________________
DEPENDENCIES
___________________________________________________

Python 3+ was used to code this program, but no external libraries were used.

___________________________________________________
RUNNING INSTRUCTIONS
___________________________________________________

This program can be run with the command 'python DTLearn.py'. The two required files will then be prompted for. 
Instructions on required file formatting are below:

scheme.txt:

- The first line of this file must be a single integer value denoting how many attributes will be used for building the decision tree, 
  plus one for the function value attribute as a result of classification

- Each attribute must be separated by a single blank line and be detailed in three lines:
    Attribute name
    Attribute number of possible values (single integer value)
    Attribute possible values (strings separated by a space between)

- The function value attribute must be the last one present in the file

sample.txt: 

- The first line of this file must be the attribute names specified in the scheme file IN-ORDER

- Each example appears after this line on a separate line with all of its attribute value assignments for the example (including the function value)

- An error will be reported for improper order of attributes on the first line, or an invalid number of values for an example


Note: For an example of a properly formatted scheme file and sample file, see those included in this repository

___________________________________________________
LIMITATIONS
___________________________________________________

- File formatting as specified as above is strict and must be followed
- Rounding for information remaining and gained are rounded to four decimal places
