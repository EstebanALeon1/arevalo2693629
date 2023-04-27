#- Lea dos numeros. Garantice que hay uno mayor que el otro. Si no es el caso pidalos de nuevo
num_1 = int(input("Digite un numero: "))
num_2 = int(input("Digite un numero: "))
while not(num_1 > num_2 or num_2 > num_1):
    print("los numeros son iguales digite dos valores diferentes")
    num_1 = int(input("Digite un numero: "))
    num_2 = int(input("Digite un numero: "))


#- Reste el menor del mayor y si el resultado lo permite reste nuevamente. Diga cuanto sobra.


    #asignacion de las variable num_mayor al numero mayor ingresado por el usuario y de la variable num_menor al numero menor ingresado por el usuario dandonos mejor control al siguiente bucle while
num_mayor = 0
num_menor = 0
if num_1 > num_2:
    num_mayor = num_1
else:
    num_mayor = num_2
if num_1 < num_2:
    num_menor = num_1
else:
    num_menor = num_2


    #bucle while en donde se resta el numero menor al numero mayor siempre y cuando num_mayor sea diferente a 0 y mayor que este, tambien se utiliza como control la funcion if para que el programa solo imprima la variable num_mayor siempre y cuando esta sea mayor a 0
while num_mayor > num_menor:
    while num_mayor != 0 and num_mayor >0:
        num_mayor = num_mayor - num_menor
        if num_mayor >= 0:
            print(f"la resta del numero mayor menos el numero menor es igual a {num_mayor} ")
        

