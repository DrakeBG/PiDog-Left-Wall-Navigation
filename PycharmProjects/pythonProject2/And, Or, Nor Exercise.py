num = float(input("Enter number:"))

if (num % 5 == 0) or (num % 7 == 0):
    print("You are a winner")

if ((num % 5 == 0) or (num % 7 == 0)) and (num % 8 == 0):
    print("You are a super winner")
