class Dog:

    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def get_name(self):
       return self.name

    def set_name(self, newname):
        if self.breed == "dalmatian":
            self.name = newname
        else:
            self.name = "Dog has no name"

    def __str__(self):
        returnstring = "My name is :" + str(self.name) + "My breed is -" +self.breed
        return returnstring

    def bark(self, numbarks):
        return numbarks * "woof"


dog1 = Dog("rover", "dalmatian", "brown")
#print (dog1.name)

print (dog1.get_name() )

dog1.name = "sparky"

dog1.set_name("sparky")

print ( dog1.get_name() )

dog2 = Dog ("johnny", "poodle", "black")

print ( dog1)
print (dog2)

barks = dog1.bark (5)
print (dog2.bark (6))
print (barks)
