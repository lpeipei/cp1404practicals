from prac_09.unreliable_car import UnreliableCar


def main():
    my_car = UnreliableCar("Unreliable Car", 100, 50)

    for i in range(1, 10):
        distance = 10
        distance_driven = my_car.drive(distance)
        if distance_driven > 0:
            print(f"Drive {i}: {distance_driven} km")
        else:
            print(f"Drive {i}: Car broke down")

    print(my_car)


main()
