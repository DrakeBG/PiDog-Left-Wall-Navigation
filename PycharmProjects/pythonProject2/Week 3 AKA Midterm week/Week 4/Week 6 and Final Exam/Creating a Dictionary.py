class_roster = {101:'jay', 102:'andy', 103:'robert', 104:'emma'}
roll_1 = class_roster[101]

print (roll_1)

dict_of_squares = {}
for i in range(10):
    dict_of_squares[i]=i**2
print(dict_of_squares)

print (len (dict_of_squares))

del (dict_of_squares[5])
print(dict_of_squares)

points_in_exam = {"Donald": 71, "Mickey":30, "Bugs":30, "Daffy":32, "Daffy":30 }
#dictionary is changeable
print (points_in_exam["Donald"])
points_in_exam["Donald"] = 78
print ("after chaging Donald's marks :", points_in_exam)
#
# #you can add new keys to a dictionary
points_in_exam["Spongebob"] = 67
print (points_in_exam)


dict1 = {1: "Donald", 2:"Mickey", 3:"Bugs", 4:"Daffy", "five":"SpongeBob"}
print (dict1)
print (type(dict1))
#a class has a bunch of methods which manipulate the data in the class
#

#use the keys method to get all the keys in the dictionary
print  (dict1.keys() )
# #
# # #use the values method to get all the values in the dictionary
print ( dict1.values() )
#
#use the keys method to iterate through all the keys in the dictionary
for k in dict1.keys():
     print (k)

for k in dict1.keys():
     print (k)
     print (dict1[k])


# #use the keys method to iterate through each key in the dictionary and then use its value
for k in dict1.keys():
    if (dict1[k] == "Bugs"):
        print ("Value Bugs has key :", k)
#
# #use the value method to iterate through each value in the dictionary
print (dict1.values())
for val in dict1.values():
    print (val)
#
# # #items method outputs the key:value pairs are tuples
print (list (dict1.items()))

word = "This is American University in Washington DC. TT"

letter_count ={}
# for char in word:
#     letter_count[char] = letter_count.get(char, 0)+1

for char in word:
    if char in letter_count.keys():
        letter_count[char] += 1
    else:
        letter_count[char] = 1

print (letter_count['n']) #Answer is 5

# for key in sorted(letter_count.keys()):
#     if letter_count[key] >1:
#         print (key, letter_count[key])
#
print (letter_count)

# for val in letter_count.values():
#     maxval = sorted(letter_count.values())[-1]
#
# maxletter = letter_count[maxval]
# print (maxletter)

