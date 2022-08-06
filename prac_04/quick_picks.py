"""
CP1404/CP5632 Practical
"Quick Pick" Lottery Ticket Generator
"""

import random

PER_LINE_NUMBER = 6
MAX_NUMBER = 45
MIN_NUMBER = 1

quick_pick = int(input("How many quick picks? "))

for l in range(quick_pick):
    numbers = []
    for n in range(PER_LINE_NUMBER):
        number = random.randint(MIN_NUMBER, MAX_NUMBER + 1)
        while number in numbers:
            number = random.randint(MIN_NUMBER, MAX_NUMBER + 1)
        numbers.append(number)
    numbers.sort()
    print(numbers)

