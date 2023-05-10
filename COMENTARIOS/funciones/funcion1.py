def parImpar(num): #creacion de la funcion ParImpar con el parametro num
    if num%2==0: #cuerpo de la funcion el cual indica si num es un numero par
        #print('par')
        return 'par' #se retorna la palabra par si el numero es par 
    else:
        #print('impar')
        return 'impar' #si el numero es impar se retorna impar

print(parImpar(36)) #se imprime la funcion ParImpar con el parametro declarado con el nuemro 36
parImpar(5) #se llama la funcion ParImpar con el paametro 5 "impar"
parImpar(2) #se llama la funcion ParImpar con el paametro 2 "par"
parImpar(7) #se llama la funcion ParImpar con el paametro 7 "impar"

def perfecto(num): #creacion de la funcion perfecto con el parametro num
    sum=0 #asignacion a una variable servira para sumar los numeros 
    for i in range(1,num): #bucle for de el rango 1 hasta num
        if num%i==0: #si el modulo entre num y i es igual a 0 se ejecutara el bloque if 
            sum+=i #se suma el valor actuar de la suma y i 
    if sum==num: #se ejecuta el bloque si la suma y num es igual
        #print('perfecto')
        return 'perfecto' #se retorna el la palabra perfecto
    else:
        #print('no esperfecto')
        return 'no es perfecto' #se retorna no es perfecto

perfecto(6) #perfecto  
perfecto(10) #no es perfecto
print(perfecto(28)) #se imprime en la pantalla  perfecto
perfecto(21) #no es perfecto