numbers_sting = input().split()

stack = []

for index in range(len(numbers_sting)):
    stack.append(numbers_sting.pop())

print(" ".join(stack))