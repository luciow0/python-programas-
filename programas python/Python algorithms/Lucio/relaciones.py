"""
El siguiente codigo pretende que, mediante el conjunto numerico ingresado por el usuario se permitan generar 
las relaciones de orden y equivalencia 
"""
#ESTE ALGORITMO GENERA EL ARREGLO PARA EL CONJUNTO INSTA 
def cargar_lista(): #func para cargar la lista
    n = int(input("Ingrese los elementos de el conjunto "))
    arr = [] #se genera un array preliminar
    while n != -1:
        arr.append(n)
        print(arr)
        n = int(input("Ingrese el siguiente elemento de el conjunto "))
    return arr 

## ESTE ALGORITMO GENERA UNA RELACION DE REFLEXION INSTA
def reflex(arr): #func reflex hace que la relacion cumpla la propiedad de relflexividad
    k = len(arr)
    R = [] # se genera el arreglo de la relacion 
    for i in range(k): # y se ingresan los elementos 
        aux = arr[i]
        aux_2 = aux
        paren = (aux, aux_2)
        R.append(paren)
        
    print(R)

## ESTE ALGORITMO GENERA UNA RELACION DE EQUIVALENCIA INSTA 
def equivalencia(arr):
    L = []
    n = len(arr) 
    for i in range(0, n):
        for j in range(0, n):
            aux = arr[i]
            aux_2 = arr[j]
            sim = (aux, aux_2)
            L.append(sim)
    print(L)

## ESTE ALGORITMO GENERA LA RELACION DE SIMETRIA INSTA 
def simetria(arr):
    n = len(arr)
    S = []
    for i in range(n):
        for j in range(n):
            if i != j:
                dos = (arr[i], arr[j])
                S.append(dos)
    print(S)



lol = cargar_lista()
#reflex(lol)
#equivalencia(lol)
simetria(lol)
