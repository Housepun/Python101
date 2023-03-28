#Parent Class
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")
        
    def make_sound(self):
        print()

# Child Class
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, "dog", age)

    def make_sound(self):
        print(f"{self.name} says woof")

# Ceeating an instance of the Animal class
my_pet = Animal("Jodie","cat", 4)

# Accessing attributes of the Animal class
print(f"My pet is a {my_pet.species} named {my_pet.name}. It is {my_pet.age} years old.")

# Calling methods of the Animal class
my_pet.eat()
my_pet.sleep()
my_pet.make_sound()
