#def cargar_lista(): #func para cargar la lista
 #   n = int(input("Ingrese los elementos de el conjunto "))
  #  arr = [] #se genera un array preliminar
   # while n != -1:
    #    arr.append(n)
     #   print(arr)
      #  n = int(input("Ingrese el siguiente elemento de el conjunto "))
   # return transitividad(arr) 

def transitividad():
    arr = [(1,2), (1,3), (1,7), (1,8)] 
    n = len(arr)
    R = []
    for i in range(0,n):
        aux = arr[i]
        x = aux[0]
        for j in range(1,n): 
            if x in arr[j]:
                aux_2 = arr[j]
                if x != aux_2[0]:
                    R.append(aux_2[0])
                
                else: 
                    R.append(aux_2[1])
                
                print(R, i)
transitividad()
