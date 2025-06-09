"""CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Main function to load and display subject data."""
    subject_data = load_data()
    display_subject_details(subject_data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students.
    Returns:
        list of [subject_code, lecturer_name, student_count]
    """
    subject_list = []

    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove newline
            parts = line.split(',')  # Split by comma
            parts[2] = int(parts[2])  # Convert student count to int
            subject_list.append(parts)  # Add the cleaned-up list to the data

    return subject_list


def display_subject_details(data):
    """Display subject details from a nested list."""
    for subject_code, lecturer, student_count in data:
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")


main()
