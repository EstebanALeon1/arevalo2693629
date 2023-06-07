import random

def generar_estaturas(cantidad):
    estaturas = []
    for _ in range(cantidad):
        estatura = round(random.uniform(1.50, 2.00), 2)
        estaturas.append(estatura)
    return estaturas

def ordenar_lista(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

def calcular_quintiles(estaturas):
    estaturas_ordenadas = ordenar_lista(estaturas)
    n = len(estaturas_ordenadas)
    q1 = estaturas_ordenadas[n // 4]
    q2 = estaturas_ordenadas[n // 2]
    q3 = estaturas_ordenadas[(3 * n) // 4]
    return q1, q2, q3

def calcular_cuartiles(estaturas):
    estaturas_ordenadas = ordenar_lista(estaturas)
    n = len(estaturas_ordenadas)
    q1 = estaturas_ordenadas[n // 4]
    q2 = estaturas_ordenadas[n // 2]
    q3 = estaturas_ordenadas[(3 * n) // 4]
    return q1, q2, q3

# Generar la lista de estaturas
estaturas = generar_estaturas(15)

# Calcular los quintiles
q1, q2, q3 = calcular_quintiles(estaturas)
print("Quintiles:")
print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)

# Calcular los cuartiles
c1, c2, c3 = calcular_cuartiles(estaturas)
print("Cuartiles:")
print("C1:", c1)
print("C2:", c2)
print("C3:", c3)