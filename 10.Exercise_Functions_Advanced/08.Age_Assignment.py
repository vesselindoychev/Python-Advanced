def age_assignment(*args, **kwargs):
    result = {}
    for i in args:
        first_letter = i[0]
        for k, v in kwargs.items():
            result[i] = kwargs[first_letter]

    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
