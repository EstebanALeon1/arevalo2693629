#Determinar si un número es o no es perfecto. Un numero es perfecto si la suma de sus divisores sin incluir el propio número es igual a este
num = int(input("Digite el numero el cual quiera saber si es un mnumero perfecto: "))
num_perfecto  = 0
for i in range(1, num+1):
    if num % i == 0:
        num_perfecto = num_perfecto + i / 2
if num_perfecto == num:
    print(f"El numero {num} es un numero perfecto")
else:
    print(f"El numero {num} no es un numero perfecto")
        
        
