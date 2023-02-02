def is_valid(r, c):
    if size > r >= 0 and size > c >= 0:
        return True
    return False
size = int(input())

matrix = []
for _ in range(size):
    row = [int(x) for x in input().split()]
    matrix.append(row)


while True:
    line = input()

    if line == "END":
        break
    line_args = line.split()
    command = line_args[0]
    row, col, value = [int(x) for x in line_args[1:]]

    if command == "Add":
        if is_valid(row, col):
            matrix[row][col] += value
        else:
            print('Invalid coordinates')

    elif command == "Subtract":
        if is_valid(row, col):
            matrix[row][col] -= value

        else:
            print('Invalid coordinates')
    else:
        print('Invalid coordinates')


for row in matrix:
    [print(str(x), end=' ') for x in row]
    print()