''' Toulouse Business School MSc AIBA

Course: Python for Data Science
Author: Dr. Samia Drappeau
Version: v1.0
'''

"""
EXERCICE 1
---
- Use print() in combination with type() to print out the type of var1.
- Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
- Use int() to convert var2 to an integer. Store the output as out2.
"""
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1

# Print out length of var1

# Convert var2 to an integer: out2

"""
EXERCICE 2
---
- Use `help()` to understand the arguments taken by the function `sorted()`.
- Use + to merge the contents of first and second into a new list: full.
- Call sorted() on full and specify the reverse argument to be True. Save the sorted list as full_sorted.
- Finish off by printing out full_sorted.
"""
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Print the documentation of the function `sorted()`
help(sorted)

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=False)

# Print out full_sorted
print(full_sorted)
