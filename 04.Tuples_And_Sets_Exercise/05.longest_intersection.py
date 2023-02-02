n = int(input())




current_res = set()
longest_intersection = set()
for _ in range(n):
    text = input().split("-")
    first_length = text[0].split(",")
    second_length = text[1].split(",")

    first_start = int(first_length[0])
    first_end = int(first_length[1])

    second_start = int(second_length[0])
    second_end = int(second_length[1])

    first_set = {i for i in range(first_start, first_end + 1)}
    second_set = {i for i in range(second_start, second_end + 1)}

    current_res = first_set.intersection(second_set)

    if len(current_res) > len(longest_intersection):
        longest_intersection = current_res

longest_intersection = [str(x) for x in longest_intersection]

print(f"Longest intersection is [{', '.join(longest_intersection)}] with length {len(longest_intersection)}")