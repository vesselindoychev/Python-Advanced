from collections import deque
people = input().split()
n = int(input())
people_queue = deque(people)

while people_queue:
    for i in range(n - 1):
        people_queue.append(people_queue.popleft())
    print(f"Removed {people_queue.popleft()}")

    if len(people_queue) == 1:
        print(f"Last is {people_queue.popleft()}")