def even_odd(*args):
    result = []
    parity = 0 if args[-1] == 'even' else 1
    for i in range(len(args)):
        if i == len(args) - 1:
            return result

        if args[i] % 2 == parity:
            result.append(args[i])


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
