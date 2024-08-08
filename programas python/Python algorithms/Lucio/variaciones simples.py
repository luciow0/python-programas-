def factorial_number (n):
    i = 1
    factorial = 1
    while i <= n:
        factorial *= i
        i += 1 
        print("la i vale ", i, "factorial vale ",factorial) 
    return factorial

def variar_con_rep(n, r):
    aux = n - r 
    n = factorial_number(n)
    aux = factorial_number(aux)
    resu = n / aux
    print(resu)

variar_con_rep(30, 3)