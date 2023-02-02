n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)


primary_diagonal = []


for row_index in range(len(matrix)):
    for column_index in range(len(matrix[row_index])):
        if column_index == row_index:
            primary_diagonal.append(matrix[row_index][column_index])

print(sum(primary_diagonal))