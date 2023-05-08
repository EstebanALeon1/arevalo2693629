###Llenar dos arreglos de n elementos con números generados con la función random.
#Compararlos y decir:
#a. Cuál de los dos tiene la suma más alta
#b. Cuál de los dos tiene el número mayor
#c. Cuál de los dos tiene el número menor
#d. Cuál es el promedio conjunto (uniendo los dos arreglos)
#e. Sacar el promedio de cada uno y decir si está por encima o por debajo del arreglo conjunto
#f. Cuál de los dos tiene mayor cantidad de pares
#g. Cuál de los dos tiene mayor cantidad de impares
import random
arreglo_1 = []
arreglo_2 = []
tam_1 = random.randint(1, 15)
tam_2 = random.randint(1, 15)
arreglo_1 = [random.randint(2, 12)for i in range(tam_1)]
arreglo_2 = [random.randint(1, 13)for i in range(tam_2)]
print(arreglo_1)
print(arreglo_2)


#a. Cuál de los dos tiene la suma más alta
suma_1 = 0
suma_2 = 0
for i in arreglo_1:
    suma_1 = suma_1 + i
for j in arreglo_2:
    suma_2 = suma_2 + j
if suma_1 > suma_2:
    print(f'la suma entre los numeros del arreglo uno es igual a {suma_1} y es mayor a la del arreglo dos que es igual a {suma_2}')
elif suma_2 > suma_1:
    print(f'la suma entre los numeros del arreglo dos es igual a {suma_2} y es mayor a la del arreglo dos que es igual a {suma_1}')   
else:
    print(f'la suma entre los dos arreglos tienen el mismo valor de {suma_1}')  


#b. Cuál de los dos tiene el número mayor
num_mayor_1 = 0
num_mayor_2 = 0
for a in arreglo_1:
    if a > num_mayor_1:
        num_mayor_1 = a
for b in arreglo_2:
    if a > num_mayor_2:
        num_mayor_2 = b
if num_mayor_1 > num_mayor_2:
    print(f'el arreglo uno contiene el numero mayor y es {num_mayor_1}')
elif num_mayor_2 > num_mayor_1:
    print(f'el arreglo dos contiene el numero mayor y es {num_mayor_2}')
else:
    print(f'En ambos arreglos coinciden los dos numeros mayores y es el numero {num_mayor_1}')


#c. Cuál de los dos tiene el número menor
num_menor_1 = 999
num_menor_2 = 999
for c in arreglo_1:
    if c < num_menor_1:
        num_menor_1 = c
for d in arreglo_2:
    if d < num_menor_2:
        num_menor_2 = d
if num_menor_1 < num_menor_2:
    print(f'el arreglo uno contiene el numero menor y es {num_menor_1}')
elif num_menor_2 < num_menor_1:
    print(f'el arreglo dos contiene el numero menor y es {num_menor_2}')
else:
    print(f'En ambos arreglos coinciden los dos numeros menores y es el numero {num_menor_1}')


#d. Cuál es el promedio conjunto (uniendo los dos arreglos)
suma_tam = tam_1 + tam_2
suma_arreglos_gen = suma_1 + suma_2
promedio_general = suma_arreglos_gen / suma_tam
print(f'el promedio general de los dos arreglos es de {promedio_general}')


#e. Sacar el promedio de cada uno y decir si está por encima o por debajo del arreglo conjunto
promedio_arre_1 = suma_1 / tam_1
promedio_arre_2 = suma_2 / tam_2

if promedio_arre_1 > promedio_general:
    print(f'el promedio del arreglo uno "{promedio_arre_1}" es mayor al promedio general "{promedio_general}"')
elif promedio_arre_1 < promedio_general:
    print(f'el promedio del arreglo uno "{promedio_arre_1}" es menor al promedio general "{promedio_general}"')
else:
    print(f'el promedio del arreglo uno "{promedio_arre_1}" es igual al promedio general "{promedio_general}"')

if promedio_arre_2 > promedio_general:
    print(f'el promedio del arreglo dos "{promedio_arre_2}" es mayor al promedio general "{promedio_general}"')
elif promedio_arre_2 < promedio_general:
    print(f'el promedio del arreglo dos "{promedio_arre_2}" es menor al promedio general "{promedio_general}"')
else:
    print(f'el promedio del arreglo dos "{promedio_arre_2}" es igual al promedio general "{promedio_general}"')


#f. Cuál de los dos tiene mayor cantidad de pares
pares_1 = 0
pares_2 = 0
for e in arreglo_1:
    if e % 2 == 0:
        pares_1 += 1
for f in arreglo_2:
    if f % 2 == 0:
        pares_2 += 1

if pares_1 > pares_2:
    print(f'el arreglo uno contiene mas pares "{pares_1}" que el arreglo dos "{pares_2}"')
elif pares_2 > pares_1:
    print(f'el arreglo dos contiene mas pares "{pares_2}" que el arreglo uno "{pares_1}"')   
else:
    print(f'el arreglo uno contiene la misma cantidad pares "{pares_1}" que el arreglo dos "{pares_2}"')


#g. Cuál de los dos tiene mayor cantidad de impares
impares_1 = 0
impares_2 = 0
for g in arreglo_1:
    if g % 2 != 0:
        impares_1 += 1
for h in arreglo_2:
    if h % 2 != 0:
        impares_2 += 1

if impares_1 > impares_2:
    print(f'el arreglo uno contiene mas impares "{impares_1}" que el arreglo dos "{impares_2}"')
elif impares_2 > impares_1:
    print(f'el arreglo dos contiene mas impares "{impares_2}" que el arreglo uno "{impares_1}"')   
else:
    print(f'el arreglo uno contiene la misma cantidad impares "{impares_1}" que el arreglo dos "{impares_2}"')