n, m = [int(x) for x in input().split()]

matrix = []

for _ in range(n):
    row = [x for x in input().split()]
    matrix.append(row)

counter = 0

for row_index in range(n - 1):
    for column_index in range(m - 1):
        if matrix[row_index][column_index] == matrix[row_index][column_index + 1] == \
                matrix[row_index + 1][column_index] == \
                matrix[row_index + 1][column_index + 1]:

            counter += 1

print(counter)
