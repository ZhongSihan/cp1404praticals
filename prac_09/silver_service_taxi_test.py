from prac_09.silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    """Test SilverServiceTaxi functionality."""
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.start_fare()

    # Drive 18 km and calculate fare
    taxi.drive(18)
    fare = taxi.get_fare()

    print(f"Fare for 18 km trip with SilverServiceTaxi (fanciness=2): ${fare:.2f}")

    # Test assert for the fare calculation
    expected_fare = (18 * 1.23 * 2) + 4.50  # 1.23 is base price per km, multiplied by fanciness
    assert fare == expected_fare, f"Expected ${expected_fare}, but got ${fare}"


# Run the test
test_silver_service_taxi()
