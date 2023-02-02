def operate(operator, *args):
    result = 0
    index = 0
    if operator == "+":
        result = sum(args)
        return result

    if operator == '*':
        result = 1
        for i in range(len(args)):
            result *= args[i]
        return result

    if operator == '-':
        result = args[0]
        for i in range(len(args)):
            if i == 0:
                continue
            result -= args[i]

        return result

    if operator == '/':
        result = args[0]
        for i in range(len(args)):
            if i == 0:
                continue
            result /= args[i]

        return result



print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
