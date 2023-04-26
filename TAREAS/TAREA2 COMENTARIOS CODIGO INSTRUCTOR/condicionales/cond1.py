x=input('ingrese numero') #entrada de un numero asignado a una variable
y=input('ingrese numero') #entrada de un segundo numero asignado a una variable
if x==y: #uso del condicional para señalar una igualdad entre x & y
    print('son iguales') #imprime en la pantalla son iguales si la condion de if es True
elif x>y: #se ejecuta elif en caso de que if sea de caracter False para señalar que x es mayor que y 
    print('descendente') #se imprime en la pantalla descendente si la condicion de elif es de valor True
else: #se ejecuta else si las otras condiciones son de caracter False para cerrar la condicion if donde se evalua si x es menos a y
    print('ascendente') #se imprime en la pantalla ascendente si el bloque else se ejecuta 