"""
SOLUTION WITH FUNCTIONS
 ---->    ----->    ----->
"""

def get_coordinates():
    str_coordinates = input()
    coordinates = str_coordinates[1: -1].split(', ')
    return [int(x) for x in coordinates]


def is_outside(row_index, col_index, SIZE):
    if row_index < 0 or row_index >= SIZE \
            or col_index < 0 or col_index >= SIZE:
        return True
    return False


def get_sum_of_4(row_index, col_index, board):
    return int(board[0][col_index]) + int(board[-1][col_index]) + \
           int(board[row_index][0]) + int(board[row_index][-1])


def get_value(row_index, col_index, board, SIZE):
    if is_outside(row_index, col_index, SIZE):
        return 0

    target = board[row_index][col_index]

    if target.isdigit():
        return int(target)

    if target == 'D':
        return get_sum_of_4(row_index, col_index, board) * 2

    if target == 'T':
        return get_sum_of_4(row_index, col_index, board) * 3

    if target == 'B':
        return 501

def is_won(total_points):
    if total_points <= 0:
        return True
    return False


def dart_game(board, player_names, SIZE):
    current_player = player_names[0], 501, 0
    other_player = player_names[1], 501, 0

    while True:
        name, total_points, throws = current_player
        row_index, col_index = get_coordinates()

        points = get_value(row_index, col_index, board, SIZE)
        total_points -= points
        throws += 1

        if is_won(total_points):
            break

        current_player = name, total_points, throws
        current_player, other_player = other_player, current_player

    print(f"{name} won the game with {throws} throws!")


player_names = input().split(', ')

SIZE = 7
board = []

for _ in range(SIZE):
    row = [x for x in input().split()]
    board.append(row)

dart_game(board, player_names, SIZE)
"""
      - - - -    SOLUTION WITHOUT FUNCTIONS    - - - -

def is_outside(row_index, col_index, SIZE):
    if row_index < 0 or row_index >= SIZE or col_index < 0 or col_index >= SIZE:
        return True
    return False


def get_sum_of_4(matrix, row_index, col_index):
    return int(matrix[row_index][0]) + int(matrix[row_index][-1]) + \
           int(matrix[0][col_index]) + int(matrix[-1][col_index])


def is_won(total_points):
    if total_points <= 0:
        return True
    return False


player_names = input().split(', ')

current_player = player_names[0], 501, 0
other_player = player_names[1], 501, 0

SIZE = 7

matrix = []

for _ in range(SIZE):
    row = [x for x in input().split()]
    matrix.append(row)

while True:
    name, total_points, throws = current_player

    coordinates = input()
    (row_index), col_index = coordinates[1: -1].split(', ')
    row_index, col_index = int(row_index), int(col_index)
    if is_outside(row_index, col_index, SIZE):
        throws += 1
        current_player = name, total_points, throws
        current_player, other_player = other_player, current_player
        continue

    target = matrix[row_index][col_index]

    if target == 'D':
        points = get_sum_of_4(matrix, row_index, col_index) * 2
        total_points -= points
        throws += 1

    elif target == 'T':
        points = get_sum_of_4(matrix, row_index, col_index) * 3
        total_points -= points
        throws += 1

    elif target == 'B':
        points = 501
        total_points -= points
        throws += 1

    if is_won(total_points):
        break

    current_player = name, total_points, throws
    current_player, other_player = other_player, current_player

print(f'{name} won the game with {throws} throws!')
"""
