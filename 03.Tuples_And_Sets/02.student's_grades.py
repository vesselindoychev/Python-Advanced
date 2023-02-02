n = int(input())

student_dict = {}

for _ in range(n):
    text = input().split()
    name = text[0]
    grade = float(text[1])

    if name not in student_dict:
        student_dict[name] = []

    student_dict[name].append(grade)

for key, value in student_dict.items():
    average = sum(value) / len(value)

    string_grades = [str(f"{x:.2f}") for x in value]
    print(f"{key} -> {' '.join(string_grades)} (avg: {average:.2f})")
