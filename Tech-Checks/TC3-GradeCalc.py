# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. 
#   However, an A+ has still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.


def main():
    # DECLARING VARIABLES
    gradeNumberValue = 0 # 1. When we change grade letter into a number
    finalNumericValue = None # 2. After adding modifier and gradeNumberValue
    userGrade = ""
    userModifier = ""
    printOutput = True

    # Constant Variables
    gradeA = 4
    gradeB = 3
    gradeC = 2
    gradeD = 1
    gradeF = 0
    plus = 0.3
    minus = -0.3

    # Welcome & User Input
    print("--------------------------------\nGrade Point Calculator\n\nValid letter grades that can be entered: A, B, C, D, F.\nValid grade modifiers are +, - or nothing.\nAll letter grades except F can include a + or - symbol.\nCalculated grade point value cannot exceed 4.0.\n--------------------------------")
    userGrade = input("Please enter a letter grade: ").upper()
    userModifier = input("Please enter a modifier (+, - or nothing): ")

    # Converting Grade Letter into Number
    if userGrade == "A":
        gradeNumberValue = gradeA 
    elif userGrade == "B":
        gradeNumberValue = gradeB
    elif userGrade == "C":
        gradeNumberValue = gradeC
    elif userGrade == "D":
        gradeNumberValue = gradeD
    elif userGrade == "F":
        gradeNumberValue = gradeF
    else:
        printOutput = False
        print("--------------------------------\nOops! Thats an inalid letter grade. Please restart and try again.")

    # Adding Modifier to Grade
    if userModifier == "+" and userGrade == "A":
        finalNumericValue = gradeA
    elif gradeNumberValue == 0 and (userModifier == "+" or userModifier == "-"):
        printOutput = False
        print("--------------------------------\nOops! You cannot add a modifier to a letter grade of F. Please restart and try again.")
    elif userModifier == "+":
        finalNumericValue = gradeNumberValue + plus 
    elif userModifier == "-":
        finalNumericValue = gradeNumberValue + minus
    elif userModifier == "":
        finalNumericValue = gradeNumberValue
    else:
        printOutput = False
        print("--------------------------------\nOops! Thats Thats an inalid modifier. Please restart and try again.")

    # Output
    if printOutput == True: # Otherwise it'll print this even if an invalid input is made
        print("--------------------------------\nThe numeric value is: {0:.1f}".format(finalNumericValue))

main()
