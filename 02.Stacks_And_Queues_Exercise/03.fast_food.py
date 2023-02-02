from collections import deque

total_food = int(input())
orders = list(map(int, input().split()))

queue = deque(orders)

print(max(orders))

for index in range(len(orders)):
    if orders[index] <= total_food:
        total_food -= orders[index]
        queue.popleft()
    else:
        break

queue = list(queue)
if not queue:
    print(f"Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, queue))}")
