"""
Student Name:   Myah Bowley 
Program Title:  IT Programming
Description:    Exercise 5: Wage Calculator
"""

# Write a program that allows the user to enter the number of hours they worked this week and the dollar amount they make per hour.
# Use these values to calculate the amount of money they made this week.
# If the # of hours exceeds 40 in a week, include the amount of overtime pay they made in the total.
# Overtime pays time-and-a-half (1.5X) the usual hourly wage, and only apply to the # of hours worked over 40.

def main():
    # Declaring Variables
    ot_Threshold = 40        # hours needed to qualify for overtime (ot)
    ot_RateMult = 1.5        # Overtime (ot) Rate Multiplier

    hoursWorked = None       # user input
    hourlyWage = None        # user input  

    ot_hours = None          # How many hours user worked overtime 
    base_ot_Pay = None       # The amount of overtime pay the user gets BEFORE multiplier
    ot_Pay = None            # The amount of overtime pay the user gets AFTER multiplier
    totalEarnings = None     # Total earnings after all calculations
    
    # Intro / User Input
    print("Welcome to the wage calculator")
    hoursWorked = float(input("Please enter the amount of hours you worked this week: "))
    hourlyWage = float(input("Please enter your hourly wage: $"))

    # User DOESN'T qualify for overtime pay
    if hoursWorked <= ot_Threshold:
        totalEarnings = hoursWorked * hourlyWage
        print("------------------------------\nYou didn't qualify for overtime pay.")

    # User DOES qualify for overtime pay
    else:
        ot_hours = hoursWorked - ot_Threshold
        base_ot_Pay = ot_hours * hourlyWage
        ot_Pay = ot_RateMult * base_ot_Pay
        totalEarnings = (hoursWorked * hourlyWage) + ot_Pay # normal pay + ot_Pay
        print("------------------------------\nAmount of overtime hours: {0:,.2f}\nAmount of overtime pay: ${1:,.2f}\nAmount of regular hour pay: ${2:,.2f}".format(ot_hours, ot_Pay, (totalEarnings - ot_Pay)))

    # Result
    print("Here is your total weekly earnings: ${0:,.2f}".format(totalEarnings))


#Do not change any of the code below!
if __name__ == "__main__":
    main()
