# Build a Python program to calculate whether a surcharge will be applied, based on the weight of an airline passenger's luggage.
# When passengers check in at the airline counter, they are allowed a maximum luggage weight of 50 lbs.
# If luggage exceeds the weight limit, a $25 surcharge is applied.
# Write a program to allow passengers to enter the total weight of their luggage and calculate whether to apply a surcharge.
# Your program should display a message indicating whether a surcharge is required, or not.

"""
Student Name: Myah    
Program Title:  IT Programming
Description: surcharge calculator
"""
#Maximum luggage weight 50 lbs
# > 50 lbs --> $25 surcharge

weightLimit = 50

print("------------------\nHello, welcome to the AirCanada airport booth!\n------------------")
luggageWeight = float(input("Please enter your luggage weight in pounds: "))

if luggageWeight <= weightLimit:
  print("Your luggage meets the weight limit of 50 lbs.")
else:
  luggageWeight > weightLimit
  print("Your luggage does not meet the weight limit of 50 lbs.\nUnfortunately you must pay the surcharge of $25.")

print("------------------\nThank you for choosing AirCanada! You may go ahead.\n------------------")
