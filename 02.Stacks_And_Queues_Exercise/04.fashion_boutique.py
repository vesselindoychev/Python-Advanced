clothes = list(map(int, input().split()))
rack_capacity = int(input())

current_rack = rack_capacity
new_rack = 1
while clothes:
    if clothes[-1] <= current_rack:
        current_rack -= clothes[-1]
        clothes.pop()
    else:
        new_rack += 1
        current_rack = rack_capacity


print(new_rack)