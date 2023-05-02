#determinar si dos numeros ingresados son amigos
sum_divisore_1 = 0
num_1 = int(input("Digite el numero el cual quiera conocer si es un numero amigo: "))
for i in range(1, num_1):
    if num_1%i == 0:
        sum_divisore_1 += i

sum_divisore_2 = 0
num_2 = int(input("Digite el numero el cual quiera conocer si es un numero amigo: "))
for j in range(1, num_2):
    if num_2%j == 0:
        sum_divisore_2 += j

if sum_divisore_1 == num_2 and sum_divisore_2 == num_1:
    print("Estos numeros son amigos")
else:
    print("Estos numeros no son amigos")

