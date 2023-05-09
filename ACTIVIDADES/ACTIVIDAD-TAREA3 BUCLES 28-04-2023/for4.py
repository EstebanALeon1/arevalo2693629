for i in range(2, 1001):
    cont = 0
    for j in range(1 , i+1):
        if i % j == 0:
            cont+=1
    if cont == 2:
        print(f"el numero {i} es primo")
    else:
        print(f"el numero {i} no es primo")
        
        
        
