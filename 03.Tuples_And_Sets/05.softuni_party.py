n = int(input())

guest_list = set()

for _ in range(n):
    guest = input()

    guest_list.add(guest)

while True:
    command = input()
    if command == "END":
        break
    guest_list.remove(command)


vip_guests = sorted([v_g for v_g in guest_list if v_g[0].isdigit()])
regular_guests = sorted([r_g for r_g in guest_list if not r_g[0].isdigit()])

print(len(guest_list))
[print(g) for g in vip_guests]
[print(g) for g in regular_guests]
