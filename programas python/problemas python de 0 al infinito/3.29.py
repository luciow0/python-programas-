destino = str(input("Ingrese el destino hacia el cual quiere viajar: playa, ciudades coloniales, zonas arequeologicas "))
paquete = str(input("Ingrese el paquete que desea elegir: exclusivo, lujo, estandar "))
dias = int(input("Ingrese la cantidad de dias que desea alojarse "))

destino = destino.lower()
paquete = paquete.lower()

if destino == "playa":
    destino = 1200
    if paquete == "exclusivo":
        destino = destino * 1.30

    if paquete == "lujo":
         destino = destino * 1.10


    if dias > 10:
            destino = destino * 0.92
            print(f"El valor de su viaje sera de {destino * dias:.2f}")
    else:
            print(f"El valor de su viaje sera de {destino * dias:.2f}")



if destino == "ciudades coloniales":
    destino = 1000
    if paquete == "exclusivo":
        destino = destino * 1.30

    if paquete == "lujo":
         destino = destino * 1.10
    

    if dias > 10:
            destino = destino * 0.92
            print(f"El valor de su viaje sera de {destino * dias:.2f}")
    else:
            print(f"El valor de su viaje sera de {destino * dias:.2f}")


if destino == "zonas arqueologicas":
    destino = 900
    if paquete == "exclusivo":
        destino = destino * 1.30

    if paquete == "lujo":
         destino = destino * 1.10
    

    if dias > 10:
            destino = destino * 0.92
            print(f"El valor de su viaje sera de {destino * dias:.2f}")
    else:
            print(f"El valor de su viaje sera de {destino * dias:.2f}")
            


