"""CP1404/CP5632 Practical - Guitar test"""

from prac_06.guitar import Guitar

guitars = []

print("My guitars!")

guitar_name = input("Name: ")
while guitar_name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar_info = Guitar(guitar_name, year, cost)
    guitars.append(guitar_info)
    print(f"{guitar_info} added.")
    guitar_name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

guitars.sort()
print("These are my guitars:")
for i, guitar in enumerate(guitars):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = " (vintage)"
    print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


