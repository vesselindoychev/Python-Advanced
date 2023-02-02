from collections import deque

# arithmetic_operations = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: a / b
# }

total_honey_made = 0

bees = deque([int(x) for x in input().split()])
nectar_value = [int(x) for x in input().split()]
symbols = deque(input().split())

while bees and nectar_value:
    current_bee = bees.popleft()
    current_nectar = nectar_value.pop()

    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()

        if current_symbol == "+":
            total_honey_made += abs(current_bee + current_nectar)
        elif current_symbol == "-":
            total_honey_made += abs(current_bee - current_nectar)
        elif current_symbol == "*":
            total_honey_made += abs(current_bee * current_nectar)
        elif current_symbol == "/":
            if current_nectar > 0:
                total_honey_made += abs(current_bee / current_nectar)

        # res = abs(arithmetic_operations[current_symbol](current_nectar, current_bee))
    else:
        bees.appendleft(current_bee)

print(f"Total honey made: {total_honey_made}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")

if nectar_value:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_value])}")
