# hacer la suma, el promedio, numero mayor, num menor de los numeros generados aleatoriamente 
import random
lista = []
tam = int(random.randint(10, 20))
print(tam)
suma = 0
num_mayor = -1
num_menor = 99999999
repeticion = 0
for i in range (tam):
    num = int(random.randrange(100))
    lista.append(num)
    print(lista.count(70))
    if i == num:
        repeticion += 1
    suma += num
    promedio = suma / tam
    if num > num_mayor:
        num_mayor = num
    if num < num_menor:
        num_menor = num    


print(lista)
print(f"La suma de los numeros generados en la lista es igual a {suma}")
print(f"el promedio de la suma de los numeros generados es igual a {promedio}")
print(f"el numero mayor generado en la lista es igual a {num_mayor}")
print(f"el numero menor generado en la lista es igual a {num_menor}")
print(lista.count(num))

#como se implementa moda, mediana y desviacion estandar
