sueldo = float(input("ingrese su sueldo "))
categoria = int(input("ingrese su categoria "))
horas_extra = int(input("ingrese la cantidad de horas extra "))

if categoria == 1:
    precio_hora = 120
    if horas_extra < 30:
        horas_extra = 30
        sueldo_bonificado = sueldo + (horas_extra * precio_hora)
        print(f"su sueldo bonificado es de {sueldo_bonificado}")
    else:
        sueldo_bonificado = sueldo + (horas_extra * precio_hora)
        print(f"su sueldo bonificado es de {sueldo_bonificado}")

if categoria == 2:
    precio_hora = 150
    if horas_extra < 30:
        horas_extra = 30
        sueldo_bonificado = sueldo + (horas_extra * precio_hora)
        print(f"su sueldo bonificado es de {sueldo_bonificado}")
    else:
        sueldo_bonificado = sueldo + (horas_extra * precio_hora)
        print(f"su sueldo bonificado es de {sueldo_bonificado}")

if categoria == 3:
    precio_hora = 195
    if horas_extra < 30:
        horas_extra = 30
        sueldo_bonificado = sueldo + (horas_extra * precio_hora)
        print(f"su sueldo bonificado es de {sueldo_bonificado}")
    else:
        sueldo_bonificado = sueldo + (horas_extra * precio_hora)
        print(f"su sueldo bonificado es de {sueldo_bonificado}")

if categoria == 4:
    precio_hora = 245
    if horas_extra < 30:
        horas_extra = 30
        sueldo_bonificado = sueldo + (horas_extra * precio_hora)
        print(f"su sueldo bonificado es de {sueldo_bonificado}")
    else:
        sueldo_bonificado = sueldo + (horas_extra * precio_hora)
        print(f"su sueldo bonificado es de {sueldo_bonificado}")

