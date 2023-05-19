#Hacer diccionarios español ingles, ingles español de animales. Escriba funciones que permitan alimentar estos diccionarios y usarlos. Genere un menú para cada una de las 4 opciones. 
#Alimentar cada diccionario (2 funciones)
#Usar cada diccionario (2 funciones)
def FunDicciEsp_Ing(diccionario):
    diccionario = {}
    clave = input("Digite la clave que desea agregar: ")
    valor = input("Digite el valor que desea agregar: ")
    if clave not in diccionario:
        while True:
            print("para finalizar el programa digite la palabra terminar")
            clave = input("Digite la clave que desea agregar: ")
            if clave == "terminar":
                break
            valor = input("Digite el valor que desea agregar: ")
            diccionario[clave] = valor
            if clave in diccionario:
                print("Esta clave ya se encuentra en el diccionario")
    return diccionario
def FunDicciIng_Esp(diccionario):
    diccionario = {}
    clave = input("Digite la clave que desea agregar: ")
    valor = input("Digite el valor que desea agregar: ")
    if clave not in diccionario:
        while True:
            print("para finalizar el programa digite la palabra terminar")
            clave = input("Digite la clave que desea agregar: ")
            if clave == "terminar":
                break
            valor = input("Digite el valor que desea agregar: ")
            diccionario[clave] = valor
            if clave in diccionario:
                print("Esta clave ya se encuentra en el diccionario")
    return diccionario
diccionario_esp_ing = {}
diccionario_ing_esp = {}
FunDicciEsp_Ing(diccionario_esp_ing)
FunDicciIng_Esp(diccionario_ing_esp)
#Codifique funciones para alamacenar en tuplas de cada diccionario todos los animales en español y en ingles respectivamente. 
def TuplaDiccioEsp_Ing(diccionario):
    for x in diccionario.values:
        print(f"la clave es {x[0]} y su valor es {x[1]}")
TuplaDiccioEsp_Ing(diccionario_esp_ing)