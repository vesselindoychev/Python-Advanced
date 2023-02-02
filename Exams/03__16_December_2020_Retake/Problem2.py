def is_valid_command(command):
    if command == 'up' or command == 'down' \
            or command == 'left' or command == 'right':
        return True
    return False


def get_next_step(command, r, c):
    if command == 'up':
        return r - 1, c
    if command == 'down':
        return r + 1, c
    if command == 'left':
        return r, c - 1
    if command == 'right':
        return r, c + 1


def is_outside(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


text = list(input())

size = int(input())

matrix = []

for _ in range(size):
    row = [x for x in input()]
    matrix.append(row)

player_row, player_col = 0, 0

for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == 'P':
            player_row, player_col = row_index, col_index

n = int(input())

current_row, current_col = 0, 0
for _ in range(n):
    command = input()

    if not is_valid_command(command):
        continue

    current_row, current_col = get_next_step(command, player_row, player_col)

    if is_outside(current_row, current_col, size):
        if text:
            text.pop()
        continue

    target = matrix[current_row][current_col]

    if target != '-':
        text += target
        target = '-'

    matrix[player_row][player_col] = '-'
    matrix[current_row][current_col] = 'P'
    player_row, player_col = current_row, current_col

print(''.join(text))
for row in matrix:
    print(''.join(row))