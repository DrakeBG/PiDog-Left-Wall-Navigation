file_handle = open('FileExerciseFile', 'a')

for x in range(1, 200):
    if (x % 5 == 0) and (x % 7 == 0):
        print(x, "is divisible by 5 and 7")
        file_handle.write(str(x))
        file_handle.write(str(" "))
    else:
        print(x, "is not divisible by 5 and 7")
file_handle.close()

file_handle = open('FileExerciseFile','r')#r = read mode

file_data = file_handle.read()
file_handle.close()#Close the file
print(file_data)