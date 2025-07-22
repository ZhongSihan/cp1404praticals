from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def print_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def taxi_simulator():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0

    while True:
        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").strip().lower()

        if choice == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            break
        elif choice == 'c':
            print_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                    print(f"You have chosen {current_taxi}")
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid option")
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    trip_cost = current_taxi.drive(distance)
                    total_bill += trip_cost
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                except ValueError:
                    print("Please enter a valid distance")
        else:
            print("Invalid option")

if __name__ == '__main__':
    taxi_simulator()
