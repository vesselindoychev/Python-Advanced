print('- - - -  FILE1 - - --')
print()
try:
    file = open('text.txt', 'r')
    print('File found')
except FileNotFoundError:
    print('File not FOUND or path is INCORRECT')
print()


print('- - - - -- FILE 2 -- - - -- -')
file2 = open('reading_file.txt', 'r')
# print(file2.readline(2))
# print(file2.read(2))
# print(file2.readlines(1))
# print(file2.read())

for line in file2:
    print(line.strip())