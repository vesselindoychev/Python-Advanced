# def expressions(numbers, current_result, expression=''):
#     if not numbers:
#         return [(expression, current_result)]
#     result_plus = expressions(
#         numbers[1:],
#         current_result + numbers[0],
#         f'{expression}+{numbers[0]}')
#     result_minus = expressions(
#         numbers[1:],
#         current_result - numbers[0],
#         f'{expression}-{numbers[0]}')
#     return result_plus + result_minus
#
# result = expressions(input().split(', ') * len(input().split(', ')), 0)
# [print(f'{exp_str}={exp_result}') for (exp_str, exp_result) in result]
#
#
# exp_num = [int(x) for x in input().split(', ')]


import itertools

numbers = [x for x in input().split(', ')]
x = len(numbers)

permutations = set(itertools.permutations(['-'] * x + ['+'] * x, x))

for permutation in permutations:
    expression = ''.join(itertools.chain(*zip(permutation, numbers)))
    res = eval(expression)
    print(f"{expression}={res}")