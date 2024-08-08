import math

x1 = float(input("ingrese su coordenada x1 "))
x2 = float(input("ingrese su coordenada x2 "))
y1 = float(input("ingrese su coordenada y1 "))
y2 = float(input("ingrese su coordenada y2 "))

distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print(f"la distancia entre los puntos es = {distancia:.2f}")


