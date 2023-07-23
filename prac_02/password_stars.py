"""
CP1404
Password_stars.py
Password Check with Functions
"""
MINIMUM_LENGTH = 5


def get_password():
    """Get the entered password and verify it"""
    password = input("Enter your password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password doesn't meet the minimum length")
        password = input("Enter your password: ")
    return password


def print_asterisks(password):
    """Print asterisks"""
    print(len(password) * "*")


def main():
    """main function"""
    password = get_password()
    print_asterisks(password)


main()



