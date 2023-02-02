import os

file = open('my_second_file.txt', 'w')

file.write('I just created my second file!')
file.close()

file_path = 'my_second_file.txt'
# try:
#     os.remove('my_second_file.txt')
# except FileNotFoundError:
#     print('File already deleted!')

n = 3

for i in range(n):
    try:
        os.remove(file_path)
    except FileNotFoundError:

        print('File already deleted!')
