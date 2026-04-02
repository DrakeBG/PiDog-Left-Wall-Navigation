a = 1
b = 1

fibonacci_list = []

while b < 10000:
    fibonacci_list.append(a)
    fibonacci_list.append(b)
    a = a + b
    b = b + a
print(fibonacci_list)
