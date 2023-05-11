#Calcular el máximo de números positivos introducidos por teclado, sabiendo que metemos números hasta que introduzcamos uno negativo. El negativo no cuenta.
num = int(input("Ingrese un numero positivo, para finalizar el programa ingrese cualquier numero negativo: "))
total_numeros = 0
while num >= 0:
    total_numeros = total_numeros + num
    num = int(input("Ingrese un numero positivo, para finalizar el programa ingrese cualquier numero negativo: "))
print(f"El total de numeros ingresados es {total_numeros}")
print("fin del programa")