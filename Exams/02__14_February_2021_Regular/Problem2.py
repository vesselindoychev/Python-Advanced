def is_valid_command(command):
    if command == 'up' or command == 'down' \
            or command == 'left' or command == 'right':
        return True
    return False


def is_outside(r, c, size):
    if r < 0 or r >= size or c < 0 or c >= size:
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


size = int(input())

matrix = []

for _ in range(size):
    row = [x for x in input().split()]
    matrix.append(row)

player_row, player_col = 0, 0
for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == 'P':
            player_row, player_col = row_index, col_index

current_row, current_col = 0, 0
coins = 0
path = []
while True:
    command = input()

    if not is_valid_command(command):
        continue

    current_row, current_col = get_next_step(command, player_row, player_col)
    # target = matrix[current_row][current_col]

    if is_outside(current_row, current_col, size):
        coins //= 2
        print(f"Game over! You've collected {coins} coins.")
        break

    if matrix[current_row][current_col] == 'X':
        coins //= 2
        print(f"Game over! You've collected {coins} coins.")
        break

    coins += int(matrix[current_row][current_col])
    path.append([current_row, current_col])

    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

    player_row, player_col = current_row, current_col

print('Your path:')
for p in path:
    print(p)
