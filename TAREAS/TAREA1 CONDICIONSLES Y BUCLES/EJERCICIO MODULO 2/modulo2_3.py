#Solicite al usuario dos números enteros realice las operaciones matemáticas básicas e imprima las en la pantalla
numero_1 = int(input("Digite un numero entero: ")) 
numero_2 = int(input("Digite un numero entero: ")) 
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multipricacion = numero_1 * numero_2
division = numero_1 / numero_2
expo = numero_1 ** numero_2
print(f"""el resultado de la suma es de {suma}
     el resultado de la resta es de {resta}
     el resultado de la multiplicacion es de {multipricacion} 
     el resultado de la division es de {round(division, 2)}
     el resultado de la exponenciacion es de {expo}""")
