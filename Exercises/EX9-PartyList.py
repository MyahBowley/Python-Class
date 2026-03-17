# Exercise 9: Party Guest List:
#   – Ask the user to enter the names and ages of everyone attending a party
#   – Store the information in a CSV file

"""
Student: Myah Bowley
Student ID: w0523461
"""

def main():
  programRunning = True
  name = ""
  age = 0

  fileName = "..\\Files\\partyList.csv"
  accessMode = "w"
  myFile = open(fileName, accessMode)

  while programRunning != False:
    name = input("Insert the name of a party guest, or type 'end' to end the program: ").lower()
    if name == "end":
      programRunning = False
      myFile.close()
    else:
      myFile.write(str(name) + ", ")
      age = input("What is the party guest's age?                                      ")
      myFile.write(str(age) + "\n")

main()
