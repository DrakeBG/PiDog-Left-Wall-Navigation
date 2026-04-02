alphabet_list ="ATCTCATCTACTATCTACGGG"
A_count = 0
C_count = 0
G_count = 0
T_count = 0
for str in alphabet_list:
    if str == "A":
        A_count += 1
    elif str == "C":
        C_count += 1
    elif str == "G":
        G_count += 1
    elif str == "T":
        T_count += 1

print("How many As:",A_count)
print("How many Cs:",C_count)
print("How many Gs:",G_count)
print("How many Ts:",T_count)