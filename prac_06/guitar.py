"""CP1404/CP5632 Practical - Guitar calss"""

YEAR = 2022
AGE = 50

class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted information of a Guitar."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age of a guitar."""
        return YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage."""
        return self.get_age() >= AGE