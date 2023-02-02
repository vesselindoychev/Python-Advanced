class Party:
    def __init__(self):
        self.people = []


party_people = Party()

while True:
    name = input()
    if name == 'End':
        break
    party_people.people.append(name)

if party_people.people:
    print(f'Going: {", ".join(party_people.people)}')
    print(f'Total: {len(party_people.people)}')
