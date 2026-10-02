''' Toulouse Business School MSc AIBA

Course: Python for Data Science
Author: Dr. Samia Drappeau
Version: v1.0
'''

"""
EXERCICE 1
---
- Print out the second element from the areas list (it has the value 100).
- Subset and print out the last element of areas, being 1000. Using a negative index makes sense here!
- Select the number representing the amount of the client_savings (100) and print it out.
"""

#  List of savings
client_savings = ["cash", 100, "saving", 200, "investment", 500, "realstate", 1000, "bitcoin", 100000]

# Print out second element from areas
print(client_savings[1])

# Print out last element from areas
print(client_savings[-1])

# Print out the amount of the `investment`
print(client_savings[5])

"""
EXERCICE 2
---
- Using a combination of list subsetting and variable assignment, create a new variable, `cash_saving_amount`, that contains the sum of the amount of the `cash` and the amount of the `saving`.
- Print the new variable `cash_saving_amount`.
"""
# Sum of cash and savings amounts: cash_saving_amount
cash_saving_amount = client_savings[1] + client_savings[3]

# Print the variable cash_saving_amount
print(cash_saving_amount)

"""
EXERCICE 3
---
- Use slicing to create a list, `investment_saving`, that contains only the `investment` information.
- Do a somilar thing to create a new variable, `simple_savings`, that contains the first 4 elements of areas.
- Do a similar thing to create a new variable, `complex_savings`, that contains the last 6 elements of areas.
- Print, `investment_saving`, `simple_savings` and `complex_savings` using print().
"""
# Use slicing to create simple_savings
investment_saving = client_savings[4:6]

# Use slicing to create simple_savings
simple_savings = client_savings[:4]

# Use slicing to create complex_savings
complex_savings = client_savings[-6:]

# Print out simple_savings and complex_savings
print(investment_saving)
print(simple_savings)
print(complex_savings)

print(investment_saving + simple_savings)