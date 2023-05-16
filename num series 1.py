n = int(input("Enter the nth term: "))
sum = 0

for i in range(1, n+1):
    sum += 1/i
    print("1/",i, end="")
    if i < n:
        print(" + ", end="")

print("\nSum of the series: ", round(sum, 2))
