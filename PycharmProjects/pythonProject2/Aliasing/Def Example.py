def Numbers(A,B,C,D,E):
    sum = (A + B + C + D + E)
    if (sum%2 == 0): #If the answer is even
        return sum**2

A1 = int(input("Enter number:"))
B1 = int(input("Enter number:"))
C1 = int(input("Enter number:"))
D1 = int(input("Enter number:"))
E1 = int(input("Enter number:"))
Total = Numbers(A1,B1,C1,D1,E1)
print(Total)