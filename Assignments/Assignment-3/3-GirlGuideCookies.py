# Program 3 – Girl Guide Cookies
# Description:   The organizers of the annual Girl Guide cookie sale event want to raise the stakes on the number of cookies sold and are offering cool prizes to those guides who go above and beyond in their sales efforts. The organizers want a program to print the guide list and their prizes.

"""
Student Name:  Myah Bowley
"""

    # The highest selling guide gets a trip to the Girl Guide Jamboree, any guides selling above average get a badge, and any guides selling at least one box get to split the remaining cookies, with guides selling no boxes shut out of all prizes.
    # (Hint: Some potential solution ideas: Research parallel arrays or two-dimensional lists

def prizes(guideNames, guideSales, averageBoxesSold):
    prizeList = ["Trip to the Jamboree", "Super Seller Badge", "Left over cookies", " "]
    print("\nGuide \t\t\t\t Prizes Won:")
    print("--------------------------------------------------------------")

    for i in range(len(guideNames)):
        name = guideNames[i]
        sales = guideSales[i]

        if sales == 0:                  # Sold 0
            prize = prizeList[3]
        elif sales == max(guideSales):  # Sold the most
            prize = prizeList[0]
        elif sales >= averageBoxesSold: # More or equal to average sales sold
            prize = prizeList[1]
        else:                           # At least 1 box sold
            prize = prizeList[2]
        print("{0}\t\t\t\t- {1}".format(name, prize))

def main():
    # VARIABLES
    amountOfGuides = 0

    nameOfGuide = ""
    boxesSoldBy1 = 0 # Boxes sold by the guide we just named (1 meaning 1 individual)

    totalBoxesSold = 0
    amountOfGuides = 0
    averageBoxesSold = 0

    # Lists
    guideNames = [] # Ex: [Amy, Joy, Rae, Sara]
    guideSales = [] # Ex: [5,   17,  11,  0]

    # Welcome / User Input
    amountOfGuides = int(input("Enter the number of guides selling cookies: "))

    # Based on the amountOfGuides the user entered, this will repeat that many times
    for guide in range(amountOfGuides):
        # Get guide Name
        nameOfGuide = input("\nEnter the name of guide #{0}: ".format(guide + 1))
        guideNames.append(nameOfGuide)  # Add guide Name to list

        # Get boxes sold by guide
        boxesSoldBy1 = int(input("Enter the number of boxes sold by {0}: ".format(nameOfGuide)))
        guideSales.append(boxesSoldBy1) # Add boxes sold by guide to list

        totalBoxesSold += boxesSoldBy1

    # Finding average
    averageBoxesSold = totalBoxesSold / amountOfGuides
    print("\n\nThe average number of boxes sold by each guide was {0:.1f}".format(averageBoxesSold))

    # Print prizes for each guide!
    prizes(guideNames, guideSales, averageBoxesSold)


main()
