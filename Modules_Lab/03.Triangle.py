n = int(input())

for row in range(1, n + 1):
    for column in range(1, row + 1):
        print(column, end=' ')

    print()

for row in range(n - 1, 0, -1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print()
