##falta acomodar la regla de 3




pan = 0
rodajasDeTomate = 0
rodajasDelechuga = 0
rodajasDeCebolla = 0
rodajasDeMorron = 0
rodajasDeJamon = 0
rodajasDeQueso = 0
aderesoElejido = 0

def calcularSanguche():

    pan = float(input("ingrese la medida del pan"))

#########################################################################################
     
    tomate = input("desea agregar tomate? 1 para si, -1 para no")

    if tomate == '1':
        rodajasDeTomate = 3 * 100 /pan
    
    else: 
        print("perfecto! sigamos")

#########################################################################################
    
    lechuga = input("desea agregar lechuga? 1 para si, -1 para no")

    if lechuga == '1':
        rodajasDeLechuga = 2 * 100 /pan
    
    else: 
        print("perfecto! sigamos")

#########################################################################################

    cebolla = input("desea agregar aros de cebolla? 1 para si, -1 para no")

    if cebolla == '1':
        rodajasDeCebolla = 7 * 100 /pan
    
    else: 
        print("perfecto! sigamos")

#########################################################################################        

    morron = input("desea agregar aros de morron? 1 para si, -1 para no")

    if morron == '1':
        rodajasDeMorron = 5 * 100 /pan
    
    else: 
        print("perfecto! sigamos")

#########################################################################################
    
    jamon = input("desea agregar fetas de jamon? 1 para si, -1 para no")

    if jamon == '1':
        rodajasDeJamon = 2 * 100 /pan
    
    else: 
        print("perfecto! sigamos")

#########################################################################################

    queso = input("desea agregar fetas de queso? 1 para si, -1 para no")

    if queso == '1':
        rodajasDeQueso = 3 * 100 /pan
    
    else: 
        print("perfecto! sigamos")
    
#########################################################################################

    adereso = input("desea agregar adereso? 1 para si, -1 para no")

    if adereso == '1':
        
        aderesoElejido = input("que adereso desea agregar? 1 para mayonesa, 2 para ketchup, 3 para mostaza")

        if aderesoElejido == '1':

            aderesoElejido = 2 * 100 /pan
        
        if aderesoElejido == '2':

            aderesoElejido = 2 * 100 /pan

        if aderesoElejido == '3':
            
            aderesoElejido = 2 * 100 /pan

     
    print("la configuracion esta lista! ", "largo del pan: ", pan,"cm", "rodajas de tomate:", rodajasDeTomate, "hojas de lechuga:", rodajasDelechuga , "aros de cebolla: ", rodajasDeCebolla, "aros de morron: ", rodajasDeMorron, "fetas de jamon: ", rodajasDeJamon, "fetas de queso: ", rodajasDeQueso, "cucharadas de adereso: ", aderesoElejido)

##########################################################################################

    #print("la configuracion esta lista! ", "largo del pan: ", pan,"cm", "rodajas de tomate:", rodajasDeTomate, "hojas de lechuga:", rodajasDelechuga , "aros de cebolla: ", rodajasDeCebolla, "aros de morron: ", rodajasDeMorron, "fetas de jamon: ", rodajasDeJamon, "fetas de queso: ", rodajasDeQueso, "cucharadas de adereso: ", aderesoElejido)

   
calcularSanguche()


