#Determinar si un numero es o no es primo
num = int(input("Digite el numero el cual quiera saber si es primo: "))
num_primo = 0
for i in range(1, num+1):
    if num % i == 0:
        num_primo += 1
        
if num_primo == 2:
    print("Este numero es primo")
    
if num_primo > 2:
    print("Este numero no es primo")
    
