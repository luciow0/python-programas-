n = int(input("Ingrese la cantidad de numeros enteros que desea ingresar "))
suma = 0

for i in range(n):
    num = int(input("ingrese su numero entero "))
    suma+= num

print(f"la sunma de los numeros enteros es de {suma} y el promedio es {suma / num}")
