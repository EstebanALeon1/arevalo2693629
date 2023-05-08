#Llenar una lista con numero aleatorios (reales con un decimal) que representen calificaciones de un curso. Se evalúa de 0 a 5.
#El curso puede tener entre 20 y 30 aprendices.
#HALLAR

#1. Genere listas nuevas para los aprobados y los reprobados (Se aprueba con 3)
#2. Genere listas nuevas por cada unidad. Es decir, los que sacan de 0 a 1 son un grupo, los de 1 a 2 otro grupo y así sucesivamente
#3. Diga cual es el promedio de los que aprueban y de los que reprueban por separado.
import random

lista =[round(random.uniform(0, 5), 1) for i in range (random.randint(20, 30))]

#1. Genere listas nuevas para los aprobados y los reprobados (Se aprueba con 3)
for i in range(len(lista)): 
    for j in range(i+1,len(lista)): 
        if lista[i]>lista[j]: 
            aux=lista[i] 
            lista[i]=lista[j] 
            lista[j]=aux
for i in lista:
    if i >= 3:
        apro = lista.index(i) 
        break
for j in lista:
    if j < 3:
        repro = lista.index(i) 
        break

aprobados = lista[apro:]
reprobados = lista[:repro]
print(f'El listado de las notas de los alumnos es {lista}')
print(f'El resultado de los alumnos aprobados son{aprobados}')          
print(f'el resultado de loa alumnos reprobados son{reprobados}')
