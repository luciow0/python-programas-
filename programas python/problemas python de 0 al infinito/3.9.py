sueldo_trabajador = float(input("Ingrese su sueldo "))

if sueldo_trabajador < 8000:
    sueldo_aumentado_12 = sueldo_trabajador * 1.12
    aumento = sueldo_aumentado_12 - sueldo_trabajador

    print(f"su sueldo aumento de {sueldo_trabajador} a {sueldo_aumentado_12} el aumento fue de {aumento}")

elif sueldo_trabajador > 8000:
    sueldo_aumentado_8 = sueldo_trabajador * 1.8 
    aumento = sueldo_aumentado_8 - sueldo_trabajador

    print(f"su sueldo aumento de {sueldo_trabajador} a {sueldo_aumentado_8} el aumento fue de {aumento}")

