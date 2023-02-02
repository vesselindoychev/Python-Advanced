n = int(input())

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

flattened_matrix = [number for row in matrix for number in row]
print(flattened_matrix)

