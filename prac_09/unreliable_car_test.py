from prac_09.unreliable_car import UnreliableCar

def main():
    """Test the UnreliableCar class."""
    car = UnreliableCar("Old Bomb", 100, 30)

    total_driven = 0
    attempts = 100
    for i in range(attempts):
        distance = car.drive(1)
        total_driven += distance

    print(f"Tried to drive {attempts} km with 30% reliability, actually drove: {total_driven} km")

if __name__ == '__main__':
    main()
