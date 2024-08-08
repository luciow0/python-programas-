base = float(input("ingrese el costo base de la pintura "))
tecnica = str(input("ingrese la tecnica con la que fue realizada "))

tecnica = tecnica.lower()

if tecnica == "oleo":
    precio = base * 1.25

elif tecnica == "acuarela":
    precio = base * 1.20 

elif tecnica == "gouache":
    precio = base * 1.18

else:
    precio = base * 1.10

print(f"el precio de su obra sera {precio:.2f}")