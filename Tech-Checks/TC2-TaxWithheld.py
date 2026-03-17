# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 

# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
    #Declaring Values
    provincialTaxRate = 0.06
    federalTaxRate = 0.25
    dependantTaxRate = 0.02 #per dependant

    #Introduction
    print("--------------------------\nTax Withholding Calculator\n--------------------------")
    weeklySalary = float(input("Please enter the full amount of your weekly salary: "))
    dependantsAmount = int(input("How many dependents do you have?: "))
    print("--------------------------\n          Receipt\n--------------------------")

    #calculations
    provincialTaxWithheld = provincialTaxRate * weeklySalary
    federalTaxWithheld = federalTaxRate * weeklySalary
    totalDependantDeduction = (dependantTaxRate * dependantsAmount) * 1000
    totalWithheldTax = (provincialTaxWithheld + federalTaxWithheld) - (totalDependantDeduction)
    totalTakeHomePay = weeklySalary - totalWithheldTax

    #Recipt
    print("Provincial Tax Withheld:              ${0:,.2f}".format(provincialTaxWithheld))
    print("Federal Tax Withheld:                ${0:,.2f}".format(federalTaxWithheld))
    print("Dependant Deduction for {0} dependents: ${1:,.2f}".format(dependantsAmount, totalDependantDeduction))
    print("Total Withheld:                      ${0:,.2f}".format(totalWithheldTax))
    print("Total Take-Home Pay:                 ${0:,.2f}".format(totalTakeHomePay))

main()
