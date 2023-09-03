from guitar import Guitar
FILE = 'guitars.csv'


def load_guitars(file_name):
    guitars = []
    try:
        file_read = open(file_name, 'r')
        for line in file_read:
            name, year, cost = line.strip().split(',')
            year = int(year)
            cost = float(cost)
            guitars.append(Guitar(name, year, cost))
        file_read.close()
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    return guitars


def save_guitars(file_name, guitars):
    file_in = open(file_name, 'w')
    for guitar in guitars:
        file_in.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}")
    file_in.close()


def main():
    guitars = load_guitars(FILE)

    print("List of Guitars:")
    for i, guitar in enumerate(guitars, start=1):
        print(f"{i}. {guitar}")

    guitars.sort()

    print("List of Guitars:")
    for i, guitar in enumerate(guitars, start=1):
        print(f"{i}. {guitar}")

    name = input("Enter guitar name: ")
    while name:
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)

        name = input("Enter guitar name: ")

    save_guitars(FILE, guitars)


main()
