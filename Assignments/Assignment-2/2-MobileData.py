# Program 2 – Erehwon Mobile Data Plans
# Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

# Student Name:  Myah Bowley

def main():
    # Declare variables
    dataUsage = 0
    totalCharge = 0.0

    # Variables: Total Data Usage rates
    upto200Mb = 20.00 # Up to and including 200Mb = $20.00 flat rate
    over200Mb = 0.105 # > 200Mb and >= 500Mb = $0.105 per Mb
    over500Mb = 0.110 # > 500Mb and >= 1Gb = $0.110 per Mb
    over1G = 118.00   # > 1Gb = $118.00 flat rate

    # Welcome / User Input
    print("-------------------------\nWelcome to Erewhon Mobile")
    dataUsage = float(input("Enter data usage (Mb): "))

    # Data Usage calculator
    if dataUsage >= 0 and dataUsage <= 200:
        totalCharge = upto200Mb
    elif dataUsage > 200 and dataUsage <= 500:
        totalCharge = over200Mb * dataUsage
    elif dataUsage > 500 and dataUsage <= 1000:
        totalCharge = over500Mb * dataUsage
    elif dataUsage > 1000:
        totalCharge = over1G
    else:
        print("Oops! That is not recognized! Please try again and input a valid amount of data usage.")

    # Output
    print("Total charge is ${0:,.2f}\n-------------------------".format(totalCharge))

main()
