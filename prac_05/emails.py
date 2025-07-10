def main():
    email_to_name = {}
    while True:
        email = input("Email: ").strip()
        if email == "":
            break
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm not in ("", "y"):
            name = input("Name: ").strip()
        email_to_name[email] = name

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    name_part = email.split('@')[0]
    name_words = name_part.replace('.', ' ').split()
    return ' '.join(word.title() for word in name_words)


main()
