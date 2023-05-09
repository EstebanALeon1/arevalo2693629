import math #Se importa la funcion math sirve para diversas operaciones matematicas 
import random #se importa la funcion ramdon 

print(math.sqrt(100)) #se imprime la raiz cuadrada de 100
print(math.pow(2,5)) #se imprime la exponenciacion de 2 a la 5

num=int(random.random()*100) #se le asigna a num un numero ramdom de 0 a 100
print(num) #se imprime el numero 
num1=random.randint(10,20) #se le asigna a num1 un numero ramdon de 1 a 20
print(num1) #se imprime numero 2


def saludo(nombre): #se declara una funcion con el parametro nombre 
    return f'Hola {nombre}' #este es un argumento de la funcion es la accion que va a ejecutar cuando se llame 

var=saludo('Soacha') #se le asigna a var la funcion saludo con el parametro soacha 
print(len(var)) #se imprime el tamaño de var 
print(var) #se imprime var 


saludo('Maria') #funcion con parametro maria 
saludo('Pedro') #funcion con parametro pedro 
saludo('Ana') #funcion con parametro ana