from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi fare calculations."""
    taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(taxi)  # Should include price per km and flagfall

    taxi.drive(18)
    fare = taxi.get_fare()
    print(f"Fare for 18km trip: ${fare:.2f}")

    # Assert expected fare: (1.23 * 4) * 18 + 4.50 = 48.78
    assert round(fare, 2) == 48.78, f"Expected $48.78, got ${fare:.2f}"


if __name__ == '__main__':
    main()
