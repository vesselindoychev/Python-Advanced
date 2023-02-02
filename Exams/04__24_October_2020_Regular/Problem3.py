from collections import deque


def best_list_pureness(numbers, rotations):
    max_pureness = 0
    max_index = 0

    numbers = deque(numbers)
    for rotation_index in range(rotations + 1):
        pureness_sum = 0
        for index in range(len(numbers)):
            pureness_sum += numbers[index] * index

        if pureness_sum > max_pureness:
            max_pureness = pureness_sum
            max_index = rotation_index

        numbers.appendleft(numbers.pop())

    return f'Best pureness {max_pureness} after {max_index} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
