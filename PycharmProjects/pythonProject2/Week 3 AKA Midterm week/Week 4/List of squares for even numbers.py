list_squares = []
for i in range (100):
    if i % 2 == 0:
        list_squares.append(i**2)
print(list_squares)

list_squares = [0,4,16,36,64]

list1 = []
for i in range (0,10,2):
    list1.append(i**2)

print(list1)

list1 = []
for i in range (100):
    list1.append(i**2)

print(list1)
listsqr = [i**2 for i in range (100)]
print(listsqr)

listofsqrofeven = [i**2 for i  in range (100) if i%2==0]
print(listofsqrofeven)