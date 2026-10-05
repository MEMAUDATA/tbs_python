''' Toulouse Business School MSc AIBA

Course: Python for Data Science
Author: Dr. Samia Drappeau
Version: v1.0
'''

"""
EXERCICE 1
---
- Write a for loop that iterates over the rows of cars and on each iteration perform two print() calls: one to print out the row label and one to print out all of the rows contents.
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('./cars.csv', index_col = 0) # ADAPT THE PATH TO YOURS

# Iterate over rows of cars


"""
EXERCICE 2
---
- Using the iterators lab and row, adapt the code in the for loop such that the first iteration prints out "US: 809", the second iteration "AUS: 731", and so on.
- The output should be in the form "country: cars_per_cap". Make sure to print out this exact string (with the correct spacing).
    - You can use str() to convert your integer data to a string so that you can print it in conjunction with the country label.
"""
# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab)
    print(row)

"""
EXERCICE 3
---
- Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. You can use the string method upper() for this.
- To see if your code worked, print out cars. Don't indent this code, so that it's not part of the for loop.
"""
# Code for loop that adds COUNTRY column



# Print cars



"""
EXERCICE 4
---
- Replace the for loop with a one-liner that uses .apply(str.upper). The call should give the same result: a column COUNTRY should be added to cars, containing an uppercase version of the country names.
- As usual, print out cars to see the fruits of your hard labor
"""
# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print cars
