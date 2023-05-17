#Ordenar el arreglo, de mayor a menor y de menor a mayor (algoritmo de la burbuja)
import random
lista_1 = [random.randrange(100) for i in range(random.randint(5, 15))]
print(lista_1)
def OrdenarListaAscendente(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista
print(f'La lista ordenada de forma ascendente es {OrdenarListaAscendente(lista_1)}')


#g. Ordenar descendente (No perder el arreglo original; el del punto a)
def OrdenarListaDescendente(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]<lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista
print(f'La lista ordenada de forma descendente es {OrdenarListaDescendente(lista_1)}')
