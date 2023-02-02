n = int(input())

even = set()
odd = set()

set_result = ()
for index in range(1, n + 1):
    name = input()
    res = 0
    for ch in name:
        res += ord(ch)

    res //= index

    if res % 2 == 0:
        even.add(res)
    else:
        odd.add(res)


if sum(odd) == sum(even):
    set_result = odd.union(even)

elif sum(odd) > sum(even):
    set_result = odd.difference(even)

elif sum(odd) < sum(even):
    set_result = odd.symmetric_difference(even)

set_result = [str(x) for x in set_result]
print(', '.join(set_result))