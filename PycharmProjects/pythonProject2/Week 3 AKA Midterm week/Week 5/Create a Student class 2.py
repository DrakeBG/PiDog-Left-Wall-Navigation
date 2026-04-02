class Student:
    def __init__(self, name, dob, id , major, gpa = 0): # function name is always "__init__(self):"
        self.name = name
        self. dob = dob
        self.id = id
        self.major = major



student1 = Student("John", "1/1/2000", "AU123", "ComputSci")
print(student1.name, student1.dob, student1.major, student1.id)

student1.gpa = 4.0
print(student1.gpa)



