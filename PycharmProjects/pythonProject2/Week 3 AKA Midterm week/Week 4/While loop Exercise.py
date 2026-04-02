num = 1
total = 0

while num <= 100:
    num += 1
    total = total + num #Finding the sum of the numbers

print(total)

number = 6523198
digit = 1

while (number // 10) > 0: #Find how many digits are in the number
    number = number // 10
    digit += 1

print(digit)