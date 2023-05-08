#programa que evalua si dos numeros son factores 
x=5 #asignacion de el numero 5 a la variable x
y=3 #asignacion de el numero 3 a la variable y

while not (x%y==0 or y%x==0): #se al bucle while este evalua que el modulo de la division entre x y y y bicebersa sea igual a 0    
    print('Rutina para saber si dos numeros son factores') #se imprime en pantalla y sirve para indicar al usuario el punto en el que esta del programa
    x=int(input('ingrese numero')) #asignacion de la variable x a la entrada de los datos digitados por el usuario
    y=int(input('ingrese numero')) #asignacion de la variable y a la entrada de los datos digitados por el usuario   
print('Son factor') #imprime en la pantalla si los numeros ingresados por el usuario son factores comunes
