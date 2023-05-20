a,b,c=[],(),{} #asignacion a variables a, b, c
diccionario={} #diccionario vacio
print(type(a)) #tipo lista
print(type(b)) #tipo tupla
print(type(c)) #tipo diccionario

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"} #diccionario con sus respectivas claves y valores
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310} #diccionario con sus respectivas claves y valores esta vez con valores numerocos 
empty_dictionary = {} #diccionario vacio

d1={1:50,'1':200,3:300,0:'100'} #se crea un diccionario con sus claves y valores esta vez se alternan tipos de datos para las claves y los valores 
print(d1) #se imprime el diccionario d1

print(dictionary) #se imprime el diccionario dictionary
print(phone_numbers) #se imprime el diccionario phone_numbers
print(empty_dictionary) #se imprime el diccionario empty_dictionary

print(f'gato en frances= {dictionary["gato"]}') #se imprime el valor del diccionario asociado a la clave gato

#se escribe el diccionario de manera mas legible 
dictionary = {"gato": "chat", 
              "perro": "chien", 
              "caballo": "cheval"}
#se crea una lista word nos servira para buscar dentro el diccionario
words = ['gato', 'león', 'caballo']
 #word se usara como variable de control de word donde cada vuelta se ñe asigna el valor siguiente 
for word in words:
    if word in dictionary: #buscar word esta en el diccionario
        print(word, "->", dictionary[word]) #se imprime word en su valor actual y el valor del diccionario asociano a la clave con el valor de word 
    else: #si no esta en el diccionario
        print(word, "no está en el diccionario") #se imprime el texto para instruir al usuario que no se encuentra esta palabra 
        
print(f'las claves de dictionary: {dictionary.keys()}') #metodo keys imprime las claves que estan en el diccionario 

for x in dictionary.keys(): #variable de control x la cual toma todas las claves del diccionario
    print('clave',x,'valor',dictionary[x])#este print imprime x la cual tomara las claves y de misma forma imprimira el valor de la clave buscando en en diccionario x
    
for x in dictionary.items(): #.items nos arrojara las claves con sus valores pero esta vez cada par en una tupla 
    print(x)#se imprime x que sera igual a una tupla con contenido de clave y valor del diccionario
    print('clave=',x[0]) #se imprime la clave que este caso corresponde a la posicion 0 de la tupla x
    print('valor=',x[1]) #se imprime el valor que en este caso corresponde a la posicion 1 de la lista  
    
dictionary["gato"]='minou' #reasignacion de un valor de la clave gato 
print(dictionary) #se imprime el diccionario con la modificacion anterio
dictionary['cisne'] = 'cygne' #se crea una nueva clave con un valor 
dictionary.update({"pato": "canard"}) #otra forma de crear claves con valores .update
print(dictionary) #se imprime el diccionario con todas sus modificaciones 

del dictionary['perro'] #se elimita la clave perro con su valor del diccionario
print(dictionary) #se imprime el diccionario con la modificacion anterio 
dictionary.popitem() #metodo .popitem este elimina el ultimo elemento de un diccionario
print(dictionary) #se imprime el diccionario con su modificacion anteriors