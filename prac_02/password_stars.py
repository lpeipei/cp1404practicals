MINIMUM_LENGTH = 5

password = input("Enter your password: ")

while len(password) < MINIMUM_LENGTH:

    print("Password doesn't meet a minimum length")

    password = input("Enter your password: ")

print(len(password) * "*")


