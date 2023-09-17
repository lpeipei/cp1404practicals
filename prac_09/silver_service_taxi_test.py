from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    fancy_taxi = SilverServiceTaxi("test taxi", 200, 2)

    fancy_taxi.drive(18)

    fare = fancy_taxi.get_fare()
    print(f"Fare: ${fare:.2f}")

    print(fancy_taxi)


main()
