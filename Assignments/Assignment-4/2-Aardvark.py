# Program 2 – The Itsy Bitsy Aardvark
# Description: Design and develop a program that presents the user with a “Mad Libs” type game, where a random 
# choice of words are read from a file, then interjected into a story read from another file.


import csv

# Function that adds list of choices to a MADLIBZ story
def addChoicesToStory(listOfChoices, story):
    # ['aardvark', 'jumped', 'impressive', 'exploded', 'president', 'messed', 'dreadfully']
    #     0           1            2           3            4           5           6
    print("\n-----------------------------------------\n\tYour Completed Story:\n-----------------------------------------\n")
    
    # Loop to switch all the _1_ with correct words
    for i in range(len(listOfChoices)): # loops runs for the amount of indexes
        wordToSwitch = "_" + str(i+1) + "_" # allows us to match the _1_ spots to switch the words
        story = story.replace(wordToSwitch, listOfChoices[i]) # replacing the _1_ with the parallel word in list

    # loops through each line and prints
    for line in story:
        print(line, end="")


def main():
    userChoicesList = []

    # Title
    print("The Itsy Bitsy Aardvark")

    fileName1 = "Files\\the_story_file.txt"
    accessMode1 = "r"
    storyFile = open(fileName1, accessMode1)
    StoryContent = storyFile.read()

    fileName2 = "Files\\the_choices_file.csv"
    accessMode2 = "r" 
    with open(fileName2, accessMode2) as storyChoices:
        dataFromFile = csv.reader(storyChoices) # turning all lines into a list
        #For loop that will run once per row
        for row in dataFromFile:
            userChoice = input("\nPlease choose {0}:\na) {1}\nb) {2}\nc) {3}\nd) {4}\ne) {5}\nEnter choice (a-e): ".format(row[0], row[1], row[2], row[3], row[4], row[5])).lower()

            # Convert letter to the value it represents before appending to list
            while True:
                if userChoice == "a":
                    userChoicesList.append(row[1].upper())
                    break
                elif userChoice == "b":
                    userChoicesList.append(row[2].upper())
                    break
                elif userChoice == "c":
                    userChoicesList.append(row[3].upper())
                    break
                elif userChoice == "d":
                    userChoicesList.append(row[4].upper())
                    break
                elif userChoice == "e":
                    userChoicesList.append(row[5].upper())
                    break
                else: # invalid input
                    userChoice = input("Enter choice (a-e): ")

    addChoicesToStory(userChoicesList, StoryContent)

    storyFile.close()            
    # storyChoices.close()  <-- 'with' closes automatically


main()
