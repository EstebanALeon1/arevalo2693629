import random # se improta ramdom 

#diferentes formas de crear tuplas 
t1=(1,2,3)
t2=()
t3=1,20,300,4
print(t3) #se imprime la tupla t3
t3=t3+(543,) #asignacion de t3 a t3 mas la tupla (543,)
print(t3) #se imprime la tupla t3

#No se llena por comprensión
# tupla=(for x in range(10))
# print(tupla)

#impresion del tipo de dato que son las tuplas y se imprimen las tuplas antes creadad 
print(type(t2))
print(t1)
print(t2)
print(t3)
t4=100, #creacion de una tupla con solo un elemento
t5=(100,1,2,3,4) #creacion de tupla con varios elementos 
print(len(t5)) #se imprime el tamaño de la tupla t5
for x in t5: #asigna a x todos los varores contenidos en t5 en cada vuelta del bucle
    print(x) #se imprime cada valor de la tupla t5
#t5.append(200)
print(t5) #se imprime la tupla t5
print('...',t3+t5) #se imprime la suma o la union de la lista t3 y t5 
print(t5*2) #se imprime la lista t5 por 2 es decir (100,1,2,3,4,100,1,2,3,4)
print(1000 not in t5) #verificacion si 1000 no esta en t5 resultado True
print(100 in t5) #verifica si 100 esta en t5 resultado True

#creacion de tuplas y de una variable que luego se asigna como elemento de otra tupla 
var=1
t11 = (1, )
t21 = (2, )
t31 = (3, var)
 
t11, t21, t31 = t21, t31, t11 #se cambian los valores de las tuplas esto es parecido a las asignaciones o cambio de valores de variables en una sola lines 
 
print(t11, t21, t31) #se imprimen las anteriores listas 

tt=(1,'a','cadena') #las tuplas pueden contener diferentes tipos de datos
print(tt) #se imprime la anterior tupla

#forma de engañar a python y agregar valores a una tupla
tam=random.randint(10,20) #tam sera un numero aleatorio
t=() #tupla vacia
for i in range(tam): #i tomara todos los valores de tam esto se define como las vueltas de bucle que va a realizar for 
    n=random.randrange(100) #n sera un numero aleatorio de 0 a 100
    t=t+(n,) #la tupla se le asignara el valor de t mas la tupla que n genere  
print(t) #se imprime t con todos sus valores 

#uso de rebanadas con las tuplas 
mitad=int(len(t)/2)
print(t[0:mitad])
print(t[mitad:])

