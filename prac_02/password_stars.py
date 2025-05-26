MIN_LENGTH = 5

password = input("Enter a password: ")
while len(password) < MIN_LENGTH:
    print("Password too short")
    password = input("Enter a password: ")

print('*' * len(password))





MIN_LENGTH = 5

def main():
    password = get_password()
    print_stars(password)

def get_password():
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password too short. Must be at least {MIN_LENGTH} characters.")
        password = input("Enter a password: ")
    return password

def print_stars(password, character='*'):
    print(character * len(password))

main()

