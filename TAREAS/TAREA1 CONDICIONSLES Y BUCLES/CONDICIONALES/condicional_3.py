#solicite al usuario un numero entero, si el numero es positivo imprima en la pantalla "este numero es positivo", si el numero es igual a 0 imprima en la pantalla "este es un numero neutro", si el numero es negativo imprima en la pantalla "el numero es negativo" 
numero = int(input("Digite un numero: "))
if numero > 0:
    print("Este numero es positivo")
elif numero == 0:
    print("Este numero es neutro")
else:
    print("Este nuemro es negativo")            