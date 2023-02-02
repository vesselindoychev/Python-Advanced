def is_outside(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


size = 8

matrix = []

for _ in range(size):
    row = [x for x in input().split()]
    matrix.append(row)

get_next_position = {
    'up': lambda r, c: (r - 1, c),
    'diagonally_up_left': lambda r, c: (r - 1, c - 1),
    'diagonally_up_right': lambda r, c: (r - 1, c + 1),
    'down': lambda r, c: (r + 1, c),
    'diagonally_down_left': lambda r, c: (r + 1, c - 1),
    'diagonally_down_right': lambda r, c: (r + 1, c + 1),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)

}

path = []
queen_row, queen_col = 0, 0
for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == 'Q':
            queen_row, queen_col = row_index, col_index

            for k, step in get_next_position.items():
                current_row, current_col = queen_row, queen_col
                while True:
                    current_row, current_col = step(current_row, current_col)

                    if is_outside(current_row, current_col, size):
                        break

                    if matrix[current_row][current_col] == 'Q':
                        break
                    if matrix[current_row][current_col] == 'K':
                        path.append([queen_row, queen_col])

                        break

if not path:
    print('The king is safe!')
else:
    for p in path:
        print(p)
