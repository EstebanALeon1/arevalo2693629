#forma de manejar las exepciones en python 
#bloque try con codigo sospechoso de generar una excepcion
try:
    temperature = float(input('Ingresa la temperatura actual:'))

    if temperature > 0:
        print("Por encima de cero")
    elif temperature < 0:
        print("Por debajo de cero")
    else:
        print("Cero")
#bloque except generado en caso de que el bloque try genere una excepcion
except NameError:
    print('name error')
    