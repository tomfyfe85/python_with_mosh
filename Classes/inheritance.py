"""
This module defines the Animal class and its subclasses Mammal and Fish.
"""


class Animal:
    "Parent class to Mammal, Fish"

    def __init__(self):
        print("animal constructor")
        self.age = 1

    def eat(self):
        "all Mammals eat"
        print("eat")


class Mammal(Animal):
    "Child class to Animal"

    def __init__(self):
        print("Mammal constructor")
        # super().__init__() 

        self.weight = 2

    def walk(self):
        "all land Mammals"
        print("walk")


class Fish(Animal):
    "Child to animal"

    def swim(self):
        "all land Mammals"
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
