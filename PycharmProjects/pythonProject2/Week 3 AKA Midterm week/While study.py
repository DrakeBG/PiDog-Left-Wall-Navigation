num = int(input("enter number"))
while num > 0:
    if num > 13:
        print("The number is too large")
        break #Break stops "while" code from endlessly looping
    elif num < 13:
        print("The number is too small")
        break
    elif num == 13:
        print("congraulation")
        break