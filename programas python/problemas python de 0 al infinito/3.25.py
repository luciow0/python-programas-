sueldo = float(input("ingrese su sueldo "))
años = int(input("ingrese sus años de antiguedad "))

if años <= 10:
    bono_anual = (sueldo * 0.06) * años
    print(f"su bono anual es de {bono_anual}")

if años <= 20:
    bono_anual = (sueldo * 0.065) * años
    print(f"su bono anual es de {bono_anual}")

if años <= 30:
    bono_anual = (sueldo * 0.07) * años
    print(f"su bono anual es de {bono_anual}")

if años > 30:
    bono_anual = (sueldo * 0.07) * años + (sueldo * 0.22)
    print(f"su bono anual es de {bono_anual}")



