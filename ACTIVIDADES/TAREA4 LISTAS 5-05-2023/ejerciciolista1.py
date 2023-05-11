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


#como se implementa moda, mediana y desviacion estandar
#moda
contador = 0
mayor = 0
for i in range(tam):
    contador = 0
    for j in range(tam):
        if lista[i] == lista[j]:
            contador += 1
    if contador > mayor:
        mayor = contador
        moda = lista[i]
    elif mayor<=1:
        moda = 0
if moda != 0:
    print('la moda es ', moda)
else:
    print('no hay moda en esta lista ya que ningun numero se repite')


#mediana
mediana = 0
def OrdenarListaAscendente(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista
print(f"lista ordenada de forma ascendente {OrdenarListaAscendente(lista)}")

if tam % 2 == 0:
    mediana = round(((lista[(len(lista)//2)-1]) + (lista[(len(lista)//2)]))/2,2)
    print(f"La mediana de la lista es {mediana}")
else:
    mediana = lista[(len(lista)//2)-1]
    print(f"La mediana de la lista es {mediana}")