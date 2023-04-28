#solicite un número al usuario, en caso de que esté sea par imprimir en la pantalla "este número es par" de lo contrario imprimir "este número es impar"
numero = int(input("Digite un numero entero: "))
if numero % 2 == 0:
    print("Este es un numero par")
else:
    print("Este es un numero inpar")