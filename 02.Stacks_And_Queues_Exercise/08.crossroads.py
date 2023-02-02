from collections import deque

green_light_duration = int(input())
window_duration = int(input())

cars = deque()
passed_cars = 0

is_crashed = False

while True:
    command = input()

    if command == "END":
        break
    elif command == "green":
        if cars:
            current_car = cars.popleft()
            seconds_left = green_light_duration - len(current_car)

            while seconds_left > 0:
                passed_cars += 1

                if cars:
                    current_car = cars.popleft()
                    seconds_left -= len(current_car)
                else:
                    break

            if seconds_left == 0:
                passed_cars += 1

            if window_duration >= abs(seconds_left):
                if seconds_left < 0:
                    passed_cars += 1

            else:
                index = window_duration + seconds_left
                print(f"A crash happened!")
                print(f"{current_car} was hit at {current_car[index]}.")
                is_crashed = True
                break

    else:
        cars.append(command)


if not is_crashed:
    print(f"Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")