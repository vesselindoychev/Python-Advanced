def is_outside(current_row, current_col, size):
    if current_row < 0 or current_row >= size or \
            current_col < 0 or current_col >= size:
        return True
    return False


def find_snake_indices(size, matrix):
    for row_index in range(size):
        for col_index in range(size):
            if matrix[row_index][col_index] == 'S':
                return row_index, col_index


def find_burrow_indices(size, matrix):
    temp = []
    for row_index in range(size):
        for col_index in range(size):
            if matrix[row_index][col_index] == 'B':
                temp.append([row_index, col_index])

    return temp


def get_next_position(direction, snake_row, snake_col):
    if direction == 'up':
        return snake_row - 1, snake_col
    if direction == 'down':
        return snake_row + 1, snake_col
    if direction == 'left':
        return snake_row, snake_col - 1
    if direction == 'right':
        return snake_row, snake_col + 1


def has_eaten_food(food_quantity):
    if food_quantity == 10:
        return True
    return False


def solve(size, matrix):
    snake_row, snake_col = find_snake_indices(size, matrix)
    burrows = find_burrow_indices(size, matrix)
    food_quantity = 0

    while True:
        direction = input()

        current_row, current_col = get_next_position(direction, snake_row, snake_col)

        if is_outside(current_row, current_col, size):
            matrix[snake_row][snake_col] = '.'
            break

        cell_value = matrix[current_row][current_col]

        if cell_value == '*':
            food_quantity += 1
            if has_eaten_food(food_quantity):
                matrix[current_row][current_col] = 'S'
                matrix[snake_row][snake_col] = '.'
                break

        if cell_value == 'B':
            if (current_row, current_col) == (burrows[0][0], burrows[0][1]):
                matrix[current_row][current_col] = '.'
                current_row, current_col = burrows[1]
            else:
                matrix[current_row][current_col] = '.'
                current_row, current_col = burrows[0]

        matrix[snake_row][snake_col] = '.'
        matrix[current_row][current_col] = 'S'
        snake_row, snake_col = current_row, current_col

    if has_eaten_food(food_quantity):
        print('You won! You fed the snake.')
    else:
        print('Game over!')

    return food_quantity, matrix


size = int(input())

matrix = []

for _ in range(size):
    row = [x for x in input()]
    matrix.append(row)

food_quantity, matrix = solve(size, matrix)

print(f'Food eaten: {food_quantity}')

for row in matrix:
    print(''.join(row))


"""def is_outside(r, c, size):
    if r < 0 or r >= size or c < 0 or c >= size:
        return True
    return False


def get_next_step(direction, r, c):
    if direction == 'up':
        return r - 1, c
    if direction == 'down':
        return r + 1, c
    if direction == 'left':
        return r, c - 1
    if direction == 'right':
        return r, c + 1


size = int(input())

territory = []

for _ in range(size):
    row = [x for x in input()]
    territory.append(row)

snake_row, snake_col = 0, 0
burrows = []
for row_index in range(size):
    for col_index in range(size):
        if territory[row_index][col_index] == 'S':
            snake_row, snake_col = row_index, col_index
        elif territory[row_index][col_index] == 'B':
            burrows.append((row_index, col_index))

eaten_food = 0
while True:
    is_food_eaten = False
    is_out = False
    direction = input()

    current_row, current_col = get_next_step(direction, snake_row, snake_col)

    if is_outside(current_row, current_col, size):
        territory[snake_row][snake_col] = '.'
        is_out = True

        break

    cell_value = territory[current_row][current_col]

    if cell_value == 'B':
        if (current_row, current_col) == burrows[0]:
            territory[current_row][current_col] = '.'
            (current_row, current_col) = burrows[1]
        else:
            territory[current_row][current_col] = '.'
            (current_row, current_col) = burrows[0]

    elif cell_value == '*':
        eaten_food += 1

        if eaten_food == 10:
            is_food_eaten = True

    territory[snake_row][snake_col] = '.'
    territory[current_row][current_col] = 'S'
    snake_row, snake_col = current_row, current_col

    if is_food_eaten:
        print(f'You won! You fed the snake.')
        break

if is_out or not is_food_eaten:
    print('Game over!')
print(f'Food eaten: {eaten_food}')

for row in territory:
    print("".join(row))
"""