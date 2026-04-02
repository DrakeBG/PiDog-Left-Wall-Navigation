perfect_numbers = []
for num in range (1,10000):
    divisors = []
    for divis in range(1,num):
        if num % divis ==0:
            divisors.append(divis)
    if num == sum(divisors):
        perfect_numbers.append(num)
print(perfect_numbers)


