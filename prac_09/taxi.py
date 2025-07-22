class Taxi:
    """Represent a Taxi."""
    price_per_km = 1.23

    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        self.odometer = 0
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string representation of the Taxi."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Return the price for the taxi trip, rounded to the nearest 10c."""
        return round(self.price_per_km * self.current_fare_distance, 1)

    def drive(self, distance):
        """Drive the taxi for the given distance and calculate fare."""
        if distance > self.fuel:
            distance = self.fuel
        self.fuel -= distance
        self.odometer += distance
        self.current_fare_distance += distance
        return distance

    def start_fare(self):
        """Start a new fare."""
        self.current_fare_distance = 0
