#Algoritmo para hallar el m.c.d de dos números m y n por el algoritmo de Euclides.
num_1 = int(input("Digite un numero: "))
num_2 = int(input("Digite un numero: "))
mayor = 0
menor = 0
if num_1 > num_2:
    mayor = num_1
    menor = num_2
elif num_2 > num_1:
    mayor = num_2
    menor = num_1
residuo = 0
while residuo <= 1:
    residuo = mayor % menor
    residuo = menor % residuo
    menor = residuo
    print(residuo)