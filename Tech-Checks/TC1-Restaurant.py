# PROG 1700 – Tech Check #1
# Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.

def main():
    # Welcome
    print("\n♡Welcome to Myah Bowley's restaurant ala cat♡\n")

    # Menu
    print("------------MENU------------\nFish and CatNips.....$15.00\nMeow-Wow! Steak......$29.00\nMeowstr Salad........$19.00\nCatburger and Fries..$21.00\n----------------------------\n")

    # User input
    ogBill = float(input("Please enter your original bill amount: "))

    # Declaring Variables:
    tax = float(ogBill) * 0.15
    tip = float(ogBill) * 0.20
    totalPrice = float(ogBill) + tax + tip

    # Printing Reciept
    print("♡Your Meow-orininal bill amount is: ${0:,.2f}".format(ogBill)) 
    print("♡Your tax is: ${0:,.2f}".format(tax))
    print("♡Your tip is: ${0:,.2f}".format(tip))
    print("♡Your Meow-tastic total is: ${0:,.2f}".format(totalPrice))

main()
