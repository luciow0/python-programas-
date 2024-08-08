def factorial_number (n):
    i = 1
    factorial = 1
    while i <= n:
        factorial *= i
        i += 1 
        print("la i vale ", i, "factorial vale ",factorial) 
    return factorial

def combinatory(m,r): 
    aux_fact = m - r
    aux_fact = factorial_number(aux_fact) 
    m = factorial_number(m)
    r = factorial_number(r)
    combinatorio = m / (r * aux_fact) 
    print("numero combinatorio (n r) ", combinatorio)

    return combinatorio

combinatory(10, 5)



