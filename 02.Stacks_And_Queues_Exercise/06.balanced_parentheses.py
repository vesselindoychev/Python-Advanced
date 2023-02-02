expression = list(input())

parentheses_dict = {
    '(': ')',
    '{': '}',
    '[': ']'
}

last_opened_bracket = []
is_balanced = True
for ch in expression:
    if ch in '([{':
        last_opened_bracket.append(ch)
    else:
        if not last_opened_bracket:
            is_balanced = False
            break
        bracket = last_opened_bracket.pop()
        if parentheses_dict[bracket] == ch:
            continue
        is_balanced = False
        break

if is_balanced and not last_opened_bracket:
    print('YES')
else:
    print('NO')