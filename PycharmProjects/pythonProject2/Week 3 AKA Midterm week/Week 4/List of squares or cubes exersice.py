List1 = [i for i in range(4,300) if (i % 5 == 0) and (i % 7 == 0)] #Creat a list of muliples of 5 and 7 between 4 and 300
print(List1)

def fibnum(n):
    a=1
    b=1
    for i in range (n):
        anext = a + b # 1 + 1 = 2
        a = b # a = 1 (b)
        b = anext # b = 2 (anext)
    return anext # returns 2

list1 = [fibnum(i) for i in range (1,30)]
print (list1)
