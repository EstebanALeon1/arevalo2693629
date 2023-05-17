dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"} #se crea un diccionario
words = ['gato', 'león', 'caballo'] #se crea una lista 
 
for word in words: #variable word como control tomara cada posicion de la lista words
    if word in dictionary:#si word esta en el diccionario
        print(word, "->", dictionary[word]) #se imprimira la clave y el valor 
    else:#si word no esta en diccionario
        print(word, "no está en el diccionario") #se imprime word y indicara que no pertenece al diccionario