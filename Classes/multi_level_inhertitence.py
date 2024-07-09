class Animal:
    "Parent class to Bird"

    def eat(self):
        "all Mammals eat"
        print("eat")


class Bird(Animal):
    "Child class to Animal"

    def fly(self):
        "most birds"
        print("fly")


class Chicken(Bird):
    "Chickens can't fly"
    pass


# AVOID MULTI-LEVEL INHERITANCE !!!!!