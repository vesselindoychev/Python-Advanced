import sys
from io import StringIO

test_input = '''1
1
2
3
2
1
2
'''
sys.stdin = StringIO(test_input)


def get_player_choice(player):
    choice = input(f'Player {player}, please choose a column\n')
    return choice


def apply_player_choice(board, player_choice, player):
    row_index = 0
    while row_index < len(board) and \
            board[row_index][player_choice] is None:
        row_index += 1


    board[row_index - 1][player_choice] = player

def check_win_condition():
    pass


def play(board):
    current_player, other_player = 1, 2
    while True:
        player_choice = get_player_choice(current_player)
        print(player_choice)
        # apply_player_choice()
        # check_win_condition()
        print(board)
        current_player, other_player = other_player, current_player


def create_board(rows_count, columns_count):
    return [[None] * columns_count for _ in range(rows_count)]


def print_board(board):
    def get_value(value):
        if value is None:
            return 0
        return value

    for row in board:
        print([get_value(x) for x in row])


board = create_board(6, 7)
apply_player_choice(board, 3, 1)
print_board(board)
