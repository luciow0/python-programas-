def simetria():
    n = len(arr)
    for i in range(0, n):
        x = 1
        for j in range(0, n-1):
            if x ==  n - 1:
                x = 0
            if x == i:
                x +=1
            aux = arr[i]
            aux_2 = arr[x]
            dos = (aux, aux_2)
            R.append(dos)
            x += 1
    print(R)

