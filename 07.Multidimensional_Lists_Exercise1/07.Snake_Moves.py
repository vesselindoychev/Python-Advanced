n, m = [int(x) for x in input().split()]
word = input()

matrix = []
word_idx = 0

for row in range(n):
    matrix.append([None] * m)
    for column in range(m):
        if row % 2 == 0:
            matrix[row][column] = word[word_idx]
        else:
            matrix[row][m - 1 - column] = word[word_idx]
        word_idx = (word_idx + 1) % len(word)

[print(''.join(text)) for text in matrix]