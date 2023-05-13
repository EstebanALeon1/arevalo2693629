#Suma pares y promedio de los impares
import random
lista_1 = [random.randrange(100) for i in range(random.randint(5, 15))]
print(lista_1)
def SumaPromedio(lista):
    suma_pares = 0
    suma_impares = 0
    for i in lista:
        if i % 2 == 0:
            suma_pares += i
        if i % 2 != 0:
            suma_impares += i
            promedio = suma_impares/len(lista)
    print(f"la suma de los numeros pares es igual a {suma_pares}")
    print(f"el promedio de los numeros impares es igual a {promedio}")
SumaPromedio(lista_1)