class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer, Swimmer):
    pass

# multiple inheritance should not be used for classes with similar methods, IE two Def Greet: methods
