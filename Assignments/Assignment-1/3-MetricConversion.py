#Program 3 – Imperial to Metric Conversion
# Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

def main():
    # PSEUDOCODE:
    # Variables: (user input (convert to float)) tons, stone, pounds, ounces. 
    # (formula) ouncePerImTon, ouncePerStone, OuncePerPound, ouncePerKilo, kiloPerMeTon, 
    # (other) totalOunces, totalKilos, metricTons

    # CODE ORDER:
    # welcome, & user input for tons, stone, pounds, ounces
    # Formulas: (hardcode numbers as variables) ouncePerImTon, ouncePerStone, ouncePerPound, ouncePerKilo, kiloPerMeTon
    # total ounces = 35840 * tons + 224 * stone + 16 * pounds + ounces
    # total kilos = total ounces / 35.274
    # metric tons = Int(kilos/1000)
    # Final result: show metricTons, totalKilos, and totalGrams using .format()

    # Declaring formula variables
    ouncePerImTon = 35840     # number of ounces in 1 imperial ton
    ouncePerStone = 224       # number of ounces in 1 stone
    ouncePerPound = 16        # number of ounces in 1 pound
    ouncePerKilo = 35.274     # number of ounces in one kilogram
    kiloPerMeTon = 1000       # kilograms in 1 metric ton

    # Welcome
    print("-----------------------------\nImperial To Metric Conversion\n-----------------------------")
    tons = float(input("Enter the number of tons: "))
    stone = float(input("Enter the number of stone: "))
    pounds = float(input("Enter the number of pounds: "))
    ounces = float(input("Enter the number of ounces: "))

    # FORMULAS
    # Convert everything to ounces
    totalOunces = ouncePerImTon * tons + ouncePerStone * stone + ouncePerPound * pounds + ounces
    # Convert ounces to kilograms
    totalKilos = (totalOunces / ouncePerKilo)
    # Convert kilograms to metric tons and grams
    metricTonsWhole = int(totalKilos/kiloPerMeTon)
    leftOverKilos = int(totalKilos - (metricTonsWhole * kiloPerMeTon))
    grams = (totalKilos - int(totalKilos)) * kiloPerMeTon

    # Final result
    print("-----------------------------\nThe metric weight is: {0:,.0f} metric tons, {1:,.0f} kilos, and {2:,.1f} grams.\n-----------------------------".format(metricTonsWhole, leftOverKilos, grams))



main()
