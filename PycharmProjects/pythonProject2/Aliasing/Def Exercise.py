def Rectangle( length, breadth, cost = 10): #Cost is automaticlly 10
    area = length*breadth
    cost = cost*area
    return cost

length1 = int(input("Enter length:"))
breadth1 = int(input("Enter breadth/width:"))
cost1 = int(input("Enter cost:")) #Entering a cost takes away the 10

Total1 = Rectangle(length1, breadth1, cost1) #With entered cost
print("The cost of the rectangle is:", Total1)

Total2 = Rectangle(length1, breadth1) #With default cost of 10
print("The area of the rectagle is:", Total2)