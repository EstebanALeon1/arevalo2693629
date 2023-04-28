#- Solicite al usuario inicio, fin y cantidad a incrementar o decrementar según el caso. Imprima la serie

inicio = int(input("Digite el numero donde se dara inicio a la serie: "))
fin = int(input("Digite el numero donde se dara fin a la serie: "))
incre_decre = int(input("Digite el numero de la contidad a incrementar o decrementar: "))
fin+=1

for i in range(inicio,fin,incre_decre):
    print(i)
    



#- Solicite un numero positivo al usuario(debe incluirse en la serie). Diga cuantos multiplos de n hay en la serie desde cero hasta el numero ingresado. n se ingresa por teclado tambien.

    #encuentra los multiplos de la variable n por la variablo numero ambas asignadas con la informacion que aporta el usuario 

n = int(input("Digite el numero del que quiera hallar los multiplos: "))
numero = int(input("Digite hasta que numero quiere hallar los multiplos: "))
numero+=1
for i in range(inicio,numero,incre_decre):
        print(f"multiplo de {n} por {i} es igual a {n*i}")