monto_de_compra = float(input("Ingrese el monto de su compra "))

while monto_de_compra <= 0:
    monto_de_compra = float(input("Ingrese un monto de compra valido "))

if monto_de_compra > 8000:

    monto_de_compra_con_descuento_aplicado = monto_de_compra / 1.15

    print(f"El importe a abonar es de ${monto_de_compra:.2f}, con su correspondiente descuento debe abonar {monto_de_compra_con_descuento_aplicado:.2f}")

else:
    print(f"el importe a abonar es de ${monto_de_compra:.2f}")