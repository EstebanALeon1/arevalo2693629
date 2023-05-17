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

print(f'gato en frances= {dictionary["gato"]}')

dictionary = {"gato": "chat", 
              "perro": "chien", 
              "caballo": "cheval"}

words = ['gato', 'león', 'caballo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")
        
print(f'las claves de dictionary: {dictionary.keys()}')

for x in dictionary.keys():
    print('clave',x,'valor',dictionary[x])
    
for x in dictionary.items():
    print(x)
    print('clave=',x[0])
    print('valor=',x[1])
    
dictionary["gato"]='minou'
print(dictionary)
dictionary['cisne'] = 'cygne'
dictionary.update({"pato": "canard"})
print(dictionary)

del dictionary['perro']
print(dictionary)
dictionary.popitem()
print(dictionary) 