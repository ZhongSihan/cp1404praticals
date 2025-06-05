import random

# Line 1: random integer between 5 and 20 (inclusive)
print(random.randint(5, 20))
# Possible values: 5 to 20 inclusive
# Smallest: 5, Largest: 20

# Line 2: random odd number between 3 and 9 (10 excluded), step of 2
print(random.randrange(3, 10, 2))
# Possible values: 3, 5, 7, 9
# Smallest: 3, Largest: 9
# Could line 2 have produced a 4? No, because step=2 starting at 3 gives only odd numbers.

# Line 3: random float between 2.5 and 5.5 (inclusive of 2.5, exclusive of 5.5)
print(random.uniform(2.5, 5.5))
# Possible range: 2.5 <= x <= 5.5
# Smallest: 2.5, Largest: 5.5

# Produce a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")
