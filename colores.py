#diccionario español ingles
diccionario = {"azul":"blue",
               "verde":"green",
               "cafe":"brown",
               "blanco":"white",
               "rojo":"red",
               "rosado":"pink",
               "naranja":"orange",
               "negro":"black",
               "amarillo":"yellow",
               "morado":"purple"
               }
colores = ["dorado","negro","azul","plateado","verde", "lila", "salmon", "amarillo", "rojo", "rosado"]
for color in colores:
    if color in diccionario:
        print(f'El color {color} en ingles es {diccionario[color]}')
    else:
        print(f"el color {color} no esta en el diccionario")
