from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A special version of Taxi with an additional charge based on fanciness."""

    flagfall = 4.50  # Flat flagfall charge for every fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance with an extra charge based on fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness  # Adjust price per km based on fanciness

    def get_fare(self):
        """Return the total fare including the flagfall and adjusted price."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string including flagfall and the adjusted price per km."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
