from math import pi
def circle(rad):
    area=pi*rad**2
    return area
r=int(input("Enter the radius of circle :"))
print("The area of circle is :",circle(r))
