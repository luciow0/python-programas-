n1 = int(input("Ingrese un numero entero "))

while n1 <= 0:
    n1 = int(input("Ingrese un numero entero positivo "))
    
n2 = int(input("Ingrese un numero entero "))

while n2 <= 0:
    n2 = int(input("Ingrese un numero entero positivo "))

n3 = int(input("Ingrese un numero entero "))

while n3 <= 0:
    n3 = int(input("Ingrese un numero entero positivo "))


if n3 < n1 and n3 > n2:
    print("el numero esta ahi en el medio si")

elif n3 > n1 and n3 < n2:
    print("el numero esta ahi en el medio si")

else:
    print("el numero no esta no ")