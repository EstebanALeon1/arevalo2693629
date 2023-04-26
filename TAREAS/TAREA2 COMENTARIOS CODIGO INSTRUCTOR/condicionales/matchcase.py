#bloque de codigo de un menu
num1,num2=100,25 #asignacion de variables en una sola linea
print('1-sumar')  #se imprime el primer inten del menu
print('2-restar') #se imprime el segundo inten del menu
print('3-multiplicar') #se imprime el tercero inten del menu
print('4-dividir') #se imprime el cuarto inten del menu
selector=(input('Digite la opcion')) #entrada de un dato digitado por el usuario el cual es una opcion en el munu 
match selector: #se utiliza el condicional match para evaluar la variable selector y encontrar una coincidencia
    case '1': #se ejecuta en caso de que la variable selector sea igial a 1 pero como cadena de texto
        print(num1+num2) #se imprime en la pantalla la suma de dos numeros
    case '2': #se ejecuta en caso de que la variable selector sea igial a 2 pero como cadena de texto
        print(num1-num2) #se imprime en la pantalla la resta entre dos numeros
    case '3': #se ejecuta en caso de que la variable selector sea igial a 3 pero como cadena de texto
        print(num1*num2) #se imprime en la pantalla la multiplicacion de dos numeros
    case '4': #se ejecuta en caso de que la variable selector sea igial a 4 pero como cadena de texto
        print(num1/num2) #se imprime en la pantalla la division de dos numeros 
    