import random #se importa ramdom
def llenarLista(tam,rango): #se crea la funcion con dos parametros
    lista=[random.randrange(rango) for i in range(tam)]  #la lista sera llenada con numeros ramdom en el ramgo del primer parametro  
    return lista #se retorna el valor de la lista a la funcion 

def sumaLista(lista):#se crea una funcion
    sum=0 #se crea una variable
    for x in lista: #ciclo for en el rango de la lista analiza cada uno de los elementos
        sum+=x #se suman todos los elementos de la lista gracias a la variable sum y al ciclo for 
    return sum

def promedioLista(lista): #creacion de una funcion
    return sumaLista(lista)/len(lista) #se retorna la division entre la suma de la lista y el tamaño de la lista aqui se utiliza una funcion dentro de otra funcion 
    
l1=llenarLista(3,10) #uso de la funcion de llenarLista con tam definido en 3 y rango en 10 
print(l1) #se imprime la lista ya con valores en su interior 
print(sumaLista(l1)) #se imprime utilizando la funcion sumaLista con el parametro de l1
print(round(promedioLista(l1),2)) #se imprime utilizando la funcion promedio con el parametro de l1 y redondeando decimales a 2

