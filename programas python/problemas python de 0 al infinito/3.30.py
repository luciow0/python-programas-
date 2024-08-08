try:
    numero = int(input("Ingrese un numero entero de 3 cifras "))
 
except ValueError:
    print("error, ingrese un numero entero")
    numero = int(input("Ingrese un numero entero de 3 cifras"))


"""
while numero[3] is not None:
    numero =str(input("se suponia que debia ingresar solo un numero de 3 cifras. ingrese un numero entero de 3 cifras"))
"""

numero = str(numero)

a = numero[0]
b = numero[1]
c = numero[2]

num_entero_1 = int(a)
num_entero_2 = int(b)
num_entero_3 = int(c)
numero_entero = int(numero)

if numero_entero == (num_entero_1 ** 3) + (num_entero_2 ** 3) + (num_entero_3 ** 3):
    print("el numero cumple con la condicion abc = a ** 3 + b ** 3 + c ** 3")
else:
    print("el numero no cumple con la condicion abc = a ** 3 + b ** 3 + c ** 3")


'''
me acabo de pasar la progrmacion buenas noches
no se si me pase la programacion pq puede meter letras el hdp
che posta no se si me pase la programacion 
creo que definitivamente no me pase nada
ahora si me la pase anazi


'''


