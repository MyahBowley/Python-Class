"""
Student Name:  Myah Bowley  
Program Title:  The Online Store
Description: Calculate the total to charge an order from an online store in Canada
"""
# ------------------------------ INSTRUCTIONS ------------------------------
# Calculate the total to charge for an order from an online store in Canada
# - Ask user what country they are from and their order total
# - If the user is from Canada, ask which province
# - If the order is from outside Canada do not charge any taxes
# - If the order was placed in Canada calculate tax based on the province
#      - Alberta charge 5% General sales Tax (GST)
#      - Ontario, New Brunswick, Nova Scotia charge 15% Harmonized sales tax
#      - All other provinces charge 11% tax
# - Tell the user the total with taxes for their order
# --------------------------------------------------------------------------
# What do you need to test to ensure your code works correctly?
# - Someone who is from outside Canada (no tax)
# - Someone from Alberta, Canada (5% tax)
# - Someone from Ontario, Canada (15% tax)
# - Someone from Canada from a different province (e.g. Quebec) (11% tax)
# --------------------------------------------------------------------------

# Declaring Variables
country = "" #user input
province = "" #user input
pricePreTax = None #user input (their order total)
outSideCanada = None #changes to T/F depending on user input for country

# Tax variables
albertaTax = 0.05
harmonizedTax = 0.15 # applies to: Ontario, New Brunswick, and Nova Scotia
otherTax = 0.11 # Other province tax
salesTax = None # how much is paid for tax
finalPrice = None # Final price + sales tax

# Welcome + User Input
print("Welcome to the Multiple Moose Merchandise Store!")
pricePreTax = float(input("How much money was your order? $"))
country = input("What country are you from? ").lower()

# Canadian options
if country == "canada":
  province = input("Hello fellow Canadian! What province are you from? ").lower()
  outSideCanada = False
  # Provincial tax for ALBERTA
  if province == "alberta" or province == "ab":
    salesTax = albertaTax * pricePreTax
    finalPrice = pricePreTax + salesTax
    print("Your final price with taxes included is: ${0:,.2f}".format(finalPrice))
  # Provincial tax for ON, NB, and NS
  elif province == "ontario" or province == "on" or province == "new brunswick" or province == "nb" or province == "nova scotia" or province == "ns":
    salesTax = harmonizedTax * pricePreTax
    finalPrice = pricePreTax + salesTax
    print("Your final price with taxes included is: ${0:,.2f}".format(finalPrice))
  # Provincial tax for ALL OTHER PROVINCES
  elif province == "british columbia" or province == "bc" or province == "manitoba" or province == "mb" or province == "newfoundland and labrador" or province == "nl" or province == "northwest territories" or province == "nt" or province == "nunavut" or province == "nu" or province == "prince edward island" or province == "pe" or province == "pei" or province == "quebec" or province == "qc" or province == "saskatchewan" or province == "sk" or province == "yukon" or province == "yt":
    salesTax = otherTax * pricePreTax
    finalPrice = pricePreTax + salesTax
    print("Your final price with taxes included is: ${0:,.2f}".format(finalPrice))
  # if user input isn't a province
  else:
    print("Oops! Thats not a Canadian province! Please try again and correctly type a Canadian province!")

# Worldwide options
else:
  outSideCanada = True
  print("Hello worldwide user!\nTo thank you for your worldwide purchase, you will not be charged with tax!\nYour final price is: ${0:,.2f}".format(pricePreTax))

print("Thank you for shopping with us! Your product(s) are on their way!")
