class Dog:

    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def get_name(self):
        return self.name
    def get_breed(self):
        return self.breed
    def get_color(self):
        return self.color

    def set_name(self, newname):
        self.name = newname

    def set_breed(self, newbreed):
        self.breed = newbreed

    def set_color(self, newcolor):
        self.color = newcolor

    def __str__(self):
        returnstring = "My name is :" + str(self.name) + " My breed is :" + self.breed
        return returnstring

    def bark(self, numbarks):
        return numbarks * "woof"

    def grrr(self, numgrrrs):
        return numgrrrs * "grr"

dog1 = Dog("rover", "dalmation", "brown")
print(dog1.name)



dogname = dog1.get_name()
print(dogname)
dogbreed = dog1.get_breed()
print(dogbreed)
dogcolor = dog1.get_color()
print(dogcolor)

print(dog1) #My name is and breed is:

dog1.set_name("sparky")
dog1.set_breed("sitzu")
dog1.set_color("green")

dogname = dog1.get_name()
print(dogname)
dogbreed = dog1.get_breed()
print(dogbreed)
dogcolor = dog1.get_color()
print(dogcolor)

print(dog1)

barks = dog1.bark (19)
print(barks)
grrs = dog1.grrr (8)
print(grrs)