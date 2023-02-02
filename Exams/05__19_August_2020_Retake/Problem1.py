from collections import deque


def taxi_express(customers, taxis):
    customers_queue = deque([int(x) for x in customers])
    taxis_stack = [int(x) for x in taxis]

    total_time = 0

    while customers_queue and taxis_stack:
        current_customer = customers_queue.popleft()
        current_taxi = taxis_stack.pop()

        if current_customer <= current_taxi:
            total_time += current_customer
            continue

        customers_queue.appendleft(current_customer)

    return customers_queue, taxis_stack, total_time


customers = input().split(', ')
taxis = input().split(', ')

customers_queue, taxis_stack, total_time = taxi_express(customers, taxis)

if not customers_queue:
    print(f'All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')

if not taxis_stack and customers_queue:
    print(f'Not all customers were driven to their destinations')
    print(f"Customers left: {', '.join(map(str, customers_queue))}")

"""
# from collections import deque
# 
# customers = deque(list(map(int, input().split(', '))))
# taxis = list(map(int, input().split(', ')))
# 
# total_time = 0
# while customers and taxis:
#     current_customer = customers.popleft()
#     current_taxi = taxis.pop()
# 
#     if current_taxi >= current_customer:
#         total_time += current_customer
#         continue
# 
#     customers.appendleft(current_customer)
# 
# if not customers:
#     print(f'All customers were driven to their destinations')
#     print(f'Total time: {total_time} minutes')
# else:
#     print(f'Not all customers were driven to their destinations')
#     print(f'Customers left: {", ".join(map(str, customers))}')

"""
