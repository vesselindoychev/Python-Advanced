n, m = [int(x) for x in input().split()]

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

biggest_sum = 0
best_row = 0
best_col = 0
for row_index in range(n - 2):
    for column_index in range(m - 2):
        res = matrix[row_index][column_index] + matrix[row_index][column_index + 1] + matrix[row_index][
            column_index + 2] + \
              matrix[row_index + 1][column_index] + matrix[row_index + 1][column_index + 1] + matrix[row_index + 1][
                  column_index + 2] + \
              matrix[row_index + 2][column_index] + matrix[row_index + 2][column_index + 1] + matrix[row_index + 2][
                  column_index + 2]

        if res > biggest_sum:
            biggest_sum, best_row, best_col = res, row_index, column_index

print(f"Sum = {biggest_sum}")
print(matrix[best_row][best_col], matrix[best_row][best_col + 1], matrix[best_row][best_col + 2])
print(matrix[best_row + 1][best_col], matrix[best_row + 1][best_col + 1], matrix[best_row + 1][best_col + 2])
print(matrix[best_row + 2][best_col], matrix[best_row + 2][best_col + 1], matrix[best_row + 2][best_col + 2])
