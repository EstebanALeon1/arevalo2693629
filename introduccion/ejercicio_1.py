#solicite dos numeros al usuario diga si estan en orden acsendente, descendente o si son iguales
nuemero_1 = int(input("Didite un numero: "))
numero_2 = int(input("Didite un numero: "))
if nuemero_1 > numero_2:
    print("estan en arden ascendente")
elif nuemero_1 < numero_2:
    print("estan en ordes descendente")
else:
    print("estos numeros son iguales")