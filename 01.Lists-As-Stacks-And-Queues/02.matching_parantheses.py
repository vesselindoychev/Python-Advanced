expression = list(input())

indices = []
last_bracket = 0

for index, ch in enumerate(expression):
    if ch == "(":
        indices.append(index)
    elif ch == ")":
        last_bracket = index
        start_index = indices.pop()
        print("".join(expression[start_index:last_bracket + 1]))