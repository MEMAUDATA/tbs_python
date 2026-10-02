''' Toulouse Business School MSc AIBA

Course: Python for Data Science
Author: Dr. Samia Drappeau
Version: v1.0
'''

"""
EXERCICE 1
---
- Finish the code that creates the `client_savings` list. Build the list so that the list first contains the name of each saving as a string and then its value. In other words, add the strings "cash", "investment" and "realstate" at the appropriate locations.
- Print areas again; is the printout more informative this time?
"""

# Saving variables
cash = 100
saving = 200
investment = 500
real_estate = 1000
bitcoin = 100000

# Adapt list of savings
client_savings = [cash, "saving", saving, investment, real_estate, bitcoin]

# Print `client_savings``


"""
EXERCICE 2
---
# [20230911-SDR] FIX INSTRUCTIONS
- Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
- Print out `portfolio`; does this way of structuring your data make more sense?
- Print out the type of `portfolio`. Are you still dealing with a list?
"""
# savings information as list of lists
portfolio = [
                ["cash", cash],
                ["saving", saving]
            ]

# Print out portfolio

# Print out the type of portfolio
