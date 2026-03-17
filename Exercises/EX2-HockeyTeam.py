# LAB 2 - HOCKEY TEAM
# Write a program that will ask the user to enter the name of a hockey team, 
# how many wins the team has, and how many losses #the team has.

# The program should calculate and display a single string output containing the team name,
# its win-loss ratio, and the win percentage formatted to 4 decimal places.

# Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

# Purpose/Concepts: Input and output to screen, string concatentation, 
# string formatting, datatype casting, simple math operations

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
   teamName = input("Please enter your hockey team name: ")
   wins = input("How many wins has {0} had? ".format(teamName))
   losses = input("How many losses has {0} had? ".format(teamName))

   #win percentage is (wins / by total games) * 100grdfvxc
   winPercentage = (float(wins) / (float(wins) + float(losses))) * 100

   print("SCORE: {0} has had {1} win(s) and {2} loss(es)! Thats a win percentage of {3:.4f}%!!".format(teamName, wins, losses, winPercentage))

    # YOUR CODE ENDS HERE

main()
