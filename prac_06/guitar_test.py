"""CP1404/CP5632 Practical - Guitar test"""

from prac_06.guitar import Guitar

YEAR = 2022

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 1256.9)

print("{} get_age() - Expected {}. Got {}".format(guitar1.name, 100, guitar1.get_age()))
print("{} get_age() - Expected {}. Got {}".format(guitar2.name, 9, guitar2.get_age()))
print("{} is_vintage() - Expected {}. Got {}".format(guitar1.name, True, guitar1.is_vintage()))
print("{} is_vintage() - Expected {}. Got {}".format(guitar2.name, False, guitar2.is_vintage()))