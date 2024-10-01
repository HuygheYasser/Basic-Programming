from math import sqrt

a = float(input("enter length of side a: "))
b = float(input("enter length of side b: "))
c = float(input("enter length of side c: "))

s = float(1/2*(a + b + c))

area = sqrt(s*(s-a)*(s-b)*(s-c))



print(f"The surface area is {round(area,2)} cm³")