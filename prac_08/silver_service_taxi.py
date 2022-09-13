from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a formatted string of SilverServiceTaxi"""
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Get the fare after plus the flagfall"""
        return self.flagfall + super().get_fare()
