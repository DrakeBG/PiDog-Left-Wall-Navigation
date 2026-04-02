import second

def one(number):
    return number - 9

def two(number):
    return number + 1

def three(number):
    return one(number) * two(number)

def four(number):
    return second.three(number)