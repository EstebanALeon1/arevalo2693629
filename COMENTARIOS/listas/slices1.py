import random
tam =random.randint(5, 20)
#tam=10#
lista = [random.randrange(100) for i in range(tam)]
rebanada = lista[3:7]
print(lista)
print(rebanada)



#rebanada de la lista de la mitas para delante 
rebanada_mitad = lista[tam//2:]
print(rebanada_mitad)