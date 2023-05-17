#llenar una tupla con num aleatorios entre 0 y 100 y el tamaño sera aleatorio sera de maximo 20 y imprimirla 
import random
tam = random.randrange(20)
for i in range(random.randrange(20)):
    n = random.randrange(100)
    tupla = tupla + (n,)
print(tupla)
