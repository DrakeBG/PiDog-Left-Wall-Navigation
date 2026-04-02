myName = "Narendra"
print (myName)
myUniversity = "American University"
print (myUniversity)
value_of_PI = 3.1415926
print (value_of_PI)
num_apples = 10
additional_apples = 23
total_apples = num_apples + additional_apples
print (total_apples)

#Square
print(18**2)
#Anwser 324
#To the power 5
print(18**5)
#Anwser 1889568
#Square root
print(9**0.5)
#Anwser 3.0
#Find the remainder
print(4%3)
#Anwser 1
#order of operations
print(4 + (3-2) * 6)
#Anwser 10
#String
print("hello" + "world")
#Anwser helloworld
#Pass
def sqr_root(x):
    if x > 0:
        return x**0.5
    else:
        pass
#main program
print (sqr_root(-16))
#Anwser None
#Escape Sequence
print("Hello \n World!")
#Anwser Hello
#        World!
# String
fruit_1 = "Orange"
fruit_2 = 'Apple'
fruit_3 = 'Banana'
fruit_basket = fruit_1 + fruit_2 + fruit_3
print (fruit_basket)
#Anwser OrangeAppleBanana
fruit_1 = "Orange"
oranges = fruit_1 *3
print (oranges)
#Anwser OrangeOrangeOrange
fruit_1 = "Orange "
fruit_2 = 'apple '
fruit_3 = 'Banana'
#String comparisons
if (fruit_1 == "Orange "):
    print ("fruits are the same")
if (fruit_2 < fruit_3):
    print ("fruit 2 < fruit 3 :", fruit_2, fruit_3)
else:
    print("fruit 3 < fruit 2 :", fruit_3,fruit_2)
#Anwser fruits are the same
#fruit 3 < fruit 2 : Banana apple
#Length of a string
string_1 = "string"
#get the length of the string - number of characters including spaces
str_len = len(string_1)
print (str_len)
#Anwser 6
#Parts of a string
index=0
while index < str_len :
    print ( string_1[index] )
    index += 1
# Anwser
#s
#t
#r
#i
#n
#g
#Slicing a string
string1 = "abracadabra"
#0=a, 1=b, 2=r, 3=a, 4=c, 5=a, ...
print ( string1[2:7] )
#racad
print ( string1[3:])
#acadabra - starting from index 3 till the end
print ( string1[:5])
#abrac - starting from the beginning till index 4 (upto index 5 not including 5)
print ( string1[:-1])
#abrac - starting from the beginning till the end
print ( string1[-5:-1])
#abrac - starting from the index -5 till the end
# In Operators
vowels = 'aeiouAEIOU'
vowel_count = 0
for x in string1:
    if x in vowels:
        vowel_count +=1
print (vowel_count)
#Answer 5
#String methods
string_1 = "string"
print(string_1)
#get the type of this variable
print (type(string_1))
#convert the characters to upper case
string_2 = string_1.upper()
print(string_2)
#convert the characters to lower case
string_3 = string_2.lower()
print(string_3)
#capitalize the first character
string_capitalize = string_1.capitalize()
print (string_capitalize)
# Anwser string
# <class 'str'>
# STRING
# string
# String
#String format
n1="narendra"
n2="tom"
n3="robert"
print ("The team members are {0}, {1}, {2}". format (n1,n2,n3))
#Answer The team members are narendra, tom, robert
print ("The team members are {0}, {1:>10}, {2}". format (n1,n2,n3))
#Answer The team members are narendra,        tom, robert
#List
wizard_players = ['Trevor Ariza', 'Bradley Beal', 'Troy Brown', 'Thomas Bryant', 'Sam Dekker']
print(wizard_players)
#Anwser ['Trevor Ariza', 'Bradley Beal', 'Troy Brown', 'Thomas Bryant', 'Sam Dekker']
print(wizard_players[2])
#Anwser Troy Brown
print(wizard_players[-1])
#Anwser Sam Dekker
#Slicing List
odd_numbers = [1,3,5,7,9,11,13,15]
print(odd_numbers[3:5])
print(odd_numbers[3:])
print(odd_numbers[:])
print(odd_numbers[-1])
print(odd_numbers[:-1])
print(odd_numbers[-3:-1])
#Using List
squares = [1,4,9,16,25]
print(squares[2]*2)
print(squares[3]**0.5)
#List Operation
list1 = ['a', 'm', 'e', 'r', 'i', 'c', 'a', 'n']
list2 = ['u', 'n', 'v', 'e', 'r', 's', 'i', 't', 'y']
list_cat = list1 + list2
print (list_cat)
#Anwser ['a', 'm', 'e', 'r', 'i', 'c', 'a', 'n', 'u', 'n', 'v', 'e', 'r', 's', 'i', 't', 'y']
#lists are mutable
sqrs = [1,1,2,4,3,9,6,36]
sqrs [6:9] = [4,16,5,25]
print (sqrs)
#Answer [1, 1, 2, 4, 3, 9, 4, 16, 5, 25]
#Aliasing list
list_a = [1,2,3,4]
print (list_a)
#using = operator to create another list
list_b = list_a
print (list_b)
#modifying one list impacts the other
list_b[2] = 16
print ("list a = ", list_a)
print ("list b = ", list_b)
#Anwser [1, 2, 3, 4]
#[1, 2, 3, 4]
#list a =  [1, 2, 16, 4]
#list b =  [1, 2, 16, 4]
#Cloning list
#use copy method to create a clone
list_c = list_a.copy()
print (list_c)
#modifying one lists doest not impact the other
list_c[2] = 3
print ("list c = ", list_c)
print ("list a = ", list_a)
#Anwser [1, 2, 16, 4]
#list c =  [1, 2, 3, 4]
#list a =  [1, 2, 16, 4]
#Strings and Lists
str1 = "This is American University. It is a great place to study"
list1 = str1.split()
print (list1)
str2 = " ".join(list1)
print (str2)
str3 = ";".join(list1)
print (str3)
#Anwser ['This', 'is', 'American', 'University.', 'It', 'is', 'a', 'great', 'place', 'to', 'study']
#This is American University. It is a great place to study
#This;is;American;University.;It;is;a;great;place;to;study
#Import
import math
sqrrt_3 = math.sqrt(3)
print (sqrrt_3)
#1.7320508075688772
print (math.factorial(4))
#24
x=3
area_of_circle = math.pi*x**2
print (area_of_circle)
#28.274333882308138
import calendar
print (dir(calendar))
#dir (module_name) shows you all the functions in the module
print (calendar.isleap(1967))
#['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth', '_locale', '_localized_day', '_localized_month', '_monthlen', '_nextmonth', '_prevmonth', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthrange', 'prcal', 'prmonth', 'prweek', 'repeat', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']
#For Loop
wizard_players = ['Trevor Ariza', 'Bradley Beal', 'Troy Brown', 'Thomas Bryant']
for player_name in wizard_players :
    print(player_name)
#Anwser Trevor Ariza
#Bradley Beal
#Troy Brown
#Thomas Bryant
#Range function
for i in range(4):
    print (i)
#Anwser 0
#1
#2
#3
for m in range(2,5):
    print (m)
#Anwser 2
#3
#4
for m in range(0,10,2): #Goes to 10 by 2s
    print (m)
#Anwser 0
#2
#4
#6
#8
#While Loop
countdown = 10
while countdown > 0:
    print (countdown)
    countdown = countdown-1
print ("Blastoff!")
#Anwser 10
#9
#8
#7
#6
#5
#4
#3
#2
#1
#Blastoff!
#find all odd number between two numbers
num1 = 3
num2 = 29
#start with the smaller of the 2 numbers
if num1<num2:
    count = num1
    larger = num2
else:
    count = num2
    larger = num1
while (count < larger) :
    if ((count%2) == 1):
        print (count, 'is an odd number')
    count = count+1
print ('we have printed all odd numbers between', num1, 'and', num2)
#Anwser we have printed all odd numbers between 3 and 29
#Calling a function
def time_taken (dist):
    speed = 20
    timeTaken = round(dist/speed)
    return (timeTaken)
time_1 = time_taken(3.55)
print(time_1)
#Anwser 0
def convert_to_inches (len_in_cms):
    len_in_inches = len_in_cms*0.3937
    return len_in_inches
len_of_sqr = convert_to_inches(30)
print(len_of_sqr)
#Anwser 11.811
def print_my_name (fname, lname):
    print (fname, lname)
myfName = 'Narendra'
mylName = 'Desirazu'
# calling the function
print_my_name (myfName,mylName)
print_my_name ('James', 'Bond')
print ('this is the last line of the program')
#Anwser Narendra Desirazu
#James Bond
#this is the last line of the program
#List of Squares of even numbers
list_squares = []
for i in range (10):
    if i%2==0:
        list_squares.append(i**2)
print(list_squares)
#Anwser [0, 4, 16, 36, 64]
#List of Squares of even numbers using List Comprehensions
squares_list = [ i**2 for i in range (10) if i%2==0 ]
print(squares_list)
#Anwser [0, 4, 16, 36, 64]
#Using a function to generate a list
def func(n):
    if n%2 == 0:
        return n**2
    else:
        return n**3
list1 = [func(i) for i in range (30)]
print(list1)
#Anwser [0, 1, 4, 27, 16, 125, 36, 343, 64, 729, 100, 1331, 144, 2197, 196, 3375, 256, 4913, 324, 6859, 400, 9261, 484, 12167, 576, 15625, 676, 19683, 784, 24389]
#Using OO to create a Student class
class Student:
    name = ""
    dob = ""
    gender = ""
    rollnum = ""
    major = ""
john = Student()
john.name = "John"
john.dob = "1/1/2000"
john.gender = 'm'
john.rollnum = 'AU123'
john.major = 'compsci'
print (john.name)
#Anwser John
#Defining a class – with a constructor
class Student:
    def __init__(self, name, dob, gender, rollnum, major):#This is a constructor
        self.name = name
        self.dob = dob
        self.gender = gender
        self.rollnum = rollnum
        self.major = major
john = Student('John', '1/1/2000', 'm', 'AU123', 'compsci')
print (john.name)
#Anwser John
#Tuple within a tuple
john = ('Lennon', 1940)
paul = ('McCartney', 1942)
george = ('Harrison', 1940)
beatles = (john, paul, george)
print(beatles[0])
print(beatles[2])
print(beatles[1][1])
print(beatles[1][0])
#Anwser ('Lennon', 1940)
#('Harrison', 1940)
#1942
#McCartney
#Using tuples – packing & unpacking
#packing
john = ('CSC280', 12, 'Business', 'Freshman')
print(john)
#('CSC280', 12, 'Business', 'Freshman')
robert = ('CSC280', 22, 'Biophysics', 'Sophomore')
print(robert)
#('CSC280', 22, 'Biophysics', 'Sophomore')
#unpacking
(course, roll_num, major, year) = john
print(course)
#CSC280
print(roll_num)
#12
print(major)
#Business
print(year)
#Freshman
#Using Tuple to swap variables
a=10
b=23
(b,a)=(a,b)
print(a)
#23
print(b)
#10
#Tuple as a return from a function
def area_perimeter (a,b=10):
    area = a*b
    perimeter = 2*a+2*b
    return (area, perimeter)
(area_1, peri_1) = area_perimeter(3,5)
print ("area =", area_1)
print("perimteter =", peri_1)
#Anwser area = 15
#perimteter = 16
#Creating a Dictionary
rollnums = {101:'jay', 102:'andy', 103:'robert', 104:'emma'}
print(rollnums[101])
#Anwser jay
print(rollnums[104])
#Anwser emma
#creating a heterogenous dictionary
h_dict = {1:"narendra", "two":("John", 201), "mary":[1,3,6,9], 3.1415:"value of pi"}
print(h_dict[1])
#Awnser narendra
print(h_dict["two"])
#Anwser ('John', 201)
print(h_dict["mary"])
#Anwser [1, 3, 6, 9]
print(h_dict[3.1415])
#Anwser value of pi
#Dict Random access
dict1 = {"num1": "Donald", "num2":"Mickey", "num3":"Bugs", "num4":"Daffy"}
print (dict1["num1"])
print (dict1["num2"])
print (dict1["num3"])
print (dict1["num4"])
#Anwser Donald
#Mickey
#Bugs
#Daffy
#the order inside the dictionary doesn’t matter
dict2 = {"num2":"Mickey", "num1": "Donald","num4":"Daffy" , "num3":"Bugs"}
print (dict2["num1"])
print (dict2["num2"])
print (dict2["num3"])
print (dict2["num4"])
#Anwser Donald
#Mickey
#Bugs
#Daffy
#Operations on a Dictionary
marks_in_exam = {"Donald": 71, "Mickey":63, "Bugs":98, "Daffy":32}
print ("before chaging the marks :", marks_in_exam)
#length of a dictionary
print ("the number of pairs in the dictionary is ", len(marks_in_exam))
#dictionary is changeable
marks_in_exam["Donald"] = 78
print ("after chaging Donald's marks :", marks_in_exam)
#arithmetic operations
marks_in_exam["Mickey"] += 10
print ("after chaging Mickey's marks :", marks_in_exam)
#deleting items key:value pair
del marks_in_exam["Daffy"]
print ("after deleting Daffy :", marks_in_exam)
#Anwser before chaging the marks : {'Donald': 71, 'Mickey': 63, 'Bugs': 98, 'Daffy': 32}
#the number of pairs in the dictionary is  4
#after chaging Donald's marks : {'Donald': 78, 'Mickey': 63, 'Bugs': 98, 'Daffy': 32}
#after chaging Mickey's marks : {'Donald': 78, 'Mickey': 73, 'Bugs': 98, 'Daffy': 32}
#after deleting Daffy : {'Donald': 78, 'Mickey': 73, 'Bugs': 98}
#Modules & import statement
import math
sqrrt_3 = math.sqrt(3)
print (sqrrt_3)
print (math.factorial(4))#Module
x=3
area_of_circle = math.pi*x**2
print (area_of_circle)
import calendar
print (dir(calendar))
#dir (module_name) shows you all the functions in the module
print (calendar.isleap(1967))
#Anwser 1.7320508075688772
#24
#28.274333882308138
#['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth', '_locale', '_localized_day', '_localized_month', '_monthlen', '_nextmonth', '_prevmonth', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthrange', 'prcal', 'prmonth', 'prweek', 'repeat', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']
