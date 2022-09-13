from prac_08.car import Car
import random

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, but depending on the random number and reliability."""
        random_number = random.randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven

