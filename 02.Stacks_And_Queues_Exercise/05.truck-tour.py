from collections import deque

queue = deque()

pumps_count = int(input())

for i in range(pumps_count):
    pump = list(map(int, input().split()))
    queue.append(pump)


for index in range(pumps_count):
    car_fuel = 0
    is_completed = True
    for petrol, distance in queue:
        car_fuel += petrol

        if distance > car_fuel:
            is_completed = False
            break
        car_fuel -= distance
    if is_completed:
        print(index)
        break
    queue.append(queue.popleft())

