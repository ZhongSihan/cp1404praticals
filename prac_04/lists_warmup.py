numbers = [3, 1, 4, 1, 5, 9, 2]

#Predicted answers
# numbers[0]        → 3
# numbers[-1]       → 2
# numbers[3]        → 1
# numbers[:-1]      → [3, 1, 4, 1, 5, 9]
# numbers[3:4]      → [1]
# 5 in numbers      → True
# 7 in numbers      → False
# "3" in numbers    → False (string "3" is not same as int 3)
# numbers + [6, 5, 3] → [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change the first element to "ten"
numbers[0] = "ten"

# Change the last element to 1
numbers[-1] = 1

# Print all elements except the first two
print(numbers[2:])

# Check if 9 is in the list
print(9 in numbers)
