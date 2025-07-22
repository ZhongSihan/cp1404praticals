from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A Silver Service Taxi that includes a flagfall and fancy pricing."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with fancy pricing."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness  # Adjust the price per km based on fanciness

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the fare for the trip including the flagfall."""
        return super().get_fare() + self.flagfall
