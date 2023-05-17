#Busqueda, decir cuantas veces está y en que posiciones
import random
lista_1 = [random.randrange(100) for i in range(random.randint(5, 15))]
print(lista_1)
def BuscarNumero(lista):
    num_buscar = int(input("Digite el numero que desea buscar: "))
    contador = 0
    for i in range(len(lista)):
        contador = 0
        for j in range(len(lista)):
            if lista[i] == lista[j]:
                if lista[i] == num_buscar:
                    contador += 1
                print(f"el numero que desea buscar esta en la poscicion [{i}] y se repite {contador} veces")
BuscarNumero(lista_1)
