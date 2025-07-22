"""
CP1404 Practical
Programming Language class with pointer arithmetic field
"""

class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"First appeared in {self.year}, Pointer Arithmetic={self.pointer_arithmetic}")

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return user-friendly string for the language."""
        return self.__repr__()


def run_tests():
    """Run simple tests on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    c = ProgrammingLanguage("C", "Static", False, 1972, True)
    print(ruby)
    print(c)

    languages = [ruby, c]
    print("Languages with pointer arithmetic:")
    for language in languages:
        if language.pointer_arithmetic:
            print(language.name)


if __name__ == "__main__":
    run_tests()
