numbers = list(map(int, input().split()))

positive_numbers = filter(lambda x: x > 0, numbers)
negative_numbers = filter(lambda x: x < 0, numbers)

positive_add_result = sum(positive_numbers)
negative_add_result = sum(negative_numbers)

print(negative_add_result)
print(positive_add_result)
if abs(negative_add_result) > positive_add_result:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")
