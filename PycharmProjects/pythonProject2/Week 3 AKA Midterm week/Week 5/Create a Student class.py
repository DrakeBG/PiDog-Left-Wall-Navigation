class Student:
    name = ""
    dob = ""
    id = ""
    major = ""

student1 = Student()

print((type)(student1))

var1 = 10
var2 = 3.14
var3 = "Drake"
print((type)(var1))
print((type)(var2))
print((type)(var3))

student1.name = "Drake"
student1.dob = "6/15/2004"
student1.id = "AU"
print(student1.name, student1.dob, student1.id)

student2 = Student()
student2.name = "Joe"
student2.dob = "2/10/1957"
student2.major = "pol sci"

print(student2.name)