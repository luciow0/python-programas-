import math


x1 = float(input("ingrese el valor de x1 "))
y1 = float(input("ingrese el valor de y1 "))
x2 = float(input("ingrese el valor de x2 "))
y2 = float(input("ingrese el valor de y2 "))
x3 = float(input("ingrese el valor de x3 "))
y3 = float(input("ingrese el valor de y3 "))

area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))  

print(f"el area de su triangulo es {area:.2f}")