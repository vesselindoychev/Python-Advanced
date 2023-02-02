numbers = list(map(float, input().split()))

count_dict = {}

for number in numbers:
    if number not in count_dict:
        count_dict[number] = 0
    count_dict[number] += 1


for key, value in count_dict.items():
    print(f"{key:.1f} - {value} times")