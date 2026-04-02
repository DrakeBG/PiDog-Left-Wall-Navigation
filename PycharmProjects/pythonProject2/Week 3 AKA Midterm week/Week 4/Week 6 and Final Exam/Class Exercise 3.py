class Dog:
    def __init__(self, name, breed, color, has_spots):
        self.name = name
        self.breed = breed
        self.color = color
        self.has_spots = has_spots

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_color(self):
        return self.color

    def get_spots(self):
        return self.has_spots

    def set_name(self, name):
        self.name = name

    def set_breed(self, breed):
        self.breed = breed

    def set_color(self, color):
        if color == 'blue' or color == 'pink' or color == 'purple':
            return ("Dogs cannot be that color.")
        elif color == 'rainbow' :
            return("Dogs are not rainbows.")
        else:
            self.color = color

    def set_spots(self, spots):
        if spots == True or spots == False:
            self.has_spots = spots
        else:
            return ("Please input True or False.")

    def __str__(self):
        return (f'I am a {self.color} {self.breed} named {self.name}.')

    def bark(self, numbarks):
        return ("Woof! " * numbarks)

    def growl(self, numgrowl):
        return ("grrrrr " * numgrowl)


class Retriever(Dog):
    def __init__(self, name, breed, color, has_spots, weight, height, tail_wagging):
        Dog.__init__(self, name, breed, color, has_spots)
        self.weight = weight
        self.height = height
        self.tail_wagging = tail_wagging

    def get_height(self):
        return (self.height)


r1 = Retriever('Pickles', 'golden doodle', 'yellow', False, 54, 36, True)
print(r1.get_spots())
dog1 = Dog("Prince Harry", "Toy Poodle", "red", False)
dog1.get_height()