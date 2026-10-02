"""
EXERCICE 1
---
- Update the amount of the cash saving to be 175 euros instead of 100.
- Change the identification of the "saving" element to "livret A".
"""
#  List of savings
client_savings = ["cash", 100, "saving", 200, "investment", 500, "realstate", 1000, "bitcoin", 100000]

# Correct the cash amount
client_savings[1] = 175

# Change "saving" to "livret A"
client_savings[2] = "livret A"

# Verify the new values are set
print(client_savings)

"""
EXERCICE 2
---
- Use the + operator to paste the list `["PEL", 22340]` to the end of the `client_savings` list. Store the resulting list as client_savings_1.
- Further extend client_savings_1 by adding data on your LDD. Add the string "LDD" and float 34548. Name the resulting list client_savings_2.
"""
# Add PEL data to client_savings, new list is client_savings_1
client_savings_1 = client_savings + ["PEL", 22340]

# Add LDD data to client_savings_1, new list is client_savings_2
client_savings_2 = client_savings_1 + ["LDD", 34548]

print(client_savings_2)