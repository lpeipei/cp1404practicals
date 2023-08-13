FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and print details about Wimbledon champions and countries."""
    records = get_records(FILENAME)
    count, countries = process_records(records)
    display_results(count, countries)


def process_records(records):
    count = {}
    countries = set()
    for item in records:
        countries.add(item[INDEX_COUNTRY])
        try:
            count[item[INDEX_CHAMPION]] += 1
        except KeyError:
            count[item[INDEX_CHAMPION]] = 1
    return count, countries


def display_results(count, countries):
    print("Wimbledon Champions:")
    for name, count in count.items():
        print(f"{name} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
