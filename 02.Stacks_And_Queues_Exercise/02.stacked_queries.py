n = int(input())

stack = []

for i in range(n):
    command = input()

    if command.startswith("1"):
        tokens = command.split()
        number = int(tokens[1])

        stack.append(number)

    elif command == "2":
        if stack:
            stack.pop()

    elif command == "3":
        if stack:
            print(max(stack))

    elif command == "4":
        if stack:
            print(min(stack))


print(", ".join(list(map(str, stack[::-1]))))

