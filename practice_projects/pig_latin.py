"""A program that takes a word as an input and returns Pig Latin."""
import sys

# List of vowels
vowels = ["a", "e", "i", "o", "u"]

while True:
    print("Welcome to the Pig Latin generator. \n")

    word_choice = input("Select the word you would like translating: \n")
    if word_choice[0].lower() in vowels:
        pig_latin = word_choice + "way"
    else:
        pig_latin = word_choice[1:] + word_choice[0] + "ay"
    print()
    print("{}".format(pig_latin), file=sys.stderr)

    try_again = input("\n\nPress enter to try again else n to stop.")
    if try_again.lower() == "n":
        sys.exit()
