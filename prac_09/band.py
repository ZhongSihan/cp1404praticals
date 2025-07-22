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
