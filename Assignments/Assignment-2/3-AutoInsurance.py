# Program 3 – Auto Insurance
# Write a program that computes monthly insurance according to the provided schedule. 

# Student Name:  Myah Bowley

def main():
    # Variable Declaration
    gender = "" 
    age = ""
    purchasePrice = 0.0

    # Variables: Vehicle multipliers
    male15To24 = 0.25 / 12
    male25To39 = 0.17 / 12
    male40To69 = 0.10 / 12
    female15To24 = 0.20 / 12
    female25To39 = 0.15 / 12
    female40To69 = 0.10 / 12

    # Function creation
    def ageDecisionMale():
        if age >= 15 and age < 25:
            monthlyInsur = purchasePrice * male15To24
            return monthlyInsur
        elif age >= 25 and age < 40:
            monthlyInsur = purchasePrice * male25To39
            return monthlyInsur
        elif age >=40 and age < 70:
            monthlyInsur = purchasePrice * male40To69
            return monthlyInsur
        else:
            print("Sorry, you unfortunately don't qualify for our insurance policies. You must be between the ages of 15 and 69.")

    def ageDecisionFemale():
        if age >= 15 and age < 25:
            monthlyInsur = purchasePrice * female15To24
            return monthlyInsur
        elif age >= 25 and age < 40:
            monthlyInsur = purchasePrice * female25To39
            return monthlyInsur
        elif age >=40 and age < 70:
            monthlyInsur = purchasePrice * female40To69
            return monthlyInsur
        else:
            print("Sorry, you unfortunately don't qualify for our insurance policies. You must be between the ages of 15 and 69.")

    # Welcome / User Input
    print("-------------------------\nAuto Insurance Calculator")
    gender = input("Are you 'Male' or 'Female' or 'Other': ").lower()
    age = int(input("\nEnter your age: "))
    purchasePrice = float(input("\nEnter the purchase price of the vehicle: $"))

    # Formula / Calculations
    if gender == "male" or gender == "m" or gender == "other" or gender == "o":
        monthlyInsur = ageDecisionMale()
        print("\nYour monthly insurance will be ${0:,.2f}\n-------------------------".format(monthlyInsur))
    elif gender == "female" or gender == "f":
        monthlyInsur = ageDecisionFemale()
        print("\nYour monthly insurance will be ${0:,.2f}\n-------------------------".format(monthlyInsur))
    else:
        print("Oops! Thats not an input we can process! Please restart, and choose 'Male', 'Female', or 'Other' only.")

    # Output
    # print("\nYour monthly insurance will be ${}\n-------------------------".format(monthlyInsur))

main()
