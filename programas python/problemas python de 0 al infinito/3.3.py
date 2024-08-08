numero_de_sonidos_grillo = int(input("Ingrese el numero de sonidos por minuto "))

while numero_de_sonidos_grillo <= 0:
    numero_de_sonidos_grillo = int(input("Ingrese un valor positivo "))

temperatura = 10 + (numero_de_sonidos_grillo - 40) / 7

print(f"la temperatura es {temperatura:.2f} grados celcius ")
