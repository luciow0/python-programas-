potencia = 0
intensidad = 0
voltaje = 0
resistencia = 0
liOP = []
cantOp = 0
n = len(liOP)


def leyDeOmh(potencia, intensidad, voltaje, resistencia):

    calcular = input("¿que deseas calcular? potencia, intensidad, voltaje o resistencia ")

    while calcular != 'potencia' and calcular != 'intensidad' and calcular != 'voltaje' and calcular != 'resistencia':

        calcular = input("por favor ingrese un valor aceptado; potencia, intensidad, voltaje o resistencia ")
    
    ########################################################################################################################################
    #POTENCIA
    if calcular == 'potencia':

        valorP= input("¿que valores posee? a: voltaje e intensidad b: intensidad y resistencia c: voltaje y resistencia ")

        while valorP != 'a' and valorP != 'b' and valorP != 'c':

            valorP= input("por favor ingrese un valor aceptado; a: voltaje e intensidad b: intensidad y resistencia c: voltaje y resistencia ")
        
        cantOp = int(input("¿cuantas operaciones desea realizar? "))
            
        while cantOp < 1:
                
                cantOp = int(input("¿cuantas operaciones desea realizar? "))


        for i in range(0, cantOp):

            if valorP== 'a':
                print("ingrese los valores de voltaje e intensidad respectivamente ")
                voltaje = float(input("ingrese su voltaje: "))
                intensidad = float(input("ingrese su intensidad: "))

                resu = voltaje * intensidad

                liOP.append(resu)
        
                print("su potencia es: ", resu, "Watt")

            if valorP== 'b':
                print("ingrese los valores de intensidad y resistencia respectivamente ")
                intensidad = float(input("ingrese su intensdidad: "))
                resistencia = float(input("ingrese su resistencia: "))

                resu = (intensidad**2) * resistencia

                liOP.append(resu)
        
                print("su potencia es: ", resu, "Watt")

            if valorP== 'c':
                print("ingrese los valores de voltaje y resistencia respectivamente ")
                voltaje = float(input("ingrese su voltaje: "))
                resistencia = float(input("ingrese su resistencia: "))

                resu = (voltaje **2) / resistencia

                liOP.append(resu)
        
                print("su potencia es: ", resu, "Watt")

        print("aqui estan todos sus resultados ", liOP)



    #####################################################################################################################################
    #INTENSIDAD
    if calcular == 'intensidad':

        valorP= input("¿que valores posee? a: voltaje y resistencia b: potencia y voltaje c: potencia y resistencia ")

        while valorP != 'a' and valorP != 'b' and valorP != 'c':

            valorP= input("por favor ingrese un valor aceptado; a: voltaje y resistencia b: potencia y voltaje c: potencia y resistencia ")
        
        cantOp = int(input("¿cuantas operaciones desea realizar? "))
            
        while cantOp < 1:
                
                cantOp = int(input("¿cuantas operaciones desea realizar? "))


        for i in range(0, cantOp):

            if valorP== 'a':
                print("ingrese los valores de voltaje y resistencia respectivamente ")
                voltaje = float(input("ingrese su voltaje: "))
                resistencia = float(input("ingrese su resistencia: "))

                resu = voltaje / resistencia

                liOP.append(resu)
        
                print("su intensidad es: ", resu, "Amperios")

            if valorP== 'b':
                print("ingrese los valores de potencia y voltaje respectivamente ")
                potencia = float(input("ingrese su potencia: "))
                voltaje = float(input("ingrese su voltaje: "))

                resu = potencia / voltaje

                liOP.append(resu)
        
                print("su intensidad es: ", resu, "Amperios")

            if valorP== 'c':
                print("ingrese los valores de potencia y resistencia respectivamente ")
                potencia = float(input("ingrese su potencia: "))
                resistencia = float(input("ingrese su resistencia: "))

                resu = (potencia / resistencia)**0.5

                liOP.append(resu)
        
                print("su intensidad es: ", resu, "Amperios")

        print("aqui estan todos sus resultados ", liOP)

    ########################################################################################################################################
    #VOLTAJE
    if calcular == 'voltaje':

        valorP= input("¿que valores posee? a: potencia y resistencia b: potencia e intensidad c: intensidad y resitencia ")

        while valorP != 'a' and valorP != 'b' and valorP != 'c':

            valorP= input("por favor ingrese un valor aceptado; a: potencia y resistencia b: potencia e intensidad c: intensidad y resitencia ")
        
        cantOp = int(input("¿cuantas operaciones desea realizar? "))
            
        while cantOp < 1:
                
                cantOp = int(input("¿cuantas operaciones desea realizar? "))


        for i in range(0, cantOp):

            if valorP== 'a':
                print("ingrese los valores de potencia y resistencia respectivamente ")
                potencia = float(input("ingrese su potencia: "))
                resistencia = float(input("ingrese su resistencia: "))

                resu = (potencia * resistencia)**0,5

                liOP.append(resu)
        
                print("su voltaje es: ", resu, "Voltios")

            if valorP== 'b':
                print("ingrese los valores de potencia e intensidad respectivamente ")
                potencia = float(input("ingrese su potencia: "))
                intensidad = float(input("ingrese su intensidad: "))

                resu = potencia / intensidad

                liOP.append(resu)
        
                print("su voltaje es: ", resu, "Voltios")

            if valorP== 'c':
                print("ingrese los valores de intensidad y resistencia respectivamente ")
                intensidad = float(input("ingrese su intensidad: "))
                resistencia = float(input("ingrese su resistencia: "))

                resu = intensidad * resistencia

                liOP.append(resu)
        
                print("su intensidad es: ", resu, "Voltios")

        print("aqui estan todos sus resultados ", liOP)
    
    ########################################################################################################################################
    #RESISTENCIA
    if calcular == 'resistencia':

        valorP= input("¿que valores posee? a: potencia e intensidad b: intensidad y voltaje c: voltaje y potencia ")

        while valorP != 'a' and valorP != 'b' and valorP != 'c':

            valorP= input("por favor ingrese un valor aceptado; a: potencia e intensidad b: intensidad y voltaje c: voltaje y potencia ")
        
        cantOp = int(input("¿cuantas operaciones desea realizar? "))
            
        while cantOp < 1:
                
                cantOp = int(input("¿cuantas operaciones desea realizar? "))


        for i in range(0, cantOp):

            if valorP== 'a':
                print("ingrese los valores de potencia e intensidad respectivamente ")
                potencia = float(input("ingrese su potencia: "))
                intensidad = float(input("ingrese su intensidad: "))

                resu = potencia / (intensidad**2)

                liOP.append(resu)
        
                print("su resistencia es: ", resu, "Ohmios")

            if valorP== 'b':
                print("ingrese los valores de intensidad y voltaje respectivamente ")
                intensidad = float(input("ingrese su intensdidad: "))
                voltaje = float(input("ingrese su voltaje: "))

                resu = intensidad / voltaje

                liOP.append(resu)
        
                print("su resistencia es: ", resu, "Ohmios")

            if valorP== 'c':
                print("ingrese los valores de voltaje y potencia respectivamente ")
                voltaje = float(input("ingrese su voltaje: "))
                potencia = float(input("ingrese su potencia: "))

                resu = (voltaje **2) / potencia

                liOP.append(resu)
        
                print("su resistencia es: ", resu, "Ohmios")

        print("aqui estan todos sus resultados ", liOP)





leyDeOmh(potencia, intensidad, voltaje, resistencia)