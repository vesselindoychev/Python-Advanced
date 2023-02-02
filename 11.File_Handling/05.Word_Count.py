input_file = open('input.txt', 'w')

input_file.write('-I was quick to judge him, but it wasn\'t his fault.\n')
input_file.write('-Is this some kind of joke?! Is it?\n')
input_file.write('-Quick, hide here…It is safer.\n')


input_file = open('input.txt', 'r')
words_file = open('words.txt', 'w')

words_file.write('quick is fault')
words_file = open('words.txt', 'r')

result = []

for line in words_file:
    tokens = line.split()
    for word in tokens:
        counter  = 0
        for line2 in input_file:
            tokens2 = line2.split()
            for word2 in tokens2:
                if word in word2.lower():
                    counter += 1

        result.append([word, counter])

print(result)

