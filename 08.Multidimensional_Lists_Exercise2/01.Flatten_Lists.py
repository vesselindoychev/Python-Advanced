line = input().split('|')

result = []
for index in range(len(line) - 1, -1, -1):
    current_numbers = line[index].split()
    result.extend(current_numbers)

print(' '.join(result))
