layout = "{0:>4}:{1:>6}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}"
print(layout.format("",1,2,3,4,5,6))
print("    :--------------------------")

print(layout.format("1",1,2,3,4,5,6))
print(layout.format("2",2,4,6,8,10,12))
print(layout.format("3",3,6,9,12,15,18))

for i in range(1,7):
    print(layout.format(i,i*1,i*2,i*3,i*4,i*5,i*6))