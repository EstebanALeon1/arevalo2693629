import random #se importa la funcion random
lista=[] #creacion de una lista vacia
tam=int(random.randint(5,10)) #se define la fincion que determinara el tamaño de la lista y este sera un numero aleatorio de 5 a 10
#print(tam) #ae imprime tamaño
for i in range(tam): #se le asigna a i el rango de la variable tam
    num=int(random.randrange(100)) #se le asigna a num un numero aleatorio de 0 a 100
    lista.append(num) #se agrega al final de la lista el numero generado en num
    
print(lista) #se imprime la lista con los nuevos valores

for i in range(tam): #asignacion de i el rango de tam 
    for j in range(i+1,tam): #asignacion de j el raango que empieza en i+1 y termina en tam
        if lista[i]>lista[j]: #se realiza un condicional dice si la lista en la poscicion i es mayor que lista en la poscicion j 
            aux=lista[i] #se guarda lista en la poscicion i en una variable auxiliar esto nos ayudara que no se pierda este valor cuando asignemos lista en la poscicion j en lista en la poscicion i 
            lista[i]=lista[j] #se le asigna lista en la poscicion j a lista en la poscicion i esto hara un intercambio de numeros 
            lista[j]=aux #se le asigna el valor inicial de lista en la poscicion i que actualmente esta almacenada en la variable aux 

print(lista) #se imprime la lista organizados de menor a mayor 

for i in range(tam): #i en el rango tam
    for j in range(i+1,tam): #asignacion de j el raango que empieza en i+1 y termina en tam
        if lista[i]<lista[j]: #se realiza un condicional dice si la lista en la poscicion i es mernir que lista en la poscicion j
            aux=lista[i] #se guarda lista en la poscicion i en una variable auxiliar esto nos ayudara que no se pierda este valor cuando asignemos lista en la poscicion j en lista en la poscicion i
            lista[i]=lista[j] #se le asigna lista en la poscicion j a lista en la poscicion i esto hara un intercambio de numeros
            lista[j]=aux #se le asigna el valor inicial de lista en la poscicion i que actualmente esta almacenada en la variable aux      

print(lista) #se imprime la lista en orden descendente

x,y=10,20 #asignacion de 2 variables en una misma linea