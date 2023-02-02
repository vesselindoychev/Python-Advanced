def is_inside(field, r, c):
    return 0 <= r < field and 0 <= c < field


size = int(input())

matrix = []

for _ in range(size):
    row = [x for x in input().split()]
    matrix.append(row)

bunny_row, bunny_col = 0, 0

for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == "B":
            bunny_row, bunny_col = row_index, col_index

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

max_eggs = float('-inf')
best_direction = ''
best_path = []

for direction, step in directions.items():
    current_row, current_col = bunny_row, bunny_col
    eggs = 0
    path = []

    while True:

        current_row, current_col = step(current_row, current_col)

        if not is_inside(size, current_row, current_col):
            break

        if matrix[current_row][current_col] == "X":
            break

        eggs += int(matrix[current_row][current_col])
        path.append([current_row, current_col])
    if eggs > max_eggs:
        max_eggs, best_direction, best_path = eggs, direction, path

print(best_direction)

for step in best_path:
    print(step)

print(max_eggs)
