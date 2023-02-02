from collections import deque

price_of_each_bullet = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(list(map(int, input().split())))
intelligence_value = int(input())

bullets_count = len(bullets)
index = 0
is_out_of_ammo = False
while True:

    if bullets and locks:
        current_bullet = bullets.pop()
        current_lock = locks.popleft()
        index += 1

        if current_bullet > current_lock:
            print('Ping!')
            locks.appendleft(current_lock)

        if current_bullet <= current_lock:
            print('Bang!')

        if bullets:
            if index == gun_barrel_size:
                print('Reloading!')
                index = 0
    else:
        if not bullets and not locks:
            break
        if not bullets:
            is_out_of_ammo = True
            break
        if not locks:
            break

if is_out_of_ammo:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_money = intelligence_value - ((bullets_count - len(bullets)) * price_of_each_bullet)
    print(f'{len(bullets)} bullets left. Earned ${earned_money}')
