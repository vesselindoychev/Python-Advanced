file2 = open('demo_write_files.py', 'a')

file = open('python.txt', 'w')

file.write('This is the write command.\n')
file.write('It allows us to write in a particular file\n')
file.close()

file = open('python.txt', 'a')
file.write('\nThis is the "a" mode\n')
file.write('And it allows me to write at an existing file\n')
file.close()

file = open('python.txt', 'a')
lines1 = ['This', 'is', '.writelines', 'command']
lines = ['\nWrite', 'in', 'file']
file.writelines(lines1)
file.writelines(lines)
file.close()