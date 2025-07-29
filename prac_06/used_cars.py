"""CP1404/CP5632 Practical - Client code to use the Car class."""

from prac_06.car import Car


def main():
    """Demo test code to show how to use Car class."""
    my_car = Car("MyCar", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # --- New code for the tasks ---
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Limo has fuel: {limo.fuel}")  # Should print 120
    distance_driven = limo.drive(115)
    print(f"Limo drove {distance_driven}km")
    print(limo)  # Should show name, fuel, and odometer via __str__

