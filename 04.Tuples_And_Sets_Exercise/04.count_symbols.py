text = input()

symbol_count = {}

for ch in text:
    if ch not in symbol_count:
        symbol_count[ch] = 1
    else:
        symbol_count[ch] += 1

for key, value in sorted(symbol_count.items()):
    print(f"{key}: {value} time/s")