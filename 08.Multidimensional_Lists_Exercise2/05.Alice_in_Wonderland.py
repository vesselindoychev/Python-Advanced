def is_outside(r, c, field):
    if r < 0 or r >= field or c < 0 or c >= field:
        return True
    return False


# def get_next_step(direction, r, c):
#     if direction == "up":
#         return r - 1, c
#     if direction == "down":
#         return r + 1, c
#     if direction == "left":
#         return r, c - 1
#     if direction == "right":
#         return r, c + 1


size = int(input())

matrix = []

for _ in range(size):
    row = [x for x in input().split()]
    matrix.append(row)

alice_row, alice_col = 0, 0

for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == "A":
            alice_row, alice_col = row_index, col_index

matrix[alice_row][alice_col] = '*'

tea_bags = 0

directions = {
    'up': lambda alice_row, alice_col: (alice_row - 1, alice_col),
    'down': lambda alice_row, alice_col: (alice_row + 1, alice_col),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

while True:
    command = input()

    for direction, step in directions.items():
        if direction == command:
            (alice_row, alice_col) = step(alice_row, alice_col)
            break
    # alice_row, alice_col = get_next_step(command, alice_row, alice_col)

    if is_outside(alice_row, alice_col, size):
        break
    cell_value = matrix[alice_row][alice_col]
    matrix[alice_row][alice_col] = "*"
    if cell_value == "R":
        break

    if cell_value.isdigit():
        tea_bags += int(cell_value)

        if tea_bags >= 10:
            break

if tea_bags >= 10:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(' '.join(row))
