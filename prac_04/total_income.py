"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_number = int(input("How many months? "))

    for month in range(1, month_number + 1):
        income = float(input("Enter income for month {} : ".format(str(month))))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print the report based on the number of month and monthly incomes"""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} \
        Total: ${:10.2f}".format(month + 1, income, total))


main()