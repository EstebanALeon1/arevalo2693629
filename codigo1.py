def numnat():
    maximo = int(input("introduce un numero maximo: "))
    suma = 0
    n = 1
    while suma < maximo:
        suma = suma + n
        n = n + 1
    return n 

lista = numnat()
print(f"El numero natural mas pequeño necesario para superar el maximo es: {lista}")