file_handle = open('myTestFile.txt','r')#r = read mode

file_data = file_handle.read()
file_handle.close()#Close the file
print(file_data)

file_handle2 = open('myTestFile.txt','w')#w = write mode
file_handle2.write("This is my new line of text")

file_handle2.close()

file_handle3 = open('NewTestFile.txt','w')#Write and a flie that doesn't exist creates a new file

file_handle3.write("Another new line of text")

file_handle3.close()

file_handle4 = open('NewTestFile.txt','w')#Write and a flie that doesn't exist creates a new file

file_handle4.write("Another new line of text\n")
file_handle4.write("Even MORE lines of text")

file_handle4.close()

file_handle5 =  open('NewTestFile.txt')
file_data2 = file_handle5.read()
file_handle.close()
print(file_data2)