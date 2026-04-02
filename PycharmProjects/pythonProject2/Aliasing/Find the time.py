def time_taken (dist):
    speed = 20
    timeTaken = (dist/speed)
    return (timeTaken)

location_1 = "Bethesda"
distance_1 = 10
time_1 =  time_taken(distance_1)
print(time_1)

def ValOfNumber (A, B, C):
    sum = (A + B + C)
    return sum
A1 = float(input())
B1 = float(input())
C1 = float(input())
Total = ValOfNumber(A1, B1, C1)
print(Total)