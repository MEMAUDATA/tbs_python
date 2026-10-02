''' Toulouse Business School MSc AIBA

Course: Python for Data Science
Author: Dr. Samia Drappeau
Version: v1.0
'''

"""
Without Variables
"""
# How much is your $100 worth after 7 years?
print(100 * 1.1**7)


"""
With Variables
"""
initial_invest = 100
roi = 1.2 #20% <---
duration = 7
print(initial_invest * roi**duration)
# > 358.32


"""
Python Types
"""
print(type(roi))
# > float

print(type(duration))
# > int

text1 = "Return on Investment"
text2 = 'This works too'
print(type(text1), type(text2))
#> str, str

is_ok = False
print(type(is_ok))
#> bool