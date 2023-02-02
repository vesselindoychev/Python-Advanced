def is_outside(r, c, size):
    if r < 0 or r >= size or c < 0 or c >= size:
        return True
    return False


def is_valid_position(direction, r, c):
    if direction == 'up':
        return r - 1, c
    if direction == 'down':
        return r + 1, c
    if direction == 'left':
        return r, c - 1
    if direction == 'right':
        return r, c + 1


is_collected = False
is_game_over = False
size = int(input())
commands = input().split()
matrix = []

for _ in range(size):
    row = [x for x in input().split()]
    matrix.append(row)

coal_count = 0
player_row, player_col = 0, 0

for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == 's':
            player_row, player_col = row_index, col_index
        if matrix[row_index][col_index] == 'c':
            coal_count += 1

collected_coal = 0
current_row, current_col = 0, 0
for command in commands:
    matrix[player_row][player_col] = '*'

    player_row, player_col = is_valid_position(command, player_row, player_col)
    if is_outside(player_row, player_col, size):
        player_row, player_col = current_row, current_col
        matrix[player_row][player_col] = 's'
        continue
    if matrix[player_row][player_col] == 'e':
        is_game_over = True
        print(f'Game over! ({player_row}, {player_col})')
        matrix[player_row][player_col] = 's'
        break

    if matrix[player_row][player_col] == 'c':
        collected_coal += 1
        if collected_coal == coal_count:
            is_collected = True
            print(f'You collected all coal! ({player_row}, {player_col})')
            break

        matrix[player_row][player_col] = 's'

    else:
        matrix[player_row][player_col] = 's'

    current_row, current_col = player_row, player_col

if not is_game_over and not is_collected:
    print(f'{coal_count - collected_coal} pieces of coal left. ({player_row}, {player_col})')
