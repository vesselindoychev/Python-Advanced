from collections import deque


def check_value(current_material, current_magic_level, gifts):
    current_sum = current_magic_level + current_material

    if current_sum < 100:
        if current_sum % 2 == 0:
            current_sum = (current_material * 2) + (current_magic_level * 3)
        else:
            current_sum *= 2

    if current_sum > 499:
        current_sum //= 2

    if 100 <= current_sum <= 199:
        gifts['Gemstone'] += 1
        return gifts

    if 200 <= current_sum <= 299:
        gifts['Porcelain Sculpture'] += 1
        return gifts

    if 300 <= current_sum <= 399:
        gifts['Gold'] += 1
        return gifts

    if 400 <= current_sum <= 499:
        gifts['Diamond Jewellery'] += 1
        return gifts


def check_pair(first_pair, second_pair, gifts):
    count = 0
    while True:

        for first_pair_name in first_pair:
            if gifts[first_pair_name] > 0:
                count += 1
                continue
        if count == 2:
            print(f'The wedding presents are made!')

            break
        count = 0
        for second_pair_name in second_pair:
            if gifts[second_pair_name] > 0:
                count += 1

        if count == 2:
            print('The wedding presents are made!')
            break
        print(f'Aladdin does not have enough wedding presents.')
        break


def solve(materials, magic_level):
    materials_stack = [int(x) for x in materials]
    magic_level_queue = deque([int(x) for x in magic_level])

    gifts = {
        'Gemstone': 0,
        'Porcelain Sculpture': 0,
        'Gold': 0,
        'Diamond Jewellery': 0
    }

    while materials_stack and magic_level_queue:
        current_material = materials_stack.pop()
        current_magic_level = magic_level_queue.popleft()

        check_value(current_material, current_magic_level, gifts)

    first_pair = ['Gemstone', 'Porcelain Sculpture']
    second_pair = ['Gold', 'Diamond Jewellery']

    check_pair(first_pair, second_pair, gifts)

    return materials_stack, magic_level_queue, gifts


materials = input().split()
magic_level = input().split()

materials_stack, magic_level_queue, gifts = solve(materials, magic_level)

if materials_stack:
    print(f'Materials left: {", ".join(map(str, materials_stack))}')
if magic_level_queue:
    print(f'Magic left: {", ".join(map(str, magic_level_queue))}')

sorted_gifts = sorted(gifts.items(), key=lambda kvp: kvp[0])

for name, quantity in sorted_gifts:
    if quantity > 0:
        print(f'{name}: {quantity}')

"""
from collections import deque

materials = list(map(int, input().split()))
magic_level = deque(list(map(int, input().split())))

gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

while materials and magic_level:
    current_material = materials.pop()
    current_magic_level = magic_level.popleft()

    current_sum = current_material + current_magic_level

    if current_sum < 100:
        if current_sum % 2 == 0:
            current_sum = (current_material * 2) + (current_magic_level * 3)
            # materials.append(current_material * 2)
            # magic_level.appendleft(current_magic_level * 3)
        else:
            current_sum *= 2

    if current_sum > 499:
        current_sum //= 2

    if 100 <= current_sum <= 199:
        gifts['Gemstone'] += 1
        continue

    if 200 <= current_sum <= 299:
        gifts['Porcelain Sculpture'] += 1
        continue

    if 300 <= current_sum <= 399:
        gifts['Gold'] += 1
        continue

    if 400 <= current_sum <= 499:
        gifts['Diamond Jewellery'] += 1
        continue

first_pair = ['Gemstone', 'Porcelain Sculpture']
second_pair = ['Gold', 'Diamond Jewellery']
# if gifts['Gemstone'] > 1 and gifts['Porcelain Sculpture'] > 1 or \
#         gifts['Gold'] > 1 and gifts['Diamond Jewellery'] > 1:

while True:
    done_presents = []
    count = 0
    is_done = False
    for first_pair_name in first_pair:
        if gifts[first_pair_name] > 0:
            count += 1
            continue
    if count == 2:
        is_done = True
        print(f'The wedding presents are made!')
        done_presents.extend(first_pair)
        break
    count = 0
    for second_pair_name in second_pair:
        if gifts[second_pair_name] > 0:
            count += 1

    if count == 2:
        is_done = True
        done_presents.extend(second_pair)
        print('The wedding presents are made!')
        break
    print(f'Aladdin does not have enough wedding presents.')
    break

if materials:
    print(f'Materials left: {", ".join(map(str, materials))}')
if magic_level:
    print(f'Magic left: {", ".join(map(str, magic_level))}')

# if is_done:
#     for i in done_presents:
#         print(f'{i}: {gifts[i]}')


sorted_gifts = sorted(gifts.items(), key=lambda kvp: kvp[0])

for name, quantity in sorted_gifts:
    if quantity > 0:
        print(f'{name}: {quantity}')
"""
