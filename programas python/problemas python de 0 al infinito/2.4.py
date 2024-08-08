"""import math es necesario para calcular la raiz cuadrada ya que esta no es posible en python sin utilizar una libreria o modulo"""

import math

lado_1 = float(input("ingrese su lado 1 "))
lado_2 = float(input("ingrese su lado 2 "))
lado_3 =float(input("ingrese su lado 3 "))

sp = (lado_1 + lado_2 + lado_3) / 2

area= math.sqrt(sp *(sp - lado_1) * (sp - lado_2) * (sp - lado_3))

print(f"el area del trinagulo es = {area:.2f}")

"""math.sqrt() para realizar la raiz cuadrada

   math.cbrt() para realizar raiz cubica
   
   dentro del parentesis se coloca el numero o el calculo al que se le quiere realizar la raiz"""