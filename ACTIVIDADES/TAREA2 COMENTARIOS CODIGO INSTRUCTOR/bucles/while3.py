#prorama que sume todos los numeros digitados por el usuario hallar el promedio, el numero mayor y el numero menor 
num_mayor = -9999
num_menor = 9999
total_num = 0
num=1
control_num = 0
cont=0
while num!=0:
    print("ingrese el numero 0 cuando desee finalizar el programa")
    num=int(input('ingrese numero: '))
    control_num = num
    if control_num> num_mayor:
        num_mayor=control_num
    if control_num<num_menor and control_num!=0:
        num_menor=control_num
        num_menor=control_num
    cont=cont+1 #cont+=1
    total_num +=num
    promedio = total_num
cont-=1
print(f'El usuario ingreso {cont} numeros')
promedio = total_num/cont
#print('El usuario ingreso', cont, 'numeros')
print(f"La suma total de los numeros ingresados es de {total_num}")
print(f"el promedio de la suma de los numeros ingresados es de {promedio}")
print(f"el numero menor ingreado por el usuario es {num_menor}")
print(f"el numero mayor ingreado por el usuario es {num_mayor}")

