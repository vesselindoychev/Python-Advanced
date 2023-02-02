numbers_dictionary = {}

line = input()

while line != 'Search':
    numbers_as_string = line
    try:
        number = int(input())
        numbers_dictionary[numbers_as_string] = number
    except ValueError:
        print('The variable must be an integer')
    line = input()

line = input()

while line != 'Remove':
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print('Number does not exist in dictionary')
    line = input()

line = input()

while line != 'End':
    key_to_be_deleted = line
    try:
        del numbers_dictionary[key_to_be_deleted]
    except KeyError:
        print('Number does not exist in dictionary')
    line = input()
print(numbers_dictionary)