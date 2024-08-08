import math

k = int(input("Ingrese su numero entero k"))
x = float(input("Ingrese su numero real x"))

if k == 1:
    fx = x/5

    print(fx)

if k == 2 or k == 3:
    fx = x ** 2

    print(fx)

if k == 4:
    fx = x ** 3 + 5

    print(fx)

else:
    fx = math.sqrt(5)

    print(fx)

