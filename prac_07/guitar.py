class Guitar:
    """Represent information about a guitar."""

    def __init__(self, name, year, cost):
        """Construct a Guitar from the given values."""
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        """Return a string representation of the guitar."""
        return f"{self.name}, {self.year}, ${self.cost}"

    def __lt__(self, other):
        """Compare guitars by year for sorting."""
        return self.year < other.year
