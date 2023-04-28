#elaborar un programa que solo imprima las vocales de lo ingresado por el usuario
vocales = input("ingrese una palabra o una frase:")
for x in "a","e","i","o","u":
    if x in vocales:
        print(x)