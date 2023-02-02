n, m = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

sum_of_columns = [0] * m

# for row_index in range(n):
#     row = matrix[row_index]
#     for column_index in range(m):
#         sum_of_columns[column_index] += row[column_index]
#
# [print(x) for x in sum_of_columns]

# for row in range(n):
#     for column in range(m):
#         value = matrix[row][column]
#         sum_of_columns[column] += value

for column in range(m):
    for row in range(n):
        value = matrix[row][column]
        sum_of_columns[column] += value

[print(x) for x in sum_of_columns]