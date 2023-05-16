from math import pi
def arpe(r):
    return (pi*r*r,2*pi*r)
r=float(input("Enter the number " ))
(area,cir)=arpe(r)
print("Area is ",area)
print("Circumference is ",cir)
