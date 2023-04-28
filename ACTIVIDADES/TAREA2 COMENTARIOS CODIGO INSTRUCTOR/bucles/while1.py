i=1 #asignacion de el numero 1 a la variable i
sum=0 #asignacion del numero 0 a la variable sum
#indentacion
while i<=10: #se hace uso del la estructura de control bucle while
    print(i) #se imprime el valor de i en pantalla
    sum+=i #sum=sum+i #se asigna a la variable sum la suma de sum + la variable i
    i+=1 #i=i+1 #este es un contador 
print('la suma es:',sum) #se imprime en la pantalla el valor actual de la variable sum

i=0 # asignacion de el numero 0 a la variable i
sp,si=0,0 #asignacion de dos variables sp y si en una misma linea la cual a las dos se les asigna el valor 0
while i<=10: #se hace uso del la estructura de control bucle while
    print(i) #se imprime el valor de i en pantalla
    if i%2==0: #se hace uso de el condicional if donde evalua que el residuo de i dividido en dos es igual a 0
        sp+=i #se asigna a la variable sp la suma de sp + la variable i
    else: #se llama la condicional else se ejecutara en caso de que la condicion el if no se cumpla 
        si+=i #se asigna a la variable si la suma de si + la variable i
    i+=1 #i=i+1 #este es un contador 
print('la suma de los pares es:',sp) #se imprime en la pantalla el mensaje de print mas el valor de la variable sp
print('la suma de los impares es:',si) #se imprime en la pantalla el mensaje de print mas el valor de la variable si