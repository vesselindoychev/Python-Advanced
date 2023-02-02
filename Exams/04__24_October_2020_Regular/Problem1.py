def scheduling(jobs, index):
    jobs_as_integers = [int(x) for x in jobs]

    wanted_number = jobs_as_integers[index]
    jobs_as_integers.remove(jobs_as_integers[index])
    cycles = 0
    for i in jobs_as_integers:
        if i <= wanted_number:
            cycles += i
    return cycles + wanted_number


jobs = input().split(', ')
index = int(input())

cycles = scheduling(jobs, index)
print(cycles)

"""
jobs_as_numbers = list(map(int, input().split(', ')))
index = int(input())

wanted_job = jobs_as_numbers[index]

jobs_as_numbers.remove(jobs_as_numbers[index])
need_numbers = []

for i in range(len(jobs_as_numbers)):
    if jobs_as_numbers[i] <= wanted_job:
        need_numbers.append(jobs_as_numbers[i])

result = sum(need_numbers) + wanted_job
print(result)
"""
