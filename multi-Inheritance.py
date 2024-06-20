class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species

    def __str__(self) -> str:
        return f"Name: {self.name}\nSpecies: {self.species}"


class Dog(Animal):
    def __init__(self, name, breed) -> None:
        super().__init__(name, species="Dog")
        self.breed = breed

    def __str__(self) -> str:
        return f"{super().__str__()}\nBreed: {self.breed}"


class GoldenRetriever(Dog):
    def __init__(self, name, color) -> None:
        super().__init__(name, breed="Golden Retreiver")
        self.color = color

    def __str__(self) -> str:
        return f"{super().__str__()}\nColor: {self.color}"


dog = GoldenRetriever("Charlie", "Black")
print(dog)
