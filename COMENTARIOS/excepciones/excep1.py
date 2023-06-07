#las exepciones se utilizan para evitar que un programa se detenga a causa de un error, nos permite tratar cada uno de ellos 

#aqui pondremos en codigo que tenemos sospechas que generara un error 
try: 
    num=10
    for i in range(num):    
        if num%i==0:
            print(i,"es divisor")
            
#en caso de que try encuentre un error el bloque exept se ejecutara tratando el error                
except:
    print('Error')
print('Este programa continua')


#aqui pondremos en codigo que tenemos sospechas que generara un error 
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)
    lista=[1]
    print(lista[0.5])
    
 #aqui tenemos el bloque exept con una gran diferencia esta vez cada uno especifica un nombre de exepcion concreto o de error, dependiendo el error que genere el bloque try va a entrar a ejecutarse el bloqye except correspondiente a la exepcion generada 
 
 #se ejecutara este except si el bloque try genera una excepcion de tipo ValueError   
except ValueError:
    print('Hubo un Error tipo VALUE')
    
#se ejecutara este except si el bloque try genera una excepcion de tipo ZeroDivisionError
except ZeroDivisionError:
    print('Hubo un Error tipo ZERO division')
    
#se ejecutara este except si el bloque try genera una excepcion de tipo TypeError
except TypeError:
    print('Hubo un error indeterminado')

#en caso que ninguno de los errores anteriores hayan sido generados y por el contrario se genere uno desconocido(no especificato) se ejecutara este ultimo except es como declarar la excepcion como BaseException que segun el arbol de jerarquia es la raiz de todas
except:
    print('Otro error')

# t=(1,)
# t.append(10)

#este bloque ejecutara una excepcion SyntaxError
try:
    raise SyntaxError #raise es utilizada para probar exepciones
#este bloque tratara la excepcion SyntaxError
except:
    print('Testing con raise y syntax error')
    
#bloque try con cosigo que posiblemente pueda fallar y generar excepciones
try:
    temperature = float(input('Ingresa la temperatura actual:'))

    if temperature > 0:
        print("Por encima de cero")
    elif temperature < 0:
        print("Por debajo de cero")
    else:
        print("Cero")
#se ejecutara el bloque en caso de que se genere un nombre incorrecto para el bloque try
except NameError:
    print('name error')
    