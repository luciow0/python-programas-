def factorial_number (n):
    i = 1
    factorial = 1
    while i <= n:
        factorial *= i
        i += 1 
        print("la i vale ", i, "factorial vale ",factorial) 
    return factorial

def repeticiones_factorial():
    r = int(input("Ingrese sus r, -1 para finalizar "))
    prod = 1
    while r != -1: 
        aux = factorial_number(r)
        prod *= aux 
        print("prod en cata iteracion", prod)
        r = int(input("Ingrese sus r, -1 para finalizar "))
    return prod

def calcular_perm_con_rep():
    m = int(input("ingrese su N "))
    m = factorial_number(m)
    prod = repeticiones_factorial()
    resu = m / prod
    return(resu)


invocar = calcular_perm_con_rep()

print(invocar)