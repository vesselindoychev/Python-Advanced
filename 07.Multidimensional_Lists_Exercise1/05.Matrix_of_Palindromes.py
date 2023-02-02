n, m = [int(x) for x in input().split()]

for row_index in range(n):
    for column_index in range(m):
        print(f"{chr(97 + row_index)}{chr(97 + column_index + row_index)}{chr(97 + row_index)}", end=' ')

    print()