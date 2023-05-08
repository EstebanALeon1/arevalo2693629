#Determinar los divisores de un número introducido por teclado

num = int(input("Digite el numero el cual quiera conocer los divisores: "))
for i in range(1, 11):
    if num%i == 0:
        print(f"los divisores del numero {num} son los sigientes\n {i}")