''' Toulouse Business School MSc AIBA

Course: Python for Data Science
Author: Dr. Samia Drappeau
Version: v1.0
'''

"""
EXERCICE 1
---
- Create the variable offset with an initial value of 8.
- Code a while loop that keeps running as long as offset is not equal to 0. Inside the while loop:
- Print out the sentence "correcting...".
- Next, decrease the value of offset by 1. You can do this with offset = offset - 1.
- Finally, still within your loop, print out offset so you can see how it changes.
"""
# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
  print("correcting...")
  offset = offset -1
  print(offset)




"""
EXERICE 2
---
- Inside the while loop, complete the if-else statement:
    - If offset is greater than zero, you should decrease offset by 1.
    - Else, you should increase offset by 1.
- If you've coded things correctly, hitting Submit Answer should work this time.

If your code is still taking too long to run, you probably made a mistake. Check your code and make sure that the statement offset != 0 will eventually evaluate to FALSE!
"""
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if ____ :
      ____
    else : 
      ____    
    print(offset)