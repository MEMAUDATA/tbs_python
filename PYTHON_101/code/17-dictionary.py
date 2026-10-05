''' Toulouse Business School MSc AIBA

Course: Python for Data Science
Author: Dr. Samia Drappeau
Version: v1.0
'''

"""
EXERCICE 1
---
- Use the index() method on countries to find the index of 'germany'. Store this index as ind_ger.
- Use ind_ger to access the capital of Germany from the capitals list. Print it out.
"""
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')


# Use ind_ger to print out capital of Germany


"""
EXERCICE 2
---
- With the strings in countries and capitals, create a dictionary called europe with 4 key:value pairs. Beware of capitalization! Make sure you use lowercase characters everywhere.
- Print out europe to see if the result is what you expected.
"""
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', ___, ___, ___ }

# Print europe


"""
EXERCICE 3
---
- Check out which keys are in europe by calling the keys() method on europe. Print out the result.
- Print out the value that belongs to the key 'norway'.
"""
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe


# Print out value that belongs to key 'norway'


"""
EXERCICE 4
---
- Add the key 'italy' with the value 'rome' to europe.
- To assert that 'italy' is now a key in europe, print out 'italy' in europe.
- Add another key:value pair to europe: 'poland' is the key, 'warsaw' is the corresponding value.
- Print out europe.
"""
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe


# Print out italy in europe


# Add poland to europe


# Print europe


"""
EXERCICE 5
---
- The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.
- Australia is not in Europe, Austria is! Remove the key 'australia' from europe.
- Print out europe to see if your cleaning work paid off.
"""
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 
          'australia':'vienna' }

# Update capital of germany


# Remove australia


# Print europe


"""
EXERCICE 6
---
- Use chained square brackets to select and print out the capital of France.
- Create a dictionary, named data, with the keys 'capital' and 'population'. Set them to 'rome' and 59.83, respectively.
- Add a new key-value pair to europe; the key is 'italy' and the value is data, the dictionary you just built.
"""
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
           
           
# Print out the capital of France


# Create sub-dictionary data


# Add data to europe under key 'italy'


# Print europe

