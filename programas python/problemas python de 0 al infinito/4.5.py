n = int(input("ingrese un numero entero "))
suma = 0

for i in range(n):
    suma += 1 / i

print(f"el resultado de la serie es de {suma:.2f}")