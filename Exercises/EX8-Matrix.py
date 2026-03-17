# Write code that creates a 5x5 matrix and fills the matrix with random numbers between 1-100

# Your first line of code must be:
# matrix = []

# Once your matrix is created and filled, print the values to the console in the following format

# 1 4 60 3 7
# 23 5 15 3 6        
# 55 1 1 7 3           
# 34 77 3 99 44
# 2 88 71 35 16 

"""
Student: Myah Bowley
Student ID: w0523461
"""

import random

def main():
  # Declaring empty lists
  # First line must be "matrix = []"
  matrix = []
  rowList = []        

  # Declaring Variables
  rowVariable = 0       # will be first number in each row
  columnVariable = 0    # will be numbers making up columns

  # generating 5x5 matrix / printing in 5x5 format
  for row in range(5):
    rowList = []      # creating new, empty rowList for each row iteration
    rowVariable = random.randint(1, 100)  # gen random num & store in variable
    rowList.append(rowVariable)           # add random number to list
    print(rowVariable, end=" ")           # print random number
    for col in range(5):
      if col == 4:
        matrix.append(rowList)          # after 4 indexes, add this row to matrix
        print("")                       # after 4 indexes, create new line
      else:
        columnVariable = random.randint(1, 100) # gen ran num & store in variable
        rowList.append(columnVariable)          # add random number to list
        print(columnVariable, end=" ")          # print random number

  # printing list to prove variables were saved properly to lists
  print("\nHere is the matrix, not formatted:") 
  print(matrix)

main()
