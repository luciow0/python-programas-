hectareas = float(input("che, guarda el goyete "))

yarda = hectareas * 10000 / 0.836

rod = yarda / 30.25

acre = rod / 160

homestad = acre / 160

milla = homestad / 4

print(f"El numero de yardas es {yarda:.2f} \n"
      f"El numero de rod es {rod:.2f} \n"
      f"El numero de acre es {acre:.2f} \n"
      f"El numero de homestad es {homestad:.2f} \n"
      f"El numero de millas es {milla:.2f} \n")