class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def fetch(self):
        print(f"{self.name} is fetching the ball.")

new_dog = Dog("Buddy", "Golden Retriever")
print(new_dog.make_sound())
new_dog.fetch()