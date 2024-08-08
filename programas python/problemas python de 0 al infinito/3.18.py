clave = int(input("Ingrese su calve telefonica "))
minutos = float(input("Ingrese la cantidad de minutos de su llamada telefonica"))

if clave == 12:
    coste = minutos * 10

elif clave == 15:
    coste = minutos *8

elif clave == 21:
    coste = minutos *8

elif clave == 23:
    coste = minutos *8

elif clave == 29:
    coste = minutos *8

else: 
    coste = 0
    print("Clave incorrecta")


if coste > 0:
    print("El coste de su llamada telefonica es de: ", coste)