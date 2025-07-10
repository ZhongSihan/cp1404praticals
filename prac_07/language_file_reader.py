"""
Language file reader
Now includes pointer arithmetic field
"""

from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []

    with open('languages.csv', 'r') as in_file:
        in_file.readline()  # Skip header

        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            typing = parts[1]
            reflection = parts[2] == "Yes"
            year = int(parts[3])
            pointer_arithmetic = parts[4] == "Yes"

            language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
            languages.append(language)

    for language in languages:
        print(language)


main()
