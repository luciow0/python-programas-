import math

try:
    x = float(input("INGRESE SU VALOR PARA X"))

except ValueError:
    x = float(input("por favor ingrese un valor numerico"))



if x % 4 == 0:
    fx = 25 / x
    print(fx)

if x % 4 == 1:
    fx = x ** 2 
    print(fx)

if x % 4 == 2:
    fx = 2 * x + math.sqrt(x)
    print(fx)

if x % 4 == 3:
    fx = 7 * x - x ** 2
    print(fx)

