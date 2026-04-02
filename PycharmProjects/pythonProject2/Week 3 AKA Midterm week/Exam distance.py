def distnace_between(X1,Y1,X2,Y2):
    distance = (((X2 - X1) ** 2 + (Y2 - Y1) ** 2)) // 2
    return distance


X_first = 2
Y_first = 3
X_second = 7
Y_second = 8

Total = distnace_between(X_first,Y_first,X_second,Y_second)
print("The distance between is:",Total)