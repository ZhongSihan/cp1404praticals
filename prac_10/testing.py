"""
CP1404/CP5632 Practical
Prac 10 - Testing with assert and doctest
"""

import doctest
from prac_06.car import Car  # 确保路径正确，根据你项目结构修改


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase as a sentence: starting with a capital letter and ending with a period.

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("this is a test")
    'This is a test.'
    """
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].upper() + phrase[1:]


def run_tests():
    """Run the tests on the functions using assert."""
    # Test repeat_string function
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Test Car class
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car_default = Car()
    assert car_default.fuel == 0, "Car default fuel should be 0"

    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Car does not set fuel correctly"


run_tests()
doctest.testmod()
