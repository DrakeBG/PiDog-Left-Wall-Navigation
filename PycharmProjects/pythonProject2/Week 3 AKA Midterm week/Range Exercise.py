for x in range(3,303): #How many 4s or 7s are in the range
    if (x % 4 ==0) or (x % 7 ==0):
        print("Buzz")
    else:
        print("Not Buzz")

Str1 = "This is American University"
A_count = 0
E_count = 0
I_count = 0
U_count = 0
for x in Str1:
    if x == "a" or x == "A":
        A_count += 1
    elif x == "e" or x == "E":
        E_count += 1
    elif x == "i" or x == "I":
        I_count += 1
    elif x == "u" or x == "U":
        U_count += 1

print("How many As:",A_count)
print("How many Es:",E_count)
print("How many Is:",I_count)
print("How many Us:",U_count)