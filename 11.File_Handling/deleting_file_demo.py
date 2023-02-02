import os


path_file = 'deleting_file_demo.txt'
if os.path.exists(path_file):
    os.remove('deleting_file_demo.txt')
