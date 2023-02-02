from collections import deque

water_quantity = int(input())

people_queue = deque()

while True:
    command = input()

    if command == "Start":
        break
    people_queue.append(command)

while True:
    command = input()

    if command == "End":
        break

    elif command.startswith("refill"):
        tokens = command.split()
        water_to_add = int(tokens[1])
        water_quantity += water_to_add

    else:
        name = people_queue.popleft()
        water_wanted = int(command)

        if water_wanted <= water_quantity:
            water_quantity -= water_wanted
            print(f"{name} got water")
        else:
            print(f"{name} must wait")

print(f"{water_quantity} liters left")