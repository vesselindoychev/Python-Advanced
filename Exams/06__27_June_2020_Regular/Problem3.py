def list_manipulator(numbers, first_parameter, second_parameter, *args):
    if first_parameter == 'add' and second_parameter == 'beginning':
        return list(args) + numbers

    if first_parameter == 'add' and second_parameter == 'end':
        return numbers + list(args)
    if first_parameter == 'remove' and second_parameter == 'beginning':
        if args:
            return numbers[args[0]:]
        return numbers[1:]
    if first_parameter == 'remove' and second_parameter == 'end':
        if not args:
            return numbers[:-1]
        return numbers[0: -args[0]]


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
