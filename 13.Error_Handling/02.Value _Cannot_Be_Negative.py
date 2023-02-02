from errors import ValueCannotBeNegative

for i in range(5):
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative