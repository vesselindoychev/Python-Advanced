n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

bomb_coordinates = input().split()

for bomb in bomb_coordinates:
    bomb_row, bomb_col = bomb.split(',')
    bomb_row = int(bomb_row)
    bomb_col = int(bomb_col)

    if matrix[bomb_row][bomb_col] > 0:
        value = matrix[bomb_row][bomb_col]
        matrix[bomb_row][bomb_col] = "x"

        targets = [
            [bomb_row - 1, bomb_col - 1],
            [bomb_row - 1, bomb_col],
            [bomb_row - 1, bomb_col + 1],
            [bomb_row, bomb_col - 1],
            [bomb_row, bomb_col],
            [bomb_row, bomb_col + 1],
            [bomb_row + 1, bomb_col - 1],
            [bomb_row + 1, bomb_col],
            [bomb_row + 1, bomb_col + 1]
        ]

        for target in targets:
            row1, col1 = target[0], target[1]

            if row1 >= 0 and col1 >= 0:
                if row1 < n and col1 < n:
                    if not matrix[row1][col1] == "x":
                        if matrix[row1][col1] > 0:
                            matrix[row1][col1] -= value

alive_cells = 0
total_sum = 0

for row_index in range(n):
    for column_index in range(n):
        if matrix[row_index][column_index] == "x":
            matrix[row_index][column_index] = 0

        if matrix[row_index][column_index] > 0:
            total_sum += matrix[row_index][column_index]
            alive_cells += 1

print(f"Alive cells: {alive_cells}")
print(f"Sum: {total_sum}")

for row in range(n):
    for column in range(n):
        print(matrix[row][column], end=' ')

    print()
