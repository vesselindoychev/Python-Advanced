command = input()
numbers = [int(x) for x in input().split()]

result = 0
parity = 0 if command == "Even" else 1

for number in numbers:
    if number % 2 == parity:
        result += number

print(result * len(numbers))
