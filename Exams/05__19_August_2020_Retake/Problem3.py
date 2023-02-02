def numbers_searching(*numbers):
    min_number = min(numbers)
    max_number = max(numbers)

    missing_number = 0
    duplicate_numbers = []

    for i in range(min_number, max_number + 1):
        if i not in numbers:
            missing_number = i
        if numbers.count(i) > 1:
            duplicate_numbers.append(i)

    return [missing_number, sorted(duplicate_numbers)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
