modelo = str(input("Ingrese el modelo de su auto "))

modelo = modelo.capitalize()

precio = float(input("Ingrese el precio de su vehiculo "))

if modelo == "Serie 1":
    precio_final = (precio * 0.97) - 20000
    print(f"Su auto {modelo} con un precio inicial de {precio:.2f} gracias al descuento + bono le sale {precio_final:.2f}")

elif modelo == "Serie 3":
    precio_final = (precio * 0.95) - 35000
    print(f"Su auto {modelo} con un precio inicial de {precio:.2f} gracias al descuento + bono le sale {precio_final:.2f}")

elif modelo == "Serie 4":
    precio_final = (precio * 0.95) - 35000
    print(f"Su auto {modelo} con un precio inicial de {precio:.2f} gracias al descuento + bono le sale {precio_final:.2f}")

elif modelo == "Serie 5":
    precio_final = (precio * 0.95) - 60000
    print(f"Su auto {modelo} con un precio inicial de {precio:.2f} gracias al descuento + bono le sale {precio_final:.2f}")

elif modelo == "Serie X1":
    precio_final = (precio * 0.95) - 30000
    print(f"Su auto {modelo} con un precio inicial de {precio:.2f} gracias al descuento + bono le sale {precio_final:.2f}")

elif modelo == "Serie X3":
    precio_final = (precio * 0.93) - 50000
    print(f"Su auto {modelo} con un precio inicial de {precio:.2f} gracias al descuento + bono le sale {precio_final:.2f}")

elif modelo == "Serie X5":
    precio_final = (precio * 0.91) - 70000
    print(f"Su auto {modelo} con un precio inicial de {precio:.2f} gracias al descuento + bono le sale {precio_final:.2f}")

else:
    print(f"su auto de mierda {modelo} sigue costando {precio}")    
    