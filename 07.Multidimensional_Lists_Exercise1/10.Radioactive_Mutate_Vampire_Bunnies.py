rows, cols = [int(x) for x in input().split()]
matrix = []
player_coor = []
move_coor = []
matrix_copy = []
for row in range(rows):
    matrix.append([])
    current_row = input()
    for col in range(cols):
        matrix[row].append(current_row[col])
        if current_row[col] == "P":
            player_coor.append(row)
            player_coor.append(col)



command = [x for x in input()]
win = False
over = False
while True:

    current_command = command.pop(0)
    if current_command == "U" or current_command == "D" or current_command == "L" or current_command == "R":
        if current_command == "U":
            move_coor.clear()
            move_coor.append(player_coor[0] - 1)
            move_coor.append(player_coor[1])
        elif current_command == "D":
            move_coor.clear()
            move_coor.append(player_coor[0] + 1)
            move_coor.append(player_coor[1])
        elif current_command == "L":
            move_coor.clear()
            move_coor.append(player_coor[0])
            move_coor.append(player_coor[1] - 1)
        elif current_command == "R":
            move_coor.clear()
            move_coor.append(player_coor[0])
            move_coor.append(player_coor[1] + 1)

        if move_coor[0] < 0 or move_coor[1] < 0:
            win = True
            matrix[player_coor[0]][player_coor[1]] = "."
        elif move_coor[0] >= rows or move_coor[1] >= cols:
            win = True
            matrix[player_coor[0]][player_coor[1]] = "."

        if not win:
            if matrix[move_coor[0]][move_coor[1]] == ".":
                matrix[player_coor[0]][player_coor[1]], matrix[move_coor[0]][move_coor[1]] = matrix[move_coor[0]][
                                                                                                 move_coor[1]], \
                                                                                             matrix[player_coor[0]][
                                                                                                 player_coor[1]]
                player_coor.clear()
                player_coor = move_coor.copy()
            else:
                over = True
                matrix[player_coor[0]][player_coor[1]] = "."
                player_coor = move_coor.copy()

        matrix_copy = matrix.copy()
        b_coor = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "B":
                    b_coor.append([row, col])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "B":
                    pass
                # /////////////////////////////////////////////
        for el in b_coor:
            row, col = el[0], el[1]
            # /////////////////////////////////////
            if row > 0:
                if matrix[row - 1][col] == "P":
                    over = True
                matrix_copy[row - 1][col] = "B"
            if row < rows - 1:
                if matrix[row + 1][col] == "P":
                    over = True
                matrix_copy[row + 1][col] = "B"
            if col > 0:
                if matrix[row][col - 1] == "P":
                    over = True
                matrix_copy[row][col - 1] = "B"
            if col < cols - 1:
                if matrix[row][col + 1] == "P":
                    over = True
                matrix_copy[row][col + 1] = "B"

        matrix.clear()
        matrix = matrix_copy.copy()
        matrix_copy.clear()

    if over:
        for row in range(rows):
            for col in range(cols):
                print(matrix[row][col], end="")
            print()
        player_coor = [str(x) for x in player_coor]
        print(f"dead: {' '.join(player_coor)}")
        break
    elif win:
        for row in range(rows):
            for col in range(cols):
                print(matrix[row][col], end="")
            print()
        player_coor = [str(x) for x in player_coor]
        print(f"won: {' '.join(player_coor)}")
        break
