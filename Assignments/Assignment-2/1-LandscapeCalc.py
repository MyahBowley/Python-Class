# Program 1 – Landscape Calculator
# A landscaping company needs a program that computes the price of landscaping for a new housing development. 

# Student Name:  Myah Bowley

def main():
    # Declare variables
    houseNum = 0
    propDepth = 0.0
    propWidth = 0.0
    grass = ""
    trees = 0
    grassCharge = 0.0
    surface = 0.0
    totalCost = 0.00

    # Variables: Constants
    baseLabour = 1000     # in dollars
    surfaceLimit = 5000
    surfaceCharge = 500   # if surface > 5000 square feet add $500
    fescue = 0.05         # in dollars
    bentgrass = 0.02      # in dollars
    campus = 0.01         # in dollars
    treeCharge = 100      # $100 per tree

    # Intro & User Input
    print("Welcome to LandscapersPro cost calculator!")
    houseNum = int(input("\nEnter House Number: "))
    propDepth = float(input("\nEnter property depth (feet): "))
    propWidth = float(input("\nEnter property width (feet): "))
    grass = input("\nEnter type of grass (fescue, bentgrass, campus): ").lower()
    trees = int(input("\nEnter the number of trees: "))

    # Calculations
    surface = propDepth * propWidth

    # Is surface > surfaceLimit
    if surface > surfaceLimit:
        totalSurfaceCharge = surfaceCharge
    else:
        totalSurfaceCharge = 0

    # What type of grass is it?
    if grass == "fescue" or grass == "f":
        grassCharge = surface * fescue
    elif grass == "bentgrass" or grass == "b":
        grassCharge = surface * bentgrass
    elif grass == "campus" or grass == "c":
        grassCharge = surface * campus
    else:
        print("Oops! That isn't one of the following grass types provided by LandscapersPro. Please restart and use only 'fescue', 'bentgrass', or 'campus'.")

    # Charging $ per tree
    totalTreeCharge = treeCharge * trees

    # Adding all the additional costs together
    totalCost = baseLabour + totalSurfaceCharge + grassCharge + totalTreeCharge

    # Output
    print("\nTotal cost for house {0} is: ${1:,.2f}".format(houseNum, totalCost))

main()
