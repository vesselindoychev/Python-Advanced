def operate(first_number, operator, second_number):
    result = 0
    if operator == '+':
        result = sum(first_number, second_number)

    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        result = first_number / second_number

    elif operator == '-':
        result = first_number - second_number

    elif operator == '^':
        result = first_number ** second_number

    return result


print(f"{operate(2.5, '*', 2):.2f}")
print(f'{operate(6.66, "^", 2):.2f}')
print(f'{operate(36.66, "/", 6):.2f}')

