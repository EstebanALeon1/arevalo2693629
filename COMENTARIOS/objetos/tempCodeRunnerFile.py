#se cera una clase de prueba 
class Prueba:
    
    contador=0 #se crea un contador
    
    #constructor de la clase con un argumento predefinido
    def __init__(self,var=1):
        self.__var=var
    
    #se crea un metodo con otra variable
    def otraVariable(self,var2):
        self.__var2=var2

#se imprime el diccionario con los argumentos y los valores de la clase 
print(Prueba.__dict__)