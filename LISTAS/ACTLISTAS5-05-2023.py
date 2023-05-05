#llenar un arreglo por comprension de minimo 10 y maxiomo 15 donde los elementos sean numeros aleatorios de 0 a 9$$$$
#buscar un numero ingresado por teclado, decir si esta, decir si esta repetido, decir si esta repetido, cuantas veces esta
#diga las posiciones donde las encontro 


import random


lista = [random.randint(0, 9) for i in range(random.randint(10, 15))]

print(lista)
print(len(lista))


num_teclado = int(input("Digite un numero de 0 a 9: "))
poscicion = 0
repeticion = 0
for i in lista:
    if i == num_teclado:
        repeticion += 1
        poscicion = lista[i]
    print(poscicion)
        
    
           
if repeticion > 0:
     print(f'Este numero se encuentra en la lista y se repite {repeticion} veces y en encuentran en la poscicion ')
else:
    print('el numero no esta')
    
print(lista.index(i))


   