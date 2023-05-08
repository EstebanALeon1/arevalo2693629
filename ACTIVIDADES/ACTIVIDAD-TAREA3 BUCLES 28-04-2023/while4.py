num  = input("Digite un numero: ")
numero_conver  = None
flag = len(num)
print(len(num))
flag_2 = -1

while flag != 0:
    numero_conver = numero_conver , num[flag_2]
    flag -= 1
    flag_2 -= 1

print(f"El numero {num} invertido es igual a {numero_conver}")