#Funciones

def asignarSlots(cantidades):
    slot = 0
    n= len(cantidades)
    for i in range(n):

        if cantidades[i] > 64:
            resu = cantidades[i] // 64
            slot += resu
        else: 
            slot+= 1

    return slot

bloques = []
cantidades = []

#Programa

tipoBloque = input("Ingrese que tipo de bloque desea cargar, -1 para finalizar ")

while tipoBloque == '':

    tipoBloque = input("Ingrese un bloque, -1 para finalizar ")

while tipoBloque != '-1':
    bloques.append(tipoBloque)

    cantidadBloque = int(input("ingrese la cantidad deseada del bloque "))
    while cantidadBloque < 1:
        cantidadBloque = int(input("no son aceptados valores vacios ingrese su cantidad "))
    cantidades.append(cantidadBloque)

    tipoBloque = input("ingrese su otro bloque, -1 para finalizar ")   


for j in range (0, len(cantidades)):
    
    print(bloques[j], cantidades[j]) 


slut = asignarSlots(cantidades)

print("cantidad de slots necesaria ", slut, "es decir ", slut // 54, "cofres dobles", "o", slut // 27, "shulkerbox")
