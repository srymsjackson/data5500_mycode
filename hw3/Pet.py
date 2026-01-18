class Pet:
    species = None

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def age_in_human_years(self):
        if self.species == "dog":
            return self.age * 7
        elif self.species == "cat":
            return self.age * 6
        elif self.species == "rabbit":
            return self.age * 8
        else:
            return None

    @classmethod
    def average_lifespan(cls, species):
        lifespans = {
            "dog": 13,
            "cat": 15,
            "rabbit": 9
        }
        return lifespans.get(species, "Unknown Species")


pet1 = Pet("Scout", 5, "dog")
pet2 = Pet("Midnight", 3, "cat")
pet3 = Pet("Thumper", 4, "rabbit")

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"{pet.name}'s age in human years:", pet.age_in_human_years())
    print(f"Average lifespan of a {pet.species}:", Pet.average_lifespan(pet.species))
    print()