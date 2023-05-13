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
def TamañoLista():
    return int(input("digita el tamaño de la lista: "))
usuario_tamaño_lista = TamañoLista()
def LlenarArreglo(tam):
    lista=[random.randrange(100) for i in range(tam)]    
    return lista
lista_1 = LlenarArreglo(usuario_tamaño_lista)
print(f'la lista se lleno con los siguientes valores {lista_1}')



#b. Suma
def SumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum
print(f'La suma de todos los elementos de la lista es igual a {SumaLista(lista_1)}')


#c. Promedio
def PromedioLista(lista):
    return SumaLista(lista)/len(lista)
print(f'El promedio de la lista es {PromedioLista(lista_1)}')


#d. Mayor
def NumeroMayor(lista):
    num_mayor = -1
    for i in lista:
        if i > num_mayor:
            num_mayor = i
    return num_mayor
print(f'El numero mayor que esta en la lista es {NumeroMayor(lista_1)}')


#e. Menor
def NumeroMenor(lista):
    num_menor = 101
    for i in lista:
        if i < num_menor:
            num_menor = i
    return num_menor
print(f'El numero menor que esta en la lista es {NumeroMenor(lista_1)}')


#f. Ordenar ascendente (No perder el arreglo original; el del punto a)
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


#h. Moda
contador = 0
mayor = 0
def Moda(lista):
    OrdenarListaAscendente(lista)
    contador = 0
    mayor = 0
    for i in range(usuario_tamaño_lista):
        contador = 0
        for j in range(usuario_tamaño_lista):
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
Moda(lista_1)


#i. Mediana
def Mediana(lista):
    OrdenarListaAscendente(lista)
    mediana = 0
    if usuario_tamaño_lista % 2 == 0:
        mediana = round(((lista[(len(lista)//2)-1]) + (lista[(len(lista)//2)]))/2,2)
        print(f"La mediana de la lista es {mediana}")
    else:    
        mediana = lista[(len(lista)//2)]
        print(f"La mediana de la lista es {mediana}")
Mediana(lista_1)


#j. Buscar. Decir si encuentra el número, en qué posición(es) está, cuantas veces está
def BuscarNumero(lista):
    num_buscar = int(input("Digite el numero que desea buscar: "))
    contador = 0
    for i in range(len(lista)):
        contador = 0
        for j in range(len(lista)):
            if lista[i] == lista[j]:
                if lista[i] == num_buscar:
                    contador += 1
                print(f"el numero que desea buscar esta en la poscicion [{i}] y se repite {contador} veces")
BuscarNumero(lista_1)