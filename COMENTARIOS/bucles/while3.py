#prorama que sume todos los numeros digitados por el usuario hallar el promedio, el numero mayor y el numero menor 
num=1 #asignacion de 1 a la variable num
cont=0 #declaracion de un contador 
sum=0 #creacion de la variabe suma
mayor=0 #creacion de la variable mayor
menor=1000000 #creacion de la variable menor 
while num!=0: #ciclo while qjue se ejecutara mientras num "ingresado por el usuario" no sea igual a 0
    num=int(input('ingrese numero')) #ingreso de los numeros por el usuario
    cont=cont+1 #cont+=1 #se suma 1 al contador
    sum=sum+num #se realiza la suma de los numeros ingresados
    if num>mayor: #condicional if para declarar cual sera el numero mayor ingresado por el usuario
        mayor=num #asignacion a mayor el numero mas grande ingresado por el usuario
    if num<menor and num!=0: #condicional if para declarar cual sera el menor de los numeros ingresados por el usuario 
        menor=num #asignacion a menor al numero menor ingresado por el usuario

print(f'El usuario ingreso {cont-1} numeros') #se imprime cuantos numeros ingreso el usuario
print(f'La suma es {sum}') #se imprime la suma de todos los numeros ingresados
print(f'El promedio es {sum/(cont-1)} numeros') #se imprime el promedio de los numeros ingrsados 
print(f'El mayor es {mayor}') #se imprime el mayor de los numeros ingresados
print(f'El menor es {menor}') #se imprime el menor de los numeros ingresados 
#print('El usuario ingreso', cont, 'numeros')


