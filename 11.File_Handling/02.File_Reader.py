file = open('numbers.txt', 'a')
file2 = open('numbers.txt', 'r')
total_sum = 0

for line in file2:
    total_sum += int(line)

print(total_sum)