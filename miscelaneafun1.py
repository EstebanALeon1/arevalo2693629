#Llenar un arreglo de n elementos con números generados con la función random. N es ingresado por el usuario. 
# Diseñe un menú con las siguientes operaciones.
#a. Imprimir arreglo original (El primero que se generó)
#b. Suma
#c. Promedio
#d. Mayor
#e. Menor
#f. Ordenar ascendente (No perder el arreglo original; el del punto a)
#g. Ordenar descendente (No perder el arreglo original; el del punto a)
#h. Moda
#i. Mediana
#j. Buscar. Decir si encuentra el número, en qué posición(es) está, cuantas veces está


#Llenar un arreglo de n elementos con números generados con la función random. N es 
#ingresado por el usuario.
import random
def LlenarArreglo(tam):
    lista=[random.randrange(100) for i in range(tam)]    
    return lista
lista_1 = LlenarArreglo(int(input("Digite el tamaño de la lista: ")))
print(lista_1)


#b. Suma
def SumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum
print(SumaLista(lista_1))


#c. Promedio
def PromedioLista(lista):
    return SumaLista(lista)/len(lista)
print(PromedioLista(lista_1))


#d. Mayor
def NumeroMayor(lista):
    num_mayor = -1
    for i in lista:
        if i > num_mayor:
            num_mayor = i
    return num_mayor
print(NumeroMayor(lista_1))


#e. Menor
def NumeroMenor(lista):
    num_menor = 101
    for i in lista:
        if i < num_menor:
            num_menor = i
    return num_menor
print(NumeroMenor(lista_1))


#f. Ordenar ascendente (No perder el arreglo original; el del punto a)
def OrdenarListaAscendente(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista
print(OrdenarListaAscendente(lista_1))


#g. Ordenar descendente (No perder el arreglo original; el del punto a)
def OrdenarListaDescendente(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]<lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista
print(OrdenarListaDescendente(lista_1))


#h. Moda