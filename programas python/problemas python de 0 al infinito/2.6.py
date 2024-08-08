import math 

radio = float(input("ingrese su radio "))

area = (4 * math.pi * radio) ** 2

volumen = (1 / 3 * math.pi * radio) ** 3

print(f"el area de su circulo es {radio:.2f}")

print(f"el volumen de su circulo es {volumen:.2f}")