n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

primary = []
secondary = []
for row_index in range(n):
    primary.append(matrix[row_index][row_index])
    secondary.append(matrix[row_index][n - row_index - 1])

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")

