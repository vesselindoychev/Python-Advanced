def is_outside(r, c, SIZE):
    if r < 0 or r >= SIZE \
            or c < 0 or c >= SIZE:
        return True
    return False


def solve(SIZE, matrix):
    has_won = False
    n = 3
    current_sum = 0

    gifts = {
        'Football': 0,
        'Teddy Bear': 0,
        'Lego Construction Set': 0
    }
    for _ in range(n):
        coordinates_str = input()
        coordinates = coordinates_str[1: -1].split(', ')
        row_index, col_index = [int(x) for x in coordinates]

        if is_outside(row_index, col_index, SIZE):
            continue
        target = matrix[row_index][col_index]

        if target.isdigit():
            continue

        if target == 'B':

            for c in range(SIZE):
                if c == col_index + 1:
                    break
                for r in range(SIZE):
                    if c == col_index:
                        if matrix[r][c] != 'B':
                            current_sum += int(matrix[r][c])
            matrix[row_index][col_index] = '0'

    if 100 <= current_sum <= 199:
        gifts['Football'] += 1
        has_won = True

    if 200 <= current_sum <= 299:
        gifts['Teddy Bear'] += 1
        has_won = True

    if current_sum >= 300:
        gifts['Lego Construction Set'] += 1
        has_won = True

    return has_won, gifts, current_sum


SIZE = 6

matrix = []

for _ in range(SIZE):
    row = [x for x in input().split()]
    matrix.append(row)

has_won, gifts, current_sum = solve(SIZE, matrix)

if has_won:
    for k, v in gifts.items():
        if v > 0:
            print(f'Good job! You scored {current_sum} points, and you\'ve won {k}.')
else:
    print(f'Sorry! You need {100 - current_sum} points more to win a prize.')
