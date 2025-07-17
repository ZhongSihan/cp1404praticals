import csv
from guitar import Guitar


def read_guitars_from_file(filename):
    """Read guitars from the given CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def write_guitars_to_file(guitars, filename):
    """Write a list of guitars to the CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def display_guitars(guitars):
    """Display the list of guitars."""
    for guitar in guitars:
        print(guitar)


def get_new_guitar():
    """Prompt the user to enter a new guitar's details."""
    name = input("Enter the guitar name: ")
    year = int(input("Enter the year of the guitar: "))
    cost = float(input("Enter the cost of the guitar: "))
    return Guitar(name, year, cost)


def main():
    """Main program function."""
    filename = 'guitars.csv'
    guitars = read_guitars_from_file(filename)

    print("Guitars from the file:")
    display_guitars(guitars)

    # Sort guitars by year (oldest to newest)
    guitars.sort()

    print("\nSorted guitars by year:")
    display_guitars(guitars)

    # Get new guitar from user and add to list
    new_guitar = get_new_guitar()
    guitars.append(new_guitar)

    # Save the updated list back to the file
    write_guitars_to_file(guitars, filename)

    print("\nUpdated list of guitars (including new one):")
    display_guitars(guitars)


if __name__ == "__main__":
    main()
