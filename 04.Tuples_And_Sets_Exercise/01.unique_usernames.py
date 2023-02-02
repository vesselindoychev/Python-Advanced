n = int(input())

unique_usernames = {input() for _ in range(n)}

[print(username) for username in unique_usernames]