"""
CP1404/CP5632 Practical
program that stores users' emails and names in a dictionary
GitHub: https://github.com/XD2013/cp1404practicals
"""

email_name = {}

email = input("Email: ")
while email != "":
    name1 = email.split('@')[0]
    name2 = name1.split('.')
    name = " ".join(name2).title()
    check_name = input("Is your name {}? (Y/n) ".format(name)) .upper()
    if check_name != "Y" and check_name != "":
        name = input("Name: ") .title()
    email_name[email] = name
    email = input("Email: ")

for email, name in email_name.items():
    print("{} ({})".format(name, email))