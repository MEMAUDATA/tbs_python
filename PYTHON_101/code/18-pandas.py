''' Toulouse Business School MSc AIBA

Course: Python for Data Science
Author: Dr. Samia Drappeau
Version: v1.0
'''

"""
EXERCICE 1
---
- Import pandas as pd.
- Use the pre-defined lists to create a dictionary called my_dict. There should be three key value pairs:
    - key 'country' and value names.
    - key 'drives_right' and value dr.
    - key 'cars_per_cap' and value cpc.
- Use pd.DataFrame() to turn your dict into a DataFrame called cars.
- Print out cars and see how beautiful it is.
"""
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd


# Create dictionary my_dict with three key:value pairs: my_dict


# Build a DataFrame cars from my_dict: cars


# Print cars


"""
EXERCICE 2
---
- Run the code to see that, indeed, the row labels are not correctly set.
- Specify the row labels by setting cars.index equal to row_labels.
- Print out cars again and check if the row labels are correct this time.
"""
# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame.from_dict(dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars


# Print cars again


"""
EXERCICE 3
---
- To import CSV files you still need the pandas package: import it as pd.
- Use pd.read_csv() to import cars.csv data as a DataFrame. Store this DataFrame as cars.
- Print out cars. Does everything look OK?
"""
# Import the cars.csv data: cars



# Print out cars

"""
EXERCICE 4
---
- Run the code with Run Code and assert that the first column should actually be used as row labels.
- Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
- Has the printout of cars improved now?
"""
# Fix import by including index_col
cars = pd.read_csv('/Users/samiadrappeau/Documents/TBS/PYTHON-101/code/02-intermediate/cars.csv') # ADAPT THE PATH TO YOURS

# Print out cars
print(cars)

"""
EXERCICE 5
---
- Use single square brackets to print out the country column of cars as a Pandas Series.
- Use double square brackets to print out the country column of cars as a Pandas DataFrame.
- Use double square brackets to print out a DataFrame with both the country and drives_right columns of cars, in this order.
"""
# Print out country column as Pandas Series


# Print out country column as Pandas DataFrame


# Print out DataFrame with country and drives_right columns

"""
EXERCICE 6
---
- Select the first 3 observations from cars and print them out.
- Select the fourth, fifth and sixth observation, corresponding to row indexes 3, 4 and 5, and print them out.
"""
# Print out first 3 observations


# Print out fourth, fifth and sixth observation

"""
EXERCICE 7
---
- Use loc or iloc to select the observation corresponding to Japan as a Series. The label of this row is JPN, the index is 2. Make sure to print the resulting Series.
- Use loc or iloc to select the observations for Australia and Egypt as a DataFrame. You can find out about the labels/indexes of these rows by inspecting cars in the IPython Shell. Make sure to print the resulting DataFrame.
"""
# Print out observation for Japan


# Print out observations for Australia and Egypt


"""
EXERCICE 8
---
- Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
- Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right.
"""
# Print out drives_right value of Morocco


# Print sub-DataFrame


"""
EXERCICE 9
---
- Print out the drives_right column as a Series using loc or iloc.
- Print out the drives_right column as a DataFrame using loc or iloc.
- Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc.
"""
# Print out drives_right column as Series


# Print out drives_right column as DataFrame


# Print out cars_per_cap and drives_right as DataFrame

