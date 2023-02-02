def is_valid(r, c, n, m):
    if 0 <= r < n and 0 <= c < m:
        return True
    return False


n, m = [int(x) for x in input().split()]

matrix = []

for _ in range(n):
    row = [x for x in input().split()]
    matrix.append(row)

while True:
    line = input()

    if line == "END":
        break

    tokens = line.split()
    command = tokens[0]

    if len(tokens) != 5:
        print("Invalid input!")
        continue

    if command != "swap":
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in tokens[1:]]

    if not is_valid(row1, col1, n, m) or not is_valid(row2, col2, n, m):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        res = []
        for x in row:
            res.append(str(x))
        print(' '.join(res))