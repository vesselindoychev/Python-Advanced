n = int(input())

parking_lot = set()
for _ in range(n):
    command, car_number = input().split(", ")

    if command == "IN":
        parking_lot.add(car_number)
    elif command == "OUT":
        if car_number in parking_lot:
            parking_lot.remove(car_number)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print(f"Parking Lot is Empty")