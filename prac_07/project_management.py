import os
from project import Project


def load_projects(filename):
    """Load projects from a given filename."""
    projects = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            file.readline()  # Skip the header line
            for line in file:
                projects.append(Project.from_line(line))
    return projects


def save_projects(projects, filename):
    """Save a list of projects to a given filename."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_completed()], key=lambda p: p.priority)
    completed = sorted([p for p in projects if p.is_completed()], key=lambda p: p.priority)

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects, date_string):
    """Filter and display projects that start after a given date."""
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > filter_date]
    filtered_projects.sort(key=lambda p: p.start_date)

    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """Prompt user to add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Allow the user to update a project's completion and priority."""
    for idx, project in enumerate(projects):
        print(f"{idx} {project}")
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]

    new_percentage = input(f"New Percentage ({project.completion_percentage}): ")
    new_priority = input(f"New Priority ({project.priority}): ")

    if new_percentage:
        project.completion_percentage = int(new_percentage)
    if new_priority:
        project.priority = int(new_priority)


def main():
    projects = load_projects('projects.txt')

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save to: ")
            save_projects(projects, filename)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? (yes/no): ").lower()
            if save_choice == 'yes':
                save_projects(projects, 'projects.txt')
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == '__main__':
    main()

