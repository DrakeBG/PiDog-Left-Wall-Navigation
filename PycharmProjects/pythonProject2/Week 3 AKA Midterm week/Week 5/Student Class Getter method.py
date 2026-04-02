class Student:
    def __init__(self, name, dob, id , major, gpa = 0): # function name is always "__init__(self):"
        self.name = name
        self. dob = dob
        self.id = id
        self.major = major

# Getter method
    def get_name(self):
        return (self.name)

s1 = Student("John", "1/1/2000", "AU123", "ComputSci")

name1 = (s1.get_name())
print(s1.get_name())
print(name1)