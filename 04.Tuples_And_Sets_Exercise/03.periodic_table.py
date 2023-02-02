n = int(input())

elements = set()

for i in range(n):
    periodic_elements = input().split()

    for periodic_element in periodic_elements:
        elements.add(periodic_element)

[print(el) for el in elements]
