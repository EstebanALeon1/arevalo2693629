import random #se importa la funcion random 
tam=random.randint(5,10) #se define la fincion que determinara el tamaño de la lista y este sera un numero aleatorio de 5 a 10
lista=[random.randrange(100) for i in range(tam)] #se llena una lista por comprension donde se generan numeros aleatorios de 0 a 100 en el rango de tam 
print(lista) #se imprime la lista 

for i in range(len(lista)-1): #i en el rango len de lista - 1
    for j in range(i+1, tam): #j en el rango i+1 hasta tam
        if lista[i]<lista[i+1]: #compara lista en poscicion i con lista p
            lista[i],lista[i+1]=lista[i+1],lista[i] #se realiza el intercambio de los numeros en una sola linea no hacefalta utilizar una variable aux

print(lista) #se imprime la lista 
    
#in - not in #operadores in y not in para las listas

# for i in range(len(lista)): #i el el rango de len lista
#     print(lista[i]) #se imprimen todos los valores de lista 

for x in lista: #busca x en la lista
    print(x) #se imprime true si x esta en la lista y false si no esta 

if 10 not in lista: #busca 10 en la lista si no esta emite true si no esta en la lista y false si esta 
    print('no esta') #se imprime si el elemento no esta  
else:
    print('si esta') #se imprime si el elemento esta
    
 