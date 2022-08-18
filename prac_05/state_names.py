"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
GitHub: https://github.com/XD2013/cp1404practicals
"""

# Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {'QLD': "Queensland", 'NSW': "New South Wales", 'NT': "Northern Territory", 'WA': "Western Australia",
                'ACT': "Australian Capital Territory", 'VIC': "Victoria", 'TAS': "Tasmania"}
STATE_CODE = []
print(CODE_TO_NAME)

state_code = input("Enter short state: ") .upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
        STATE_CODE.append(state_code)
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ") .upper()
for i in STATE_CODE:
    state_name = CODE_TO_NAME[i]
    print(f"{i:<3} is {state_name}")