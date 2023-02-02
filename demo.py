substring = input()
second_string = input()

while substring in second_string:
    second_string = second_string.replace(substring, '')
print(second_string)