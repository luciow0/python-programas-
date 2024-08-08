def factorial_number (n):
    i = 1
    factorial = 1
    while i <= n:
        factorial *= i
        i += 1 
        print("la i vale ", i, "factorial vale ",factorial) 
    return factorial

factorial_number(10)