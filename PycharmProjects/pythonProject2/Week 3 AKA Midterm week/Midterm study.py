def circle_area(radius):
    area = 3.14 * radius ** 2
    return area
print(circle_area(10), circle_area(1))
print('is the same as:', 3.14 * 10 ** 2, 3.14 * 1 ** 2)

a= str.title('drake greene')
print(a)

name = ["D","r","a","k","e"]
name.append(["G","r","e","e","n","e"])
print(name)

name = ["D","r","a","k","e"]
name.extend(["G","r","e","e","n","e"])
print(name)

name = ["D","r","a","k","e"]
name.extend(["G","r","e","e","n","e"])
name.clear() #CLEAR
print(name)

name = ["D","r","a","k","e"]
name.extend(["G","r","e","e","n","e"])
name.remove("e")
print(name)

name = ["D","r","a","k","e"]
name.extend(["G","r","e","e","n","e"])
name.remove("e")
name.insert(4, "!")
print(name)

name = ["D","r","a","k","e"]
name.extend(["G","r","e","e","n","e"])
name.sort() #SORT in increasing order
print(name)

dict={'AU':13061,'UMD':40521,'GW':25613}
dict['GT']=42
print(dict)

lst = [10, 100, 200]
for indx in range(len(lst)):
    print(indx, lst[indx])

for key in {4: 50, 7: 80}:
    print(key, end=' ')
