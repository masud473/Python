
class Animal:
    def __init__(self,name,species) -> None:
        self.name=name
        self.species=species
    def make_sound(self):
        print('Sound made by animal')
class cat(Animal):
    def __init__(self, name, species,breed) -> None:
        super().__init__(name, species)
        self.breed=breed
    def make_sound(self):
        print('Mew!')
d=cat('abd','dab','few')
d.make_sound()