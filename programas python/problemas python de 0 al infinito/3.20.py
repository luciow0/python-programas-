tipo = str(input("Ingrese el tipo de habitacion que desea reservar, S (simple) D (doble) T (triple) F(familiar) "))
tipo = tipo.upper()

dias = int(input("Ingrese la cantidad de dias que desea quedarse "))

if tipo == "S":
    coste = dias * 1500

elif tipo == "D":
    coste = dias * 2100

elif tipo == "T":
    coste = dias * 2700

elif tipo == "F":
    coste = dias * 3100

else:
    print("tipo de habitacion invalido!")

print(f"el costyo de su reserva sera de ${coste:.2f}")
