''' Toulouse Business School MSc AIBA

Course: Python for Data Science
Author: Dr. Samia Drappeau
Version: v1.0
'''

"""
EXERCICE 1
---
- Extract the drives_right column as a Pandas Series and store it as dr.
- Use dr, a boolean Series, to subset the cars DataFrame. Store the resulting selection in sel.
- Print sel, and assert that drives_right is True for all observations.
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('./cars.csv', index_col = 0) # ADAPT THE PATH TO YOURS

# Extract drives_right column as Series: dr


# Use dr to subset cars: sel


# Print sel


"""
EXERCICE 2
---
- Convert the code to a one-liner that calculates the variable sel as before.
"""
# Convert code to a one-liner
dr = cars['drives_right']
sel = cars[dr]

# Print sel
print(sel)


"""
EXERCICE 3
---
- Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.
- Use cpc in combination with a comparison operator and 500. You want to end up with a boolean Series that's True if the corresponding country has a cars_per_cap of more than 500 and False otherwise. Store this boolean Series as many_cars.
- Use many_cars to subset cars, similar to what you did before. Store the result as car_maniac.
- Print out car_maniac to see if you got it right.
"""
# Select the cars_per_cap column


# Create car_maniac: observations that have a cars_per_cap over 500



# Print car_maniac


"""
EXERCICE 4
---
- Use the code sample provided to create a DataFrame medium, that includes all the observations of cars that have a cars_per_cap between 100 and 500.
Print out medium.
"""
# Import numpy, you'll need this


# Create medium: observations with cars_per_cap between 100 and 500


# Print medium

