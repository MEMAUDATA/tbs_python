''' Toulouse Business School MSc AIBA

Course: Python for Data Science
Author: Dr. Samia Drappeau
Version: v1.0


Description
---
You've got your first taste of writing your own functions in the previous exercises. You've learned how to add parameters to your own function definitions, return a value or multiple values with tuples, and how to call the functions you've defined.

In this and the following exercise, you will bring together all these concepts and apply them to a simple data science problem. You will load a dataset and develop functionalities to extract simple insights from the data.

For the first exercise, your goal is to recall how to load a dataset into a DataFrame. The dataset contains Twitter data and you will iterate over entries in a column to build a dictionary in which the keys are the names of languages and the values are the number of tweets in the given language. The file tweets.csv is available in your current directory.

In the second exercise, you will define a function with the functionality you developed in the previous exercise, return the resulting dictionary from within the function, and call the function with the appropriate arguments.

Be aware that this is real data from Twitter and as such there is always a risk that it may contain profanity or other offensive content (in this exercise, and any following exercises that also use real Twitter data).
'''

"""
EXERCICE 1
---
- Import the pandas package with the alias pd.
- Import the file 'tweets.csv' using the pandas function read_csv(). Assign the resulting DataFrame to df.
- Complete the for loop by iterating over col, the 'lang' column in the DataFrame df.
- Complete the bodies of the if-else statements in the for loop: if the key is in the dictionary langs_count, add 1 to the value corresponding to this key in the dictionary, else add the key to langs_count and set the corresponding value to 1. Use the loop variable entry in your code.
"""
# Import pandas
import pandas as pd

# Import Twitter data as dataframe: df
tweets_df = ____

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = tweets_df['lang']

# Iterate over lang column in DataFrame
for entry in ____:

    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        ____
    # Else add the language to langs_count, set the value to 1
    else:
        ____

# Print the populated dictionary
print(langs_count)


"""
EXERCICE 2
---
- Define the function count_entries(), which has two parameters. The first parameter is df for the DataFrame and the second is col_name for the column name.
- Complete the bodies of the if-else statements in the for loop: if the key is in the dictionary langs_count, add 1 to its current value, else add the key to langs_count and set its value to 1. Use the loop variable entry in your code.
- Return the langs_count dictionary from inside the count_entries() function.
- Call the count_entries() function by passing to it tweets_df and the name of the column, 'lang'. Assign the result of the call to the variable result.
- Plot the variable result on a Barplot
"""
# Define count_entries()
def ____(____, ____):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = tweets_df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            ____
        # Else add the language to langs_count, set the value to 1
        else:
            ____

    # Return the langs_count dictionary
    

# Call count_entries(): result


# Print the result
print(result)


# Show the result in a bar plot
import matplotlib.pyplot as plt
plt.bar(____, ____, color='g')
plt.show()
plt.clf()