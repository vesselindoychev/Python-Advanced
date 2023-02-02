# try:
#     file = open('text.txt', 'r')
#     print('File found')
# except FileNotFoundError:
#     print('File not found')
#
#

file = open('text.txt', 'a')

try:
    file2 = open('text.txt', 'r')
    print(file2.readlines())
    print('File found')
except FileNotFoundError:
    print('File not found')