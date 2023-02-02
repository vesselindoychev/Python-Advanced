# - - - - With Functions - - - - -


from collections import deque


def solve(firework_effects, explosive_power):
    queue = deque(list(map(int, firework_effects)))
    stack = list(map(int, explosive_power))

    def are_fireworks_enough(fireworks):
        if fireworks['palm'] >= 3 and fireworks['willow'] >= 3 \
                and fireworks['crossette'] >= 3:
            return True
        return False

    fireworks = {
        'palm': 0,
        'willow': 0,
        'crossette': 0
    }

    while queue and stack and not are_fireworks_enough(fireworks):
        current_firework = queue.popleft()
        current_power = stack.pop()

        if current_firework <= 0:
            stack.append(current_power)
            continue
        if current_power <= 0:
            queue.appendleft(current_firework)
            continue

        current_sum = current_firework + current_power

        if current_sum % 3 == 0 and current_sum % 5 == 0:
            fireworks['crossette'] += 1
            continue

        if current_sum % 3 == 0:
            fireworks['palm'] += 1
            continue

        if current_sum % 5 == 0:
            fireworks['willow'] += 1
            continue

        current_firework -= 1
        queue.append(current_firework)
        stack.append(current_power)

    return fireworks, queue, stack


firework_effect = input().split(', ')
explosive_power = input().split(', ')

(fireworks, remaining_firework_effect, remaining_explosive_power) = solve(firework_effect, explosive_power)


def are_fireworks_done(fireworks):
    if fireworks['palm'] >= 3 and fireworks['willow'] >= 3 and fireworks['crossette'] >= 3:
        return True
    return False


if are_fireworks_done(fireworks):
    print(f'Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")

if remaining_firework_effect:
    print(f'Firework Effects left: {", ".join(list(map(str, remaining_firework_effect)))}')

if remaining_explosive_power:
    print(f'Explosive Power left: {", ".join(list(map(str, remaining_explosive_power)))}')

print(f"Palm Fireworks: {fireworks['palm']}")
print(f"Willow Fireworks: {fireworks['willow']}")
print(f"Crossette Fireworks: {fireworks['crossette']}")

"""
- - - - Without Functions - - - - 

from collections import deque

firework_effects = deque(list(map(int, input().split(', '))))
explosive_power = list(map(int, input().split(', ')))

def are_fireworks_enough(fireworks):
    if fireworks['palm'] >= 3 and fireworks['willow'] >= 3 and fireworks['crossette'] >= 3:
        return True
    return False

fireworks = {
    'palm': 0,
    'willow': 0,
    'crossette': 0,
}

while firework_effects and explosive_power and not are_fireworks_enough(fireworks):
    current_firework_punch = firework_effects.popleft()
    current_explosive_power = explosive_power.pop()

    if current_firework_punch <= 0:
        explosive_power.append(current_explosive_power)
        continue

    if current_explosive_power <= 0:
        firework_effects.appendleft(current_firework_punch)
        continue

    current_sum = current_explosive_power + current_firework_punch

    if current_sum % 3 == 0 and current_sum % 5 == 0:
        fireworks['crossette'] += 1
        continue

    if current_sum % 3 == 0:
        fireworks['palm'] += 1
        continue
    if current_sum % 5 == 0:
        fireworks['willow'] += 1
        continue

    current_firework_punch -= 1
    firework_effects.append(current_firework_punch)
    explosive_power.append(current_explosive_power)

if are_fireworks_enough(fireworks):
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

print(f'Palm Fireworks: {fireworks["palm"]}')
print(f'Willow Fireworks: {fireworks["willow"]}')
print(f'Crossette Fireworks: {fireworks["crossette"]}')
"""
