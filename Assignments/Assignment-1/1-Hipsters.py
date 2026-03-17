# Program 1 – Hipster's Local Vinyl Records
# Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

def main():
    # PSEUDOCODE
    # Variables: name, distance(in Km), recordsCost, deliveryRate, tax, deliveryCost, purchaseCost, totalCost, salesTax (14% of the price)
    # welcome
    # user is asked for name (capitalize first letter with .title)
    # user is asked distance in km (change to float)
    # user is asked for cost of records (recordsCost variable) (change to float)
    # Program displays reciept:
    # print customer name
    # print deliveryCost
    # print recordsCost (plus tax)
    # print totalCost

    # Delaring variables
    name = ""
    distance = 0 #in Kilometers
    recordsCost = 0
    deliveryRate = 15 # Delivery is charged at a rate of $15 per kilometer.
    tax = 0.14
    
    # Questions / User Input
    print("-----------------------------\nHipster's Local Vinyl Records - Customer Order Details\n-----------------------------")
    name = (input("Enter the customer's name: "))
    distance = float(input("Enter the distance in kilometers for delivery: "))
    recordsCost = float(input("Enter the cost of records purchased: $"))

    # Formulas
    deliveryCost = deliveryRate * distance
    salesTax = recordsCost * tax
    purchaseCost = recordsCost + salesTax
    totalCost = deliveryCost + purchaseCost

    # Print receipt
    print("-----------------------------\nPurchase summary for {0}".format(name.title()))
    print("Delivery Cost: ${0:,.2f}".format(deliveryCost))
    print("Purchase Cost: ${0:,.2f}".format(purchaseCost))
    print("Total Cost   : ${0:,.2f}\n-----------------------------".format(totalCost))
    

main()
