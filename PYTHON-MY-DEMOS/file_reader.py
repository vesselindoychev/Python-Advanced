file = open('numbers.txt', 'r')

sum_of_line_integers = 0
for line in file:
    if line == '':
        continue
    sum_of_line_integers += int(line)

print(sum_of_line_integers)