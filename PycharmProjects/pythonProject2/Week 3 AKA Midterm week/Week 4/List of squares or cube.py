list1 = [i**2 if i%2==0 else 1**3 for i in range(30)]
print(list1)

def func(n):
    if n % 2 == 0:
        return n**2
    else:
        return n**3

List1 = [func(i) for i in range(30)]
print(List1)