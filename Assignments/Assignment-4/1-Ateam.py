# Program 1 – The A-Team
# Description: Design and write a program that reads the text from a provided text file into a list, displays the 
# text on-screen, makes some alterations to the text and outputs the changed text to the screen, then saves the 
# altered text as a new file. 

# Altered Text must include:
#   - Add a line number (starting with line number 1) to the beginning of each line of text in the file.
#   - Any line of text that is longer than twenty characters should be converted to all lowercase letters.
#   - Any line 20 or less characters long should be converted to all uppercase letters.
#   - Your program should randomly select a line in the text and OMIT it from any output.

# Once all text alterations are complete, output the altered text to the console, and finish by saving the altered
# text to a new text file. Every time the program is run it should pick a different random line of text and you
# can assume the file doesn’t contain any commas. Although a text file is provided, your finished program
# should work with any text-based file, not just the original A-Team text

# This program has no user inputs. When run, it should produce output similar to the screenshot shown below, as well as save the altered text into a new text file. Subsequent runs of the program should omit different random lines of text, and overwrite the current contents of the new file.

# PSEUDO CODE
# 1) DONE print entire txt file without changes (printOriginalText function)

# 2) DONE Alter text by adding a number before each printed line (printAlteredText function)
# 3) DONE Any line of text that is longer than twenty characters should be converted to all lowercase letters.
# 4) DONE Any line 20 or less characters long should be converted to all uppercase letters.
# 5) DONE Your program should randomly select a line in the text and OMIT it from any output. (including the number before the line, without messing up the order)

# 6) DONE Add each altered line to a new txt file

import random

# Function that will print all original text
def printFileText(fileName):
    """insert name of File you want to be printed. File should already be opened"""

    for line in fileName: # loops through each line and prints
        print(line, end="")

# Function that will print all altered text
def printAlteredText(originalFile, alteredFile):
    """insert name of your original file, and the file that will be altered. Files should already be opened"""
    originalFile.seek(0) # resets cursor to beginning --> found online
    number = 0

    # Finding random line to omit
    randomLine = random.choice(list(originalFile)) # Turns file into a list, so random.choice can select a random iteration --> Found online

    originalFile.seek(0) # resets cursor to beginning

    for line in originalFile: # loops through each line and prints number & line
        number += 1
        if line == randomLine: # Omit the randomly selected line
            print(number, ":" )
            alteredFile.write(str(number) + ":" + str("\n")) # writing to new txt file
        elif len(line) > 20: 
            line = line.lower()
            print(number, ":", line, end="")
            alteredFile.write(str(number) + ":" + str(line)) # writing to new txt file
        else: # elif len(line) <= 20:
            line = line.upper()
            print(number, ":", line, end="")
            alteredFile.write(str(number) + ":" + str(line)) # writing to new txt file

    # Possibly have separate function that will save the altered text to a .txt file

def main():
    fileName1 = "Files\\ateam_Original.txt"
    accessMode1 = "r" # read
    original_Ateam = open(fileName1, accessMode1)

    fileName2 = "Files\\ateam_Altered.txt"
    accessMode2 = "w" # write
    altered_Ateam = open(fileName2, accessMode2)

    print("\n-------------------------------------------------\nOriginal Text\n-------------------------------------------------")
    printFileText(original_Ateam)
    print("\n\n-------------------------------------------------\nAltered Text\n-------------------------------------------------")
    printAlteredText(original_Ateam, altered_Ateam)

    original_Ateam.close()
    altered_Ateam.close()


main()
