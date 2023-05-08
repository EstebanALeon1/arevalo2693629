import random #ae importa la funcion random 
lista=[] #se crea una lista vacia
tam=int(random.randint(10,20)) #tam va a ser un entero generado aleatoriamente de 10 a 20
print(tam) #se imprime tam
for i in range(tam): #se ejecuta for mientras este en el rango tam
    num=int(random.randrange(100)) #num es un numero entero aleatorio de 0 a 100
    lista.append(num) #se agrega num a la lista con el metodo append 

print(lista) #se imprime la lista 