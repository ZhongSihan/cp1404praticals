import csv

def read_data(filename):
    data = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data.append(row)
    return data

def process_champions(data):
    champion_count = {}
    for row in data:
        champion = row[2].strip()
        if champion in champion_count:
            champion_count[champion] += 1
        else:
            champion_count[champion] = 1
    return champion_count

def process_countries(data):
    countries = set()
    for row in data:
        country = row[3].strip()
        countries.add(country)
    return countries

def display_data(champion_count, countries):
    print("Wimbledon Champions: ")
    for champion, count in sorted(champion_count.items()):
        print(f"{champion} {count}")

    print("\nThese countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


def main():
    filename = 'wimbledon.csv'
    data = read_data(filename)
    champion_count = process_champions(data)
    countries = process_countries(data)
    display_data(champion_count, countries)


main()
