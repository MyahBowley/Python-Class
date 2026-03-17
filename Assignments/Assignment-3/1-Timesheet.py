# Program 1 – Time Sheet
# Description:   Design and write a program that accepts the number of hours worked on each of five work days from the user, then displays different information calculated about those entries as output. 

"""
Student Name:  Myah Bowley
"""

# Determining the day(s) where the most hours were worked
def daysWithMostHours(hrsWorkedInDay): # ex [4, 9, 3, 7, 6]
    # highestHours = max(hrsWorkedInDay)
   
    # Finding the index of it (index + 1 = day)
    # highestDays = hrsWorkedInDay.index(highestHours) + 1 # + 1 because it is 0 based counting
    # return highestDays, highestHours
    # print("Day {0} when you worked {1} hour(s).".format(highestDays, highestHours)) 

    dayMaxValue = []
    dayMax = []
    count = 0
    for hrsWorked in hrsWorkedInDay:
        
        if len(dayMaxValue) == 0:
            # Setting first index to be the values we want to save
            dayMaxValue.append(hrsWorked)
            dayMax.append(count)
        elif hrsWorked > dayMaxValue[0]:

            # Empty the lists
            dayMaxValue = []
            dayMax = []

            # Setting first index to be the values we want to save
            dayMaxValue.append(hrsWorked)
            dayMax.append(count)
        # If hours worked is the same as the previous one then we have matching which is why we have a list to store them
        elif hrsWorked == dayMaxValue[0]:
            # Add them to the end of the list
            dayMaxValue.append(hrsWorked)
            dayMax.append(count)
        count += 1

    for i in range(len(dayMax)):
        dayValueMax = dayMax[i]
        dayValueMax = int(dayMax[i]) + 1
        # print("Day #", dayValueMax, "when you worked", dayMaxValue[i], "hours.")
        print("Day {0} when you worked {1} hour(s).".format(dayValueMax, dayMaxValue[i]))

def daysWithBadHours(hrsWorkedInDay):
    insufficientHours = 7
    count = 0
    for hrsWorked in hrsWorkedInDay:
        if hrsWorked < insufficientHours:
            print("Day {0} when you worked {1} hour(s).".format(count + 1, hrsWorked))
        count += 1

    
def main():
    # VARIABLES
    hrsWorkedInDay = []
    # insufficientHours = 7
    daysWorked = 5

    # Welcome / User Input
    for x in range(daysWorked):
        day = x + 1                 # +1 so we don't start on day 0
        hours = int(input("Enter hours worked on Day #{}: ".format(day)))
        hrsWorkedInDay.append(hours)   # Adding to list
        
    # FUNCTION determining the day(s) where the most hours were worked
    # highestDays, highestHours = daysWithMostHours(hrsWorkedInDay)

    # Calculating the sum of the list hrsWorkedInDay
    sumOfHours = sum(hrsWorkedInDay)

    # Calculating the daily average of hours worked:
    # Average = (Sum of all numbers) / (how many numbers there were)
    averageHours = sumOfHours / daysWorked

    # Output
    print("-----------------------------------------------")
    print("The most hours worked was on:")
    daysWithMostHours(hrsWorkedInDay)
    # print("Day {0} when you worked {1} hour(s).".format(highestDays, highestHours))
    print("-----------------------------------------------")
    print("The total number of hours worked was: {}".format(sumOfHours))
    print("The average number of hours worked each day was: {}".format(averageHours))
    print("-----------------------------------------------")
    print("Days you slacked off (i.e. worked less than 7 hours):")
    # Function determining the day(s) with insufficient hours
    daysWithBadHours(hrsWorkedInDay)
 
    # Print the days and hours slacked off on. Ex:
    # Print("Day {0}: {1} hour(s)".format())


main()
