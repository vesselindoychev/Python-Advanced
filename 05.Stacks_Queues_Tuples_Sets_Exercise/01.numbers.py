first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

max_length = first_set
min_length = second_set

if first_set < second_set:
    max_length = second_set
    min_length = first_set
n = int(input())

for _ in range(n):
    tokens = input().split()
    command = tokens[0]
    parameter = tokens[1]
    numbers = [int(x) for x in tokens[2:]]

    if command == "Add" and parameter == "First":
        [first_set.add(x) for x in numbers]

    elif command == "Add" and parameter == "Second":
        [second_set.add(x) for x in numbers]

    elif command == "Remove" and parameter == "First":
        # [first_set.remove(x) for x in numbers if x in first_set]
        current_set = set(numbers)
        first_set = first_set.difference(current_set)

    elif command == "Remove" and parameter == "Second":
        # [second_set.remove(x) for x in numbers if x in second_set]
        current_set = set(numbers)
        second_set = second_set.difference(current_set)

    elif command == "Check" and parameter == "Subset":
        if min_length.issubset(max_length):
            print(True)
        else:
            print(False)

first_set = sorted(first_set)
second_set = sorted(second_set)
first_set = list(map(str, first_set))
second_set = list(map(str, second_set))

print(', '.join(first_set))
print(', '.join(second_set))
