''' Toulouse Business School MSc AIBA

Course: Python for Data Science
Author: Dr. Samia Drappeau
Version: v1.0
'''

def add_numbers(x, y):
  """
  Add two numbers passed as arguments
  and return the sum
  """
  total = x + y
  return total


def main():
  x = 10
  y = 8
  sum = add_numbers(x, y)
  print(sum)
  
if __name__ == '__main__':
    main()

