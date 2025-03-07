"""A program that returns a poor man's bar chart."""

from collections import defaultdict
import sys
import pprint

poor_mans_barchart = defaultdict(list)

while True:
    print("Welcome to the Poor Man's Bar Chart. \n")
    input_text = input("Type a sentence of your choice: \n")

    for letter in input_text:
        letter = letter.lower()
        poor_mans_barchart[letter].append(letter)

    pprint.pprint(poor_mans_barchart)

    try_again = input("\n\nPress enter key to go again else n to stop.")
    if try_again.lower() == "n":
        sys.exit()
