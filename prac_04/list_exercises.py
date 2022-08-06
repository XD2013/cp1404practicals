"""
CP1404/CP5632 Practical
Basic list operation and woefully inadequate security checker
"""

numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

loop = 0
while loop < 5:
    number = int(input("Number: "))
    numbers.append(number)
    loop += 1

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The mallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

username = input("Enter your username: ")

if username in usernames:
    print("Access granted")
else:
    print("Access denied")

