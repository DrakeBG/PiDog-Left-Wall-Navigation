class Person():
    def __init__(self, fname, lname, dob):
        self.fname = fname
        self.lname = lname
        self.dob = dob
    #crete the getter and setter methods
    #also create the __str__ method
    def get_name(self):
        return (self.fname, self.lname)
    def printName(self):
        print(self.fname, self.lname)
class Student (Person):

    #construtor for the child class
    def __init__(self, fname, lname, dob, year, major, gpa):
        #the below is the parent's constructor
        Person.__init__(self, fname, lname, dob)
        #assign values to the child class attributes
        self.year = year
        self.major = major
        self.gpa = gpa

    #a child class method
    def printYear(self):
        print(self.year)


p1 = Person("narendra", "desirazu", "June 1 1990")
p1.printName()

s1 = Student("John", "Travolta", "June 1 2000", 2020,"CompSci", 3.4)
s1.printName() #printName is a Parent class method
s1.printYear() #printYear is a child class method

