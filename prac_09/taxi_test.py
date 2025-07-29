from prac_09.taxi import Taxi

def main():
    """Test code for the Taxi class using class variable price_per_km."""
    # Create a new Taxi instance (no need to pass price_per_km now)
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km
    my_taxi.drive(40)

    # Print taxi details and current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Start a new fare and drive 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Print taxi details and current fare again
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == '__main__':
    main()
