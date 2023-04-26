#realice un programa donde se cuenten los numeros ingresados al sistema y cuantos de estos son pares y cuantos soi inpares
numeros_pares = 0
numeros_impares = 0
numeros_totales = 0
numero = int(input('Digite un numero o digite "-1" para terminar el sistema\n'))
while numero != -1:
    if numero % 2 == 0:
        numeros_pares += 1
        numeros_totales += 1
        numero = int(input('Digite un numero o digite "fin" para terminar el sistema\n'))

    else:
        numeros_impares += 1
        numeros_totales += 1
        numero = int(input('Digite un numero o digite "fin" para terminar el sistema\n'))

        
print(f"digitaste {numeros_pares} numeros pares, {numeros_impares} numeros inpares para un total de {numeros_totales} numeros totales")