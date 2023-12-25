class Animal:
    def __init__(self, name="None"):
        self.name = name
    
    def print_animal_name(self):
        print(f"Animal Name: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__()
        self.name = "Bob"
        #super().__init__( name) # call the base class constructor
        self.breed = breed
        print(f"NAME: {self.name}")

    def bark(self):
        print(f"{self.name} is barking")

d = Dog("Spot", "Labrador")
d.bark() # prints "Spot is barking"
d.print_animal_name()
print(d.name) # prints "Spot"
print(d.breed) # prints "Labrador"