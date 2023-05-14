#Hallar el factorial de los numeros de una lista y guradarlos en otro lista. Utilice numeros entre 2 y 15 para llenar la lista
import random
lista_1 = [random.randint(2, 15) for i in range(random.randint(2, 15))]
lista_2 = []
print(lista_1)
def factorial(lista, lista_nueva):
    for i in lista:
        if i <= 0:
            return 1
        factorial = 1
        while i > 0:
            factorial = factorial * i
            i -= 1
        lista_nueva.append(factorial)
        return lista_nueva
print(factorial(lista_1, lista_2))