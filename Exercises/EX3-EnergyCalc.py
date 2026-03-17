"""
Student Name:  Myah Bowley  
Program Title:  Energy Calculator - BROKEN
Description:   Debugging practice
"""

# The code given to you has many bugs. Correct them using the debugger and comment what you changed.

def main():
    
    print("Energy Calculator")
    print("\nThis program will calculate how much you pay for electricity for")
    print("a particular device, based on the wattage of the device and how")
    print("many hours the device was in use.")
    print("\nCalculations are based on a cost of 12.65 cents per kiloWatt hour.")

    kwhPrice = 12.65
    avgDaysInAMonth = 30.42
    monthsInYear = 12

    deviceWattage = float(input("\nEnter the wattage of the device: "))
    hoursUsedPerDay = float(input("Enter how many hours per day the device is in use: "))


    # Bug here: to convert W to kW we divide by 1000, not 100
    costPerHour = ((deviceWattage /1000) * kwhPrice) / 100
    # Bug here: costPerDay is not equal to hoursUsedPerDay. I corrected the formula
    costPerDay = hoursUsedPerDay * costPerHour 
    # Bug here: we don't need to multiply by 60 at the end
    costPerMonth = avgDaysInAMonth * costPerDay
    costPerYear = monthsInYear * costPerMonth
    kwhPerDay = (deviceWattage /1000) * hoursUsedPerDay

  

    # bug here: you inputed deviceWattage twice and didn't input hoursUsedPerDay at all; also, not technically a bug, but, it would be good to have consistancy with decimal formatting, so I fixed that;
  # Also not a bug, but a grammatical mistake corrected: changed hour to hour(s) as we will likely have a user input of multiple hours
    print("\nElectrical cost for a device using {0:.2f} watts for {1:.2f} hour(s) per day:".format(deviceWattage, hoursUsedPerDay))
    # not technically a bug, but not good practice to add inconsistant decimal spaces. I changed it to show 5 spaces rather then 1
    print("\tCost Per Hour:\t${0:.5f}".format(costPerHour))
    print("\tCost Per Day:\t${0:.5f}".format(costPerDay))
    print("\tCost Per Month:\t${0:.5f}".format(costPerMonth))
    # bug here: you mistakenly were entering the costperMonth instead of costPerYear; changed decimal formatting to 5 decimal places in case the value is small
    print("\tCost Per Year:\t${0:.5f}".format(costPerYear))
    print("\tkWh Per Day:\t{0:.2f}".format(kwhPerDay))

#Do not change any of the code below!
if __name__ == "__main__":
    main()
