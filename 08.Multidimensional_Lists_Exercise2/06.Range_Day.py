def is_inside(r, c, size):
    if size > r >= 0 and size > c >= 0:
        return True
    return False


def get_next_position(direction, r, c, step):
    if direction == 'up':
        return r - step, c
    if direction == 'down':
        return r + step, c
    if direction == 'left':
        return r, c - step
    if direction == 'right':
        return r, c + step


size = 5

matrix = []

for _ in range(size):
    row = [x for x in input().split()]
    matrix.append(row)

player_row, player_col = 0, 0
targets_count = 0

for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == 'A':
            player_row, player_col = row_index, col_index

        if matrix[row_index][col_index] == 'x':
            targets_count += 1

n = int(input())

shot_targets = 0
path = []
for _ in range(n):
    line = input().split()
    command, direction = line[0], line[1]
    current_row, current_col = player_row, player_col

    if command == 'move':
        steps = int(line[-1])

        current_row, current_col = get_next_position(direction, player_row, player_col, steps)

        if is_inside(current_row, current_col, size) and matrix[current_row][current_col] != '.':
            continue

        if not is_inside(current_row, current_col, size):
            continue

        matrix[player_row][player_col] = '.'
        matrix[current_row][current_col] = 'A'
        player_row, player_col = current_row, current_col

    else:
        next_row, next_col = player_row, player_col
        while True:
            bullet_row, bullet_col = get_next_position(direction, next_row, next_col, step=1)

            if not is_inside(bullet_row, bullet_col, size):
                break

            if is_inside(bullet_row, bullet_col, size) and matrix[bullet_row][bullet_col] == 'x':
                shot_targets += 1
                path.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = '.'

                break

            next_row, next_col = bullet_row, bullet_col

        if shot_targets == targets_count:
            break

if shot_targets == targets_count:
    print(f'Training completed! All {shot_targets} targets hit.')
else:
    print(f"Training not completed! {targets_count - shot_targets} targets left.")

for p in path:
    print(p)
