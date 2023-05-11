#Se generara un numero aleatorio y el usuario lo tendra que adivinar para finalizar con la ejecucion del programa
import random

num_aleatorio = int(random.random()*100)
print(num_aleatorio)
num_usuario = int(input("Intenta adivinar el numero, Digita un numero: "))

while num_usuario != num_aleatorio:
    if num_usuario < num_aleatorio:
        print(f"!Pista¡ El numero a adivinar es mayor a {num_usuario}")
    if num_usuario > num_aleatorio:
        print(f"!Pista¡ El numero a adivinar es menor a {num_usuario}")

    print("¡! JA JA JA este numero es incorrecto")
    num_usuario = int(input("Intenta adivinar el numero, Digita un numero: "))

print("Lograste adividar el numero ¡FELICIDADES!")
