def square(x):
    if (x >= 1 and x <= 10):
        x = x ** 2
        return True
add = filter(square, range(1, 11))
sum = 0
for i in add:
    sum += i ** 2
print(sum)
