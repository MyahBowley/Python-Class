import math

def gallonsPaint():

  square_feet_per_gallon = 150.0

  # Intro messages
  print("Welcome to the Paint Shop!")
  print("This program will help you calculate how many cans of paint you need to buy, based on the dimensions of your room.")

  # INPUT
  # Get Dimensions of the room
  length = float(input("\nEnter the length of the room, in feet: "))
  width = float(input("Enter the width of the room, in feet: "))
  height = float(input("Enter the height of the room, in feet: "))

  # PROCESSING
  # Calculate the area of the walls
  totalArea = (length * height * 2) + (width * height * 2)

  # Divide the area by 150 square feet and
  # round number of gallons up to the nearest whole number
  gallons_of_paint = math.ceil(totalArea / square_feet_per_gallon)

  # OUTPUT - Display number of gallons needed
  print("\nThe total wall area of your room is {0} square feet.".format(totalArea))
  print("You will need {0} gallon(s) of paint. \n\nHappy Painting!".format(gallons_of_paint))

gallonsPaint()
