from math import log


def calculate_log(x, base):
    if base == 'natural':
        return f'{log(x):.2f}'

    return f'{log(x, int(base)):.2f}'


print(calculate_log(10, 'natural'))
print(calculate_log(10, 10))
