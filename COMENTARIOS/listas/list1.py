#[] {} () #diferentes signos con diferentes utilidades para python
x=100 #asignacion de una varibale 
print('tipo de x',type(x)) #se imprime el tipo de dato que es la variable x
lista=[1,1.4,'sena',['a','b',],'soacha'] #se crea una lista donde hay diferentes tipos de datos, incuso listas dentro de la lista
print(f'elemento {lista[4]}') #se imprime el elemento 4 de la lista que hace referencia a "soacha"
print(len(lista)) #cuenta los elementos de la lista con la funcion len 
print('tipo de lista',type(lista)) #se imprime el tipo de dato que es lista el cual es lista
print('ultimo indice',lista[-1]) #se utilizan valores negativos para un acceso mas rapido de los ultimos elementos de la lista este imprime "soacha"

print(len(lista)) #cuenta los elementos de la lista con la funcion len
lista.append(20) #metodo append que sirve para agregar elementos al final de la lista en este caso sera el numero 20
lista.append('python') #se agrega un nuevo elemento a la lista "python"
print(lista) #se imprime la lista 
lista.insert(len(lista),'java') #metodo insert el cual nos sirve para insertar elemnetos a la lista en cualquier poscicion en este caso al final gracias a la funcion len 
print(lista) #se imprime la lista 
