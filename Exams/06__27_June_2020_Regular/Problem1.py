from collections import deque


def bomb_materials(bomb_effects, bomb_casings):
    bomb_effects_queue = deque([int(x) for x in bomb_effects])
    bomb_casings_stack = [int(x) for x in bomb_casings]

    bombs = {
        40: 'Datura Bombs',
        60: 'Cherry Bombs',
        120: 'Smoke Decoy Bombs',
    }

    current_bombs = {
        'Datura Bombs': 0,
        'Cherry Bombs': 0,
        'Smoke Decoy Bombs': 0
    }

    def are_bombs_filled(current_bombs):
        if current_bombs['Datura Bombs'] >= 3 and current_bombs['Cherry Bombs'] >= 3 \
                and current_bombs['Smoke Decoy Bombs'] >= 3:
            return True
        return False

    while bomb_effects_queue and bomb_casings_stack and not are_bombs_filled(current_bombs):
        current_bomb_effect = bomb_effects_queue.popleft()
        current_bomb_casing = bomb_casings_stack.pop()

        current_sum = current_bomb_effect + current_bomb_casing

        if current_sum in bombs:
            bomb_name = bombs[current_sum]
            current_bombs[bomb_name] += 1
            continue

        bomb_effects_queue.appendleft(current_bomb_effect)
        bomb_casings_stack.append(current_bomb_casing - 5)

    return current_bombs, bomb_effects_queue, bomb_casings_stack


bomb_effects = input().split(', ')
bomb_casing = input().split(', ')

current_bombs, bomb_effects_queue, bomb_casing_stack = bomb_materials(bomb_effects, bomb_casing)


def are_bombs_filled(current_bombs):
    if current_bombs['Datura Bombs'] >= 3 and current_bombs['Cherry Bombs'] >= 3 \
            and current_bombs['Smoke Decoy Bombs'] >= 3:
        return True
    return False


if are_bombs_filled(current_bombs):
    print(f'Bene! You have successfully filled the bomb pouch!')
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if bomb_effects_queue:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects_queue))}")
else:
    print(f"Bomb Effects: empty")

if bomb_casing_stack:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casing_stack))}")
else:
    print(f"Bomb Casings: empty")

sorted_bombs = sorted(current_bombs.items(), key=lambda kvp: kvp[0])

for name, quantity in sorted_bombs:
    print(f'{name}: {quantity}')

"""
from collections import deque

bomb_effects = deque(list(map(int, input().split(', '))))
bomb_casings = [int(x) for x in input().split(', ')]

bombs = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs',

}

current_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}


def are_bombs_created(current_bombs):
    if current_bombs['Datura Bombs'] >= 3 and current_bombs['Cherry Bombs'] >= 3 \
            and current_bombs['Smoke Decoy Bombs'] >= 3:
        return True
    return False


while bomb_effects and bomb_casings and not are_bombs_created(current_bombs):
    current_bomb = bomb_effects.popleft()
    current_bomb_casing = bomb_casings.pop()

    current_sum = current_bomb + current_bomb_casing

    if current_sum in bombs:
        bomb_name = bombs[current_sum]
        current_bombs[bomb_name] += 1

    else:
        bomb_effects.appendleft(current_bomb)
        bomb_casings.append(current_bomb_casing - 5)


if are_bombs_created(current_bombs):
    print(f'Bene! You have successfully filled the bomb pouch!')
else:
    print(f"You don't have enough materials to fill the bomb pouch.")


if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print(f'Bomb Effects: empty')


if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print(f'Bomb Casings: empty')


sorted_bombs = sorted(current_bombs.items(), key=lambda kvp: kvp[0])

for bomb_name, bomb_quantity in sorted_bombs:
    print(f'{bomb_name}: {bomb_quantity}')
"""
