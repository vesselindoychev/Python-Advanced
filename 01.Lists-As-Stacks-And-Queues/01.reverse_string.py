text = input()

res = []
reversed_word = []
for char in text:
    res.append(char)

for i in range(len(res)):
    reversed_word.append(res.pop())

print("".join(reversed_word))


