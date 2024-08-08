precioAd = float(input("ingrese el precio de la comida de adultos por kilo "))

precioCach = float(input("ingrese el precio de la comida de cachorros por kilo "))

ad = 450 * precioAd / 1000 * 10  
med = 380 * precioAd / 1000 * 12
cach = 230 * precioCach / 1000 * 6

total = (ad + med + cach) * 30

print(f"el total para darle de comer a todos los perros durante un mes es de = {total:.2f}")