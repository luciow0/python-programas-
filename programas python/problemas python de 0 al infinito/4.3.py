n = int(input("Ingrese la cantidad de numeros que desea ingresar"))

suma = 0
cant_impar = 0
total_impar = 0

for i in range (n):

    num = int(input("ingrese su numero"))

    if num % 2 == 0:
        suma+= num

    elif num % 2 == 1:
        cant_impar += 1
        total_impar += num



if suma > 0:
    print(f"la suma de los numeros pares es de {suma}")

else: 
    print("no hay numeros pares para sumar")

if cant_impar > 0:
    print(f"el promedio de los numeros impares es de {total_impar / cant_impar}")

else:
    print("no hay numeros impares para realizar dicho promedio")