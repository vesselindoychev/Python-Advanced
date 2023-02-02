n, m = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

total_sum = 0

for row_index in range(n):
    row = matrix[row_index]
    for column_index in range(m):
        total_sum += row[column_index]

print(total_sum)
print(matrix)