''' Toulouse Business School MSc AIBA

Course: Python for Data Science
Author: Dr. Samia Drappeau
Version: v1.0
'''

"""
EXERCICE 1
---
- Write a for loop that iterates over all elements of the areas list and prints out every element separately.
"""
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop


"""
EXERCICE 2
---
- Adapt the for loop in the sample code to use enumerate() and use two iterator variables.
- Update the print() statement so that on each run, a line of the form "room x: y" should be printed, where x is the index of the list element and y is the actual list element, i.e. the area. Make sure to print out this exact string, with the correct spacing.
"""
# Change for loop to use enumerate()
for a in areas :
    print(a)


"""
EXERCICE 3
---
- Adapt the print() function in the for loop so that the first printout becomes "room 1: 11.25", the second one "room 2: 18.0" and so on.
"""
# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index) + ": " + str(area))

"""
EXERCICE 4
---
- Write a for loop that goes through each sublist of house and prints out the x is y sqm, where x is the name of the room and y is the area of the room.
"""
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch

