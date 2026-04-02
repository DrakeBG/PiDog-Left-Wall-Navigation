x = 27
for x in range (3, 101):
    for y in range (2, x):
        if x % y == 0:
            prime = 0
            break


if prime == 1:
    print("x is a prime number")

def IsPrime(x):
    prime = 1
    for y in range (2, x):
        if y % x == 0:
            prime = 0
            break
    if prime == 1:
        return (True)
    else:
        return (False)
