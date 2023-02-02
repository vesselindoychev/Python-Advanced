n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

primary_diagonal = []
secondary_diagonal = []
below_primary_diagonal = []
'''
   --- Primary Diagonal ---

for row_index in range(len(matrix)):
    for column_index in range(len(matrix[row_index])):
        if column_index == row_index:
            primary_diagonal.append(matrix[row_index][column_index])

print(sum(primary_diagonal))
'''

'''
   --- Secondary Diagonal ---

for row_index in range(len(matrix)):
    for column_index in range(len(matrix[row_index])):
        if column_index == len(matrix) - row_index - 1:
            secondary_diagonal.append(matrix[row_index][column_index])

print(secondary_diagonal)
'''

'''
   --- Below Primary Diagonal ---
for row_index in range(len(matrix)):
    for column_index in range(row_index):
        below_primary_diagonal.append(matrix[row_index][column_index])

print(below_primary_diagonal)
'''

above_secondary_diagonal = []

'''
   --- Above Secondary Diagonal ---

for row_index in range(len(matrix)):
    for column_index in range(len(matrix[row_index]) - 1 - row_index):
        above_secondary_diagonal.append(matrix[row_index][column_index])

print(above_secondary_diagonal)
'''