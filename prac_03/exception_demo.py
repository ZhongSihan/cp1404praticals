"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   - A ValueError occurs if the user enters something that can't be converted to an integer,
     such as letters, symbols, or a decimal (e.g., "abc", "4.5").

2. When will a ZeroDivisionError occur?
   - A ZeroDivisionError occurs if the user enters 0 as the denominator,
     because dividing by zero is not allowed in mathematics.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, you can check if the denominator is zero before doing the division
     and prompt the user again until it's not zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
