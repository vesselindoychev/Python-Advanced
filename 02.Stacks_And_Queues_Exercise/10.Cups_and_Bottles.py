from collections import deque

cups_capacity = deque(list(map(int, input().split())))
bottles_capacity = list(map(int, input().split()))

wasted_water = 0
while len(cups_capacity) > 0  and len(bottles_capacity) > 0:
    current_cup = cups_capacity[0]
    current_bottle = bottles_capacity[-1]

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
        cups_capacity.popleft()
        bottles_capacity.pop()

    else:

        cups_capacity[0] = current_cup - current_bottle

        bottles_capacity.pop()

if bottles_capacity:
    print(f'Bottles: {" ".join(list(map(str, bottles_capacity)))}')
    print(f'Wasted litters of water: {wasted_water}')

else:
    print(f'Cups: {" ".join(list(map(str, cups_capacity)))}')
    print(f'Wasted litters of water: {wasted_water}')