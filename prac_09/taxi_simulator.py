from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def choose_taxi(taxis):
    """Prompt user to choose a taxi."""
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        choice = int(input("Choose taxi: "))
        if choice < 0 or choice >= len(taxis):
            print("Invalid taxi choice")
            return None
        return taxis[choice]
    except ValueError:
        print("Invalid input")
        return None

def drive_taxi(taxi):
    """Prompt user to drive a taxi."""
    if taxi is None:
        print("You need to choose a taxi before you can drive")
        return
    try:
        distance = float(input("Drive how far? "))
        distance_driven = taxi.drive(distance)
        print(f"Your {taxi.name} trip cost you ${taxi.get_fare():.2f}")
        print(f"Bill to date: ${sum(taxi.get_fare() for taxi in taxis):.2f}")
    except ValueError:
        print("Invalid input")

def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()
        if choice == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
            print(f"Bill to date: ${total_bill:.2f}")
        elif choice == 'd':
            drive_taxi(current_taxi)
        else:
            print("Invalid option")

if __name__ == '__main__':
    main()
