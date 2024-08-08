nivel = int(input("ingrese su nivel "))

while nivel <= 0:
    nivel = int(input("Ingrese un nivel valido mayor a 0"))

sueldo = float(input("ingrese su sueldo en pesos "))

while sueldo <= 0:
    sueldo = float(input("Ingrese un sueldo valido mayor a 0"))

if nivel == 1:
    viejo_sueldo = sueldo
    sueldo = sueldo * 1.12

    print(f"felicitaciones su sueldo paso de {viejo_sueldo:.2f} a {sueldo:.2f}")

elif nivel == 2:
    viejo_sueldo = sueldo
    sueldo = sueldo * 1.08

    print(f"felicitaciones su sueldo paso de {viejo_sueldo:.2f} a {sueldo:.2f}")

elif nivel == 3:
    viejo_sueldo = sueldo
    sueldo = sueldo * 1.05

    print(f"felicitaciones su sueldo paso de {viejo_sueldo:.2f} a {sueldo:.2f}")

elif nivel == 4:
    viejo_sueldo = sueldo
    sueldo = sueldo * 1.035

    print(f"felicitaciones su sueldo paso de {viejo_sueldo:.2f} a {sueldo:.2f}")

else:
    print(f"su sueldo seguira siendo {sueldo:.2f}, manso seco")


