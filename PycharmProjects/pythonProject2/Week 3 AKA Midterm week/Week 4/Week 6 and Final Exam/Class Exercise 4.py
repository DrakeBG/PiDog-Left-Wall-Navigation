class Cat:

    def __init__(self, name, age, breed, coat, purring):
        self.name = name
        self.age = age
        self.breed = breed
        self.coat = coat
        self.purring = purring

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_breed(self):
        return self.breed
    def get_coat(self):
        return self.coat
    def get_purring(self):
        return self.purring

    def set_name(self, newname):
        self.name = newname
    def set_age(self, newage):
        self.age = newage
    def set_breed(self, newbreed):
        self.breed = newbreed
    def set_coat(self, newcoat):
        self.coat = newcoat
    def set_purring(self, newpurring):
        self.purring = newpurring

    def hiss(self, numhiss):
        return numhiss * "ssss"

    def meow(self, nummeows):
        return nummeows * "meow"

    def __str__(self):
        if self.purring is True:
            returnstring = str(self.name) + " is happy"
            return returnstring
        else:
            returnstring = str(self.name) + " is not happy"
            return returnstring

class Kitten(Cat):
    def __init__(self, name, age, breed, coat, purring, jumping, good_mood):
        Cat.__init__(self, name, age, breed, coat, purring)
        self.jumping = jumping
        self.good_mood = good_mood

    def __str__(self):
        if self.jumping == True and self.good_mood is True:
            returnstring2 = str(self.name) + " is happy"
            return returnstring2
        else:
            returnstring2 = str(self.name) + " is not happy"
            return returnstring2


cat1 = Cat("Gardflied","20", "Cat", "Orange", True)
print(cat1.name)

catname = cat1.get_name()
print(catname)
catage = cat1.get_age()
print(catage)
catbreed = cat1.get_breed()
print(catbreed)
catcoat = cat1.get_coat()
print(catcoat)
catpurring = cat1.get_purring()
print(catpurring)

print(cat1)

Kit = Kitten("Whisker",'56','cat','green',True,True,True)
print(Kit.name)
print(Kit.age)
print(Kit.breed)
print(Kit.coat)
print(Kit.purring)
print(Kit.jumping)
print(Kit.good_mood)