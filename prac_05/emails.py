def main():
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name.title()}? (Y/n) ").lower()

        if confirmation.lower() != "y" and confirmation != "":
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ").strip()

    for email, name in email_to_name.items():
        print(f"{name.title()} ({email})")


def extract_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    username = " ".join(parts).title()
    return username


main()
