def is_outside(r, c, size):
    if r < 0 or r >= size or c < 0 or c >= size:
        return True
    return False


def check_neighbours(matrix, r, c, directions):
    for direction in directions:
        current_row, current_col = r + direction[0], c + direction[1]
        if not is_outside(current_row, current_col, size):
            if matrix[current_row][current_col] != '*':
                matrix[current_row][current_col] += 1

size = int(input())
bombs_count = int(input())

matrix = []
bomb_coordinates = []

directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
    [-1, -1],
    [-1, 1],
    [1, -1],
    [1, 1]
]

for row_index in range(size):
    matrix.append([])
    for col_index in range(size):
        matrix[row_index].append(0)

for i in range(bombs_count):
    coordinates_str = input()
    coordinates = coordinates_str[1: -1].split(', ')
    bomb_row, bomb_col = [int(x) for x in coordinates]

    if not is_outside(bomb_row, bomb_col, size):
        bomb_coordinates.append([bomb_row, bomb_col])
        matrix[bomb_row][bomb_col] = '*'


for bomb in bomb_coordinates:
    check_neighbours(matrix, bomb[0], bomb[1], directions)

for row in matrix:
    print(' '.join(map(str, row)))