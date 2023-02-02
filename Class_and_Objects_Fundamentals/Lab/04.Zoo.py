class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.birds = []
        self.fishes = []

    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        if species == 'bird':
            self.birds.append(name)
        if species == 'fish':
            self.fishes.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ''

        if species == 'mammal':
            result += f'Mammals in {self.name}: {", ".join(self.mammals)}\n'
        if species == 'bird':
            result += f'Birds in {self.name}: {", ".join(self.birds)}\n'
        if species == 'fish':
            result += f'Fishes in {self.name}: {", ".join(self.fishes)}\n'

        result += f'Total animals: {Zoo.__animals}'
        return result


zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())

for i in range(n):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animals(species, name)

species_info = input()

print(zoo.get_info(species_info))
