class Musician:
    def __init__(self, name):
        self.name = name
        self.instruments = []

    def add_instrument(self, instrument):
        """Add an instrument to the musician's list."""
        self.instruments.append(instrument)

    def __str__(self):
        """Return a string representation of the musician and their instruments."""
        instruments_str = ', '.join(str(instrument) for instrument in self.instruments)
        if instruments_str:
            return f"{self.name} ({instruments_str})"
        else:
            return f"{self.name} (needs an instrument!)"

class Instrument:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price

    def __str__(self):
        """Return a string representation of the instrument."""
        return f"{self.name} ({self.year}) : ${self.price:.2f}"

class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add_musician(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band and its musicians."""
        musicians_str = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_str})"
