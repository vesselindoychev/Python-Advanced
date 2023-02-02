n = int(input())

matrix = []
for _ in range(n):
    row = [x for x in input()]
    matrix.append(row)

symbol = input()

is_found = False
matrix_indices = []
for row_index in range(n):
    if is_found:
        break
    for column_index in range(len(matrix[row_index])):
        value = matrix[row_index][column_index]

        if symbol == value:
            matrix_indices.append(row_index)
            matrix_indices.append(column_index)
            is_found = True
            break

if not is_found:
    print(f"{symbol} does not occur in the matrix")
else:

    row_index, column_index = [x for x in matrix_indices]
    print(f"({row_index}, {column_index})")