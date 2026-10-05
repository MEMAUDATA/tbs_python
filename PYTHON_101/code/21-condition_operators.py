''' Toulouse Business School MSc AIBA

Course: Python for Data Science
Author: Dr. Samia Drappeau
Version: v1.0
'''

"""
EXERCICE 1
---
- Examine the if statement that prints out "looking around in the kitchen." if room equals "kit".
- Write another if statement that prints out "big place!" if area is greater than 15.
"""
# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area



"""
EXERCICE 2
---
- Add an else statement to the second control structure so that "pretty small." is printed out if area > 15 evaluates to False.
"""
# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")



"""
EXERCICE 3
---
- Add an elif to the second control structure such that "medium size, nice!" is printed out if area is greater than 10.
"""
# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
else :
    print("pretty small.")