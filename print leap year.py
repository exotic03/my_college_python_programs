print("Leap years from 1900 to 2023")
for i in range(1900,2024):
    if(i%4==0 and i%100!=0) or (i%400==0):
        print(i)
