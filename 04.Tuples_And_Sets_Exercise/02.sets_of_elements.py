firs_length, second_length = [int(x) for x in input().split()]

first_set = {int(input()) for i in range(firs_length)}
second_set = {int(input()) for y in range(second_length)}

res = first_set.intersection(second_set)

[print(el) for el in res]
