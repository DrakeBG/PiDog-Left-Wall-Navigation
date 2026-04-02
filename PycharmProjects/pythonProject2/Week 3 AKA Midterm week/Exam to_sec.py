def to_sec(hours,minutes,seconds):
    to_min = hours * 60
    sec = to_min + minutes * 60
    total = sec + seconds
    return total

hours1 = int(input("Enter hours"))
minutes1 = int(input("Enter minutes"))
seconds1 = int(input("Enter seconds"))

Total_sec = to_sec(hours1,minutes1,seconds1)
print(Total_sec)