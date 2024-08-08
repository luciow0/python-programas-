num = int(input("ingrese un numero entero para determinar si es par o no "))

while num <= 0:
    num = int(input("Ingrese un numero entero positivo"))

if num % 2 == 0:
    print("numero par")

else:
    print("Numero impar")