# Tech Check 4 - Provided Starter File

# Take this provided single-grade entry program and re-work it to use a function, 
# to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.

# Student Name: Myah Bowley

def numericGrade(courseName):

    numericGrade = 0.0

    #Gather user inputs
    letterGrade = input("\nPlease enter a letter grade for {}: ".format(courseName)).upper()
    modifier = input("Please enter a modifier (+, - or nothing) : ")

    # Determine base numeric value of the grade
    if letterGrade == "A":
        numericGrade = 4.0
    elif letterGrade == "B":
        numericGrade = 3.0
    elif letterGrade == "C":
        numericGrade = 2.0
    elif letterGrade == "D":
        numericGrade = 1.0
    elif letterGrade == "F":
        numericGrade = 0.0
    else:
        #If an invalid entry is made
        print("You entered an invalid letter grade.")
    
    # Determine whether to apply a modifier
    if modifier == "+":
        if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3

    return numericGrade

def main():
    # Intro
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.")

    # calling functions to calculate numeric grades
    progGrade = numericGrade("PROG1700")
    netwGrade = numericGrade("NETW1700")
    osysGrade = numericGrade("OSYS1200")
    webdGrade = numericGrade("WEBD1000")
    commGrade = numericGrade("COMM1700")
    dbasGrade = numericGrade("DBAS1007")
    
    # Calculating average = sum of grades / number of classes
    gradeAverage = (progGrade + netwGrade + osysGrade + webdGrade + commGrade + dbasGrade) / 6 

    # Output final message and result, with formatting
    print("\n****************************************\n")
    print("The numeric value for PROG1700 is: {0:.1f}".format(progGrade))
    print("The numeric value for NETW1700 is: {0:.1f}".format(netwGrade))
    print("The numeric value for OSYS1200 is: {0:.1f}".format(osysGrade))
    print("The numeric value for WEBD1000 is: {0:.1f}".format(webdGrade))
    print("The numeric value for COMM1700 is: {0:.1f}".format(commGrade))
    print("The numeric value for DBAS1007 is: {0:.1f}".format(dbasGrade))
    print("==================================================")
    print("Your grade point average for the semester is: {0:.1f}".format(gradeAverage))
    print("==================================================")


main()
