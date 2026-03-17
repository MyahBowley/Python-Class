# Program 2 – Weekly Loan Calculator
# Develop a short term loan calculator program as a console application 

def main():
    # PSEUDOCODE
    # VARIABLES: loanAmount, interestRate, years, weeklyPay
    # Welcome "Weekly Loan Calculator"
    # FORMULAS:
    # i = r / 5200
    # weeklyPay = (i / (1 - (1 + i) ** (-52 * n))) * A

    # Declaring Variables
    # interestRate = 0        # annual interest rate
    # loanAmount = 0          # User input
    # years = 0               # User input
    # weeklyInterestR = 0     # formula
    # weeklyPay = 0           # formula

    # formulas go next
    # print weekly payment for user

    # formula variables (don't change, these are conversion rates)
    weeks = 52      # 52 weeks in a year

    # Welcome & User Input
    print("-----------------------------\nWeekly Loan Calculator\n-----------------------------")
    loanAmount = float(input("Enter the amount of loan: "))
    interestRate = float(input("Enter the interest rate (%): "))
    years = float(input("Enter the number of years: "))

    # Formulas
    weeklyInterestR = (interestRate / 100) / weeks
    weeklyPay = (weeklyInterestR / (1 - (1 + weeklyInterestR) ** (-weeks * years))) * loanAmount

    # Result
    print("-----------------------------\nYour weekly payment will be: ${0:,.2f}\n-----------------------------".format(weeklyPay))

main()
