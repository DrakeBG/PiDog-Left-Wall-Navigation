sentence = "I am a student at American University located in Washington DC"
sentence2 = "It’s mascot is Clawed Z. Eagle"
A_count = 0
E_count = 0
I_count = 0
O_count = 0
U_count = 0
for str in sentence:
    if str == "A" or str == "a":
        A_count += 1
    elif str == "E" or str == "e":
        E_count += 1
    elif str == "I" or str == "i":
        I_count += 1
    elif str == "O" or str == "o":
        O_count += 1
    elif str == "U" or str == "u":
        U_count += 1

for str in sentence2:
    if str == "A" or str == "a":
        A_count += 1
    elif str == "E" or str == "e":
        E_count += 1
    elif str == "I" or str == "i":
        I_count += 1
    elif str == "O" or str == "o":
        O_count += 1
    elif str == "U" or str == "u":
        U_count += 1
print("All the As in the sentences:",A_count)
print("All the Es in the sentence:",E_count)
print("All the Is in the sentence:",I_count)
print("All the Os in the sentence:",O_count)
print("All the Us in the sentence:",U_count)