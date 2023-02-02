from collections import deque

pizza_orders = deque(int(x) for x in input().split(', '))
employee_pizza_capacity = list(map(int, input().split(', ')))

total_pizza_made = 0
while len(pizza_orders) > 0 and len(employee_pizza_capacity) > 0:
    current_order = pizza_orders[0]
    current_capacity = employee_pizza_capacity[-1]

    if current_order > 10:
        pizza_orders.popleft()
        continue

    if current_order <= 0:
        pizza_orders.popleft()
        continue

    if current_order > current_capacity:

        current_order -= current_capacity
        total_pizza_made += current_capacity
        pizza_orders.popleft()
        pizza_orders.appendleft(current_order)
        employee_pizza_capacity.pop()

    else:
        total_pizza_made += current_order
        pizza_orders.popleft()
        employee_pizza_capacity.pop()

if not pizza_orders:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza_made}')
    print(f'Employees: {", ".join([str(x) for x in employee_pizza_capacity])}')

if pizza_orders and not employee_pizza_capacity:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in pizza_orders])}')
