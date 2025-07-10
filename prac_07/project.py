import datetime


class Project:
    """Represents a project with a name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __repr__(self):
        """String representation for a project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def is_completed(self):
        """Returns True if the project is completed (100%)."""
        return self.completion_percentage == 100

    def __lt__(self, other):
        """Compares projects by priority."""
        return self.priority < other.priority

    @staticmethod
    def from_line(line):
        """Create a Project instance from a data file line."""
        parts = line.strip().split('\t')
        return Project(parts[0], parts[1], parts[2], parts[3], parts[4])

