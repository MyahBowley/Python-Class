# Program 2 – Message Redaction
# Description:   Design and write a program that counts and removes all desired letters from any user-entered sentence or phrase.

# PSEUDO CODE
    # While loop until user types "quit"
    # Ask user for phrase
    # Ask user for redactedLetters
    # amountOfLetters = len(redactedLetters)
    # 2nd loop: we for loop through each letter in redactedLetters (with amountOfLetters as the amount of times we loop), and if each letter is in the phrase we list.remove(x) it from the redactedPhrase list
    # Display the amountOfLetters we redacted for user.
    # display the redactedPhrase in proper format (possibly another loop?)
    # The entire program loops again until user types "quit" as their phrase
    # If user types "quit" ask "are you sure you would like to quit? (yes/no):" and if they type "no" then quit is the phrase

"""
Student Name:  Myah Bowley
"""

# FUNCTIONS
def stringToList():
     # Turning the redacted letters from a string into a list
    redactedLetters = input("\nType a comma-separated list of letters to redact: ")
    redactedLetters = redactedLetters.split(",")   
    return redactedLetters

def letterToUnderscore(phrase, redactedLetters):
    # Nested FOR loops to switch redactedLetters to "_"

    finalPhrase = ""
    redactedPhrase = []

    for character in phrase:
        underscoreAdded = False
        for character2 in redactedLetters:
            if character.lower() == character2.lower():
                finalPhrase += "_"
                underscoreAdded = True
                # lettersTaken = redactedPhrase.append("i")
                redactedPhrase.append(character) #storing the redacted character to count it later
                break
        if underscoreAdded == False:
            finalPhrase += character
    return finalPhrase, redactedPhrase

def quitLoop():
    # Asking the user if they are sure they want to exit the loop
    while True:
        yesOrNo = input("\nIf you want to quit, type 'yes'.\nIf 'quit' was the phrase you wanted to use, type 'no': ").lower()
        if yesOrNo == "yes":
            return "yes"
        elif yesOrNo == "no":
            return "no"
        else:
            print("Sorry, that was not a valid answer.")
            break

def main():
    # Declaring Variables
    phrase = ""
    redactedLetters = []
    # redactedPhrase = []

    # Welcome / user input
    while phrase != "quit":
        # resetting the redactedLetters and redactedPhrase each loop when we do a new phrase
        redactedLetters = []
        finalPhrase = ""
        lettersTaken = [] #all the letters we removed from the sentence

        # Welcome / User input
        phrase = input("\nType a phrase (or type 'quit' to exit program): ") 

        # Quitting if user typed "quit"
        if phrase == "quit":
            quit = quitLoop()
            if quit == 'yes':
                break
            else:
                pass
        
        redactedLetters = stringToList()
        
        finalPhrase, lettersTaken = letterToUnderscore(phrase, redactedLetters)

        # Finding the amount of indexes in redactedLetters
        # amountOfLetters = len(redactedLetters)

        # Output
        print("\nNumber of letters redacted: {}".format(len(lettersTaken)))
        print("\nRedacted phrase: {}\n-----------------------------------------------------------------".format(finalPhrase))
        phrase = ""     # resetting phrase so while loop continues


    print("\nThank you for using this program!\n")


main()

# TESTS
    # Imagination is more important than knowledge.
    # a,i,k,j

    # The medium is the message!
    # m,e,b

    # I want to put a ding in the universe.
    # a,g,x,n
