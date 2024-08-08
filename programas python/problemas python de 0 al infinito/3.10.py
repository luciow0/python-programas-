distancia = float(input("Ingres su distancia en km "))
dias = int(input("Ingrese la cantidad de dias  para el regreso "))

precio_pasaje = distancia * 1.9 * 2


if distancia * 2 > 500 and dias >= 10:
    precio_pasaje = precio_pasaje / 1.20

"""orta opcion era precio_pasaje = precio_pasaje * 0.80"""

print(f"el precio del pasaje es {precio_pasaje:.2f}$")