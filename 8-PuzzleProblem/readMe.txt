Author: Reed Spratt
Last Date Modified: April 21st 2020

___________________________________________________
DESCRIPTION
___________________________________________________

This program performs A* search using Manhattan heuristics to solve the 8-Puzzle Problem.

The 8-Puzzle Problem is defined in an input file with an initial state to start at and a goal state to reach.
Instructions for the file formatting can be found in RUNNING INSTRUCTIONS.

After searching, the search tree that was formed is displayed along with the solution as the list of nodes from the root to the goal state.

Note: This program is a recreation of an assignment I originally completed in school in Java. 
The original program coded included provided code from the instructor, Dr. Yang Xiang, but this program was entirely coded by me.

___________________________________________________
DEPENDENCIES
___________________________________________________

This program was coded to be compatible with Python 3. 
It has not been tested with previous versions of Python, but should be compatible with them.

No external libraries are required.

___________________________________________________
RUNNING INSTRUCTIONS
___________________________________________________

This program can be run with the command python searchAgent.py.

An input file is required with the initial and goal states of the 8-Puzzle Problem to use.
The required format of the file is specified below:

Lines 1-3 are the three lines making up the initial puzzle configuration.
Lines 6-8 are the three lines making up the goal puzzle configuration. 

Note: The initGoal.txt file included in this repository provides an example of a valid input file.

___________________________________________________
LIMITATIONS
___________________________________________________

This program is not equipped to detect and handle puzzles that are impossible to solve.
Using one such puzzle will cause the program to loop infinitely.