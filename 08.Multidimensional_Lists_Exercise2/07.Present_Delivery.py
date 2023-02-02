def is_inside(r, c, size):
    if size > r >= 0 and size > c >= 0:
        return True
    return False


def get_next_position(direction, r, c, step):
    if direction == 'up':
        return r - step, c
    if direction == 'down':
        return r + step, c
    if direction == 'left':
        return r, c - step
    if direction == 'right':
        return r, c + step


presents_count = int(input())
size = int(input())

matrix = []
for _ in range(size):
    row = [x for x in input().split()]
    matrix.append(row)

santa_row, santa_col = 0, 0
good_kids_count = 0
good_kids_given_presents = 0

for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == 'S':
            santa_row, santa_col = row_index, col_index

        if matrix[row_index][col_index] == 'V':
            good_kids_count += 1

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
}

is_run_out_of_presents = False
while True:
    command = input()

    if command == 'Christmas morning':
        break

    current_row, current_col = get_next_position(command, santa_row, santa_col, step=1)

    if not is_inside(current_row, current_col, size):
        continue

    if matrix[current_row][current_col] == 'V':
        presents_count -= 1
        good_kids_given_presents += 1

    if matrix[current_row][current_col] == 'C':
        for direction, step in directions.items():
            next_row, next_col = step(current_row, current_col)
            if not is_inside(next_row, next_col, size):
                continue
            if matrix[next_row][next_col] == 'V':
                good_kids_given_presents += 1
                presents_count -= 1
            if matrix[next_row][next_col] == 'X':
                presents_count -= 1

            matrix[next_row][next_col] = '-'

            if presents_count <= 0:
                break
    matrix[santa_row][santa_col] = '-'
    matrix[current_row][current_col] = 'S'
    santa_row, santa_col = current_row, current_col

    if presents_count <= 0:
        is_run_out_of_presents = True
        break

if is_run_out_of_presents and good_kids_count - good_kids_given_presents > 0:
    print('Santa ran out of presents!')

for row in matrix:
    print(' '.join(row))

if good_kids_given_presents == good_kids_count:
    print(f'Good job, Santa! {good_kids_count} happy nice kid/s.')
else:
    print(f'No presents for {good_kids_count - good_kids_given_presents} nice kid/s.')

# def is_outside(size, r, c):
#     if r < 0 or r >= size or c < 0 or c >= size:
#         return True
#     return False
#
#
# def get_next_position(position, r, c, step=1):
#     if position == 'up':
#         return r - step, c
#     if position == 'down':
#         return r + step, c
#     if position == 'left':
#         return r, c - step
#     if position == 'right':
#         return r, c + step
#
#
# def get_houses_in_range(size, r, c):
#     houses = []
#
#     if is_outside(r - 1, c, size):
#         houses.append([r - 1, c])
#
#     if is_outside(r + 1, c, size):
#         houses.append([r + 1, c])
#
#     if is_outside(r, c - 1, size):
#         houses.append([r, c - 1])
#
#     if is_outside(r, c + 1, size):
#         houses.append([r, c + 1])
#
#     return houses
#
#
# presents = int(input())
# size = int(input())
#
# matrix = []
#
# for _ in range(size):
#     row = [x for x in input().split()]
#     matrix.append(row)
#
# santa_row, santa_col = 0, 0
# nice_kids_count = 0
# initial_good_kids = 0
#
# for row_index in range(size):
#     for col_index in range(size):
#         if matrix[row_index][col_index] == 'S':
#             santa_row, santa_col = row_index, col_index
#         elif matrix[row_index][col_index] == 'V':
#             initial_good_kids += 1
#
# nice_kids_count = initial_good_kids
#
# while True:
#     direction = input()
#
#     if direction == 'Christmas morning':
#         break
#
#     next_santa_row, next_santa_col = get_next_position(direction, santa_row, santa_col, step=1)
#
#     if matrix[next_santa_row][next_santa_col] == 'V':
#         presents -= 1
#         nice_kids_count -= 1
#
#     elif matrix[next_santa_row][next_santa_col] == 'C':
#         houses_in_range = get_houses_in_range(size, next_santa_row, next_santa_col)
#
#         for row, col in houses_in_range:
#             if matrix[row][col] == 'V':
#                 presents -= 1
#                 nice_kids_count -= 1
#
#             if matrix[row][col] == 'X':
#                 presents -= 1
#
#             matrix[row][col] = '-'
#
#             if presents == 0:
#                 break
#
#     matrix[santa_row][santa_col] = '-'
#     matrix[next_santa_row][next_santa_col] = 'S'
#     santa_row, santa_col = next_santa_row, next_santa_col
#
#     if presents == 0:
#         break
#
# if presents == 0 and nice_kids_count > 0:
#     print(f"Santa ran out of presents!")
#
# for row in matrix:
#     print(' '.join(row))
#
# if nice_kids_count == 0:
#     print(f"Good job, Santa! {initial_good_kids} happy nice kid/s.")
# else:
#     print(f"No presents for {nice_kids_count} nice kid/s.")
