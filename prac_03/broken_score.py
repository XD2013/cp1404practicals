"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# Fix this!

import random

def main():
    score = float(input("Enter score: "))
    get_result(score)
    random_score = random.randint(0, 101)
    get_result(random_score)

def get_result(score):
    if score < 0 or score > 100:
        return print("Invalid score")
    else:
        if score >= 90:
            return print("Excellent")
        elif score >= 50:
            return print("Passable")
        elif score < 50:
            return print("Bad")

main()