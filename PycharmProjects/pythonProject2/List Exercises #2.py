even_list = [2,4,6,8,10,12,14,16,18,20]
odd_list = [1,3,5,7,9,11,13,15,17,19]

print(even_list[0:10])
print(odd_list[0:10])

num_list = even_list + odd_list
print(num_list)

del(num_list[3:7]) #Removes from list
print(num_list)

num_list[0] = 5 #Replaces number in list
print(num_list)

num_list.append(27) #Add new number in list
print(num_list)

num_list.sort() #Put numbers in order
print(num_list)

num_list.remove(7) #Removes from list
print(num_list)

num_list.insert(3, 100) #Put the 100 in the 3rd spot
print(num_list)

