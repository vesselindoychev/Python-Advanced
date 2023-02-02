def is_knight_placed(board, r, c):
    board_size = len(board)
    if r < 0 or r >= board_size or c < 0 or c >= board_size:
        return False
    return board[r][c] == 'K'


def count_affected_knights(board, r, c):
    result = 0
    if is_knight_placed(board, r + 2, c + 1):
        result += 1
    if is_knight_placed(board, r + 2, c - 1):
        result += 1
    if is_knight_placed(board, r - 2, c - 1):
        result += 1
    if is_knight_placed(board, r - 2, c + 1):
        result += 1
    if is_knight_placed(board, r - 1, c - 2):
        result += 1
    if is_knight_placed(board, r - 1, c + 2):
        result += 1
    if is_knight_placed(board, r + 1, c - 2):
        result += 1
    if is_knight_placed(board, r + 1, c + 2):
        result += 1
    return result


size = int(input())

matrix = []

for _ in range(size):
    row = [x for x in input()]
    matrix.append(row)

removed_knights = 0
while True:
    max_count, knight_row, knight_col = 0, 0, 0
    for row_index in range(size):
        for col_index in range(size):
            if matrix[row_index][col_index] == '0':
                continue
            count = count_affected_knights(matrix, row_index, col_index)

            if count > max_count:
                max_count = count
                knight_row, knight_col = row_index, col_index

    if max_count == 0:
        break
    matrix[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)
