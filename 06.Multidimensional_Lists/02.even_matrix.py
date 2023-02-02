n = int(input())

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)


even_matrix = []
for row in matrix:
    even_row = [x for x in row if x % 2 == 0]
    even_matrix.append(even_row)
print(even_matrix)