symbols = {'.', '?', '!', ',', ';', ':', '-', '_', "'", '"', }

index = 1

with open('text.txt', 'r') as file, open('output.txt', 'w') as file_output:

    for line in file:
        symbols_count = 0
        letters = 0
        tokens = list(line.strip())

        for ch in tokens:
            if ch.isalpha():
                letters += 1
            elif ch == ' ':
                symbols_count += 0
            else:
                symbols_count += 1

        file_output.write(f'Line {index}: {line.strip()} ({letters})({symbols_count})')
        file_output.write('\n')
        index += 1


