list1 =[1,2,3,4]

total = 0

for num in list1:
    var= num ** 2
    total = total + var
print(total)

list2 = [5,6,7,8,9]
even_count = 0
odd_count = 0
for x in list2:
    if x % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("How many even numbers:", even_count)
print("How many odd numbers:", odd_count)
