"""
CP1404/CP5632 Practical
Allows a user to enter a color's name and get the hexadecimal code
GitHub: https://github.com/XD2013/cp1404practicals
"""

COLOUR = {'#0048ba': "Absolute Zero", '#b0bf1a': "Acid Green", '#f0f8ff': "AliceBlue", '#e32636': "Alizarin crimson",
                '#e52b50': "Amaranth", '#ffbf00': "Amber", '#9966cc': "Amethyst", '#faebd7': "AntiqueWhite",
          '#ffefdb': "AntiqueWhite1", '#eedfcc': "AntiqueWhite2"}
print(COLOUR)

colour_code = input("Enter a colour code: ")
while colour_code != "":
    print("{0} is {1}".format(colour_code, COLOUR.get(colour_code)))
    colour_code = input("Enter short state: ")
