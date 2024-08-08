edad = int(input("Ingrese la edad del paciente "))
enfermedad = int(input("Ingrese el tipo de enfermedad del paciente "))
dias = int(input("Ingrese la cantidad de dias que el paciente estara internado "))
importe = 0

"""
1 3,150
2 3,980
3 5,500
4 7,150
"""
if enfermedad == 1:
    if edad < 16:
        importe = dias * (3.150 * 1.08)
        print(f"el importe a pagar es de {importe:.2f}")
    elif edad > 70:
        importe = dias * (3.150 * 1.17)
        print(f"el importe a paga es de {importe:.2f}")
    else:
        importe = dias * 3.150
        print(f"el importe a pagar es de {importe:.2f}")


if enfermedad == 2:
    if edad < 16:
        importe = dias * (3.980 * 1.08)
        print(f"el importe a pagar es de {importe:.2f}")
    elif edad > 70:
        importe = dias * (3.980 * 1.17)
        print(f"el importe a paga es de {importe:.2f}")
    else:
        importe = dias * 3.980
        print(f"el importe a pagar es de {importe:.2f}")


if enfermedad == 3:
    if edad < 16:
        importe = dias * (5.500 * 1.08)
        print(f"el importe a pagar es de {importe:.2f}")
    elif edad > 70:
        importe = dias * (5.500 * 1.17)
        print(f"el importe a paga es de {importe:.2f}")
    else:
        importe = dias * 5.500
        print(f"el importe a pagar es de {importe:.2f}")


if enfermedad == 4:
    if edad < 16:
        importe = dias * (7.150 * 1.08)
        print(f"el importe a pagar es de {importe:.2f}")
    elif edad > 70:
        importe = dias * (7.150 * 1.17)
        print(f"el importe a paga es de {importe:.2f}")
    else:
        importe = dias * 7.150
        print(f"el importe a pagar es de {importe:.2f}")

if enfermedad != 1 and enfermedad != 2 and enfermedad != 3 and enfermedad != 4: 
    print("la enfermedad ingresada no esta registrada en la base de datos")