n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

primary = 0
secondary = 0


for row_index in range(n):
    primary += matrix[row_index][row_index]
    secondary += matrix[row_index][n - row_index - 1]

print(abs(primary - secondary))