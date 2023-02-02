from collections import deque

expression = input().split()

numbers = deque()


arithmetic_dict = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}

for ch in expression:
    if ch.lstrip('-').isdigit():
        numbers.append(int(ch))
    else:
        result = numbers.popleft()
        while numbers:
            number = numbers.popleft()
            result = arithmetic_dict[ch](result, number)

        numbers.append(result)

print(numbers.pop())


# from math import floor
#
# text = input().split()
#
# text_twin = text
# temp = []
# operator = 0
# res = ""
#
# idx = 0
# index_char = 0
# for el in range(len(text)):
#     if not text[el].isdigit():
#         index_char = el
#
# while len(text_twin) > 1:
#     a = text_twin[idx].lstrip('-')
#     if a.isdigit():
#         temp.append(text_twin[idx])
#         idx += 1
#     else:
#         operator = text_twin[idx]
#         index_char = idx
#         idx = 0
#
#         for i in range(len(temp)):
#             if i == len(temp) - 1:
#                 res += temp[i]
#             else:
#                 res += temp[i]
#                 res += operator
#
#         del text_twin[0:index_char + 1]
#         res = floor(eval(res))
#         text_twin.insert(0, str(res))
#         res = ""
#         temp = []
#
# number = float(text_twin[0])
# print(floor(number))
