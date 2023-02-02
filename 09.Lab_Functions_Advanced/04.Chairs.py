def generate_combination(values, count, index, comb):
    if len(comb) == count:
        print(', '.join(comb))
        return

    for i in range(index, len(values)):
        comb.append(values[i])
        generate_combination(values, count, i + 1, comb)
        comb.pop()


generate_combination(input().split(), int(input()), 0, [])
