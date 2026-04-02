import first

def one(number):
    return number ** 2

def two(number):
    return number * 3

def three(number):
    return one(number) - two(number)

print(three(2))
print(first.three(2))
print(first.four(2))